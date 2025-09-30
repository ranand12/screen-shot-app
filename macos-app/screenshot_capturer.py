#!/usr/bin/env python3
"""
Tutorial Screenshot Capturer - macOS Desktop App
Captures screenshots on every click system-wide
"""

import os
import time
import json
from datetime import datetime
from pathlib import Path
from pynput import mouse
from PIL import ImageGrab, ImageDraw, ImageFont
import threading

class ScreenshotCapturer:
    def __init__(self):
        self.is_capturing = False
        self.screenshots = []
        self.output_dir = Path.home() / "TutorialScreenshots"
        self.output_dir.mkdir(exist_ok=True)
        self.session_dir = None
        self.last_capture_time = 0
        self.min_capture_interval = 0.5  # 500ms between captures
        
    def start_capture(self):
        """Start capturing screenshots on clicks"""
        self.is_capturing = True
        self.screenshots = []
        
        # Create session directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_dir = self.output_dir / f"session_{timestamp}"
        self.session_dir.mkdir(exist_ok=True)
        
        print(f"\n✅ Capture started!")
        print(f"📁 Screenshots will be saved to: {self.session_dir}")
        print("🖱️  Click anywhere to capture screenshots")
        print("⌨️  Press Ctrl+C to stop capturing\n")
        
    def stop_capture(self):
        """Stop capturing and generate HTML"""
        self.is_capturing = False
        
        if self.screenshots:
            print(f"\n🛑 Capture stopped. Total screenshots: {len(self.screenshots)}")
            self.generate_html()
        else:
            print("\n🛑 Capture stopped. No screenshots captured.")
    
    def on_click(self, x, y, button, pressed):
        """Handle mouse click events"""
        if not pressed or not self.is_capturing:
            return
        
        # Rate limiting
        current_time = time.time()
        if current_time - self.last_capture_time < self.min_capture_interval:
            print("⏭️  Click too fast, skipping...")
            return
        
        self.last_capture_time = current_time
        
        # Capture screenshot in a separate thread to avoid blocking
        threading.Thread(target=self.capture_screenshot, args=(x, y)).start()
    
    def capture_screenshot(self, click_x, click_y):
        """Capture screenshot and add click highlight"""
        try:
            # Capture the screen
            screenshot = ImageGrab.grab()
            
            # Get the actual screenshot dimensions
            screenshot_width, screenshot_height = screenshot.size
            
            # macOS Retina displays have a scale factor (usually 2x)
            # We need to scale the click coordinates to match the screenshot resolution
            import AppKit
            screen = AppKit.NSScreen.mainScreen()
            scale_factor = screen.backingScaleFactor()
            
            # Scale the click coordinates
            scaled_x = int(click_x * scale_factor)
            scaled_y = int(click_y * scale_factor)
            
            print(f"  Original coords: ({click_x}, {click_y})")
            print(f"  Scale factor: {scale_factor}")
            print(f"  Scaled coords: ({scaled_x}, {scaled_y})")
            print(f"  Screenshot size: {screenshot_width}x{screenshot_height}")
            
            # Add click indicator - ONLY an arrow pointing to the click location
            draw = ImageDraw.Draw(screenshot, 'RGBA')
            
            # Arrow configuration
            arrow_length = int(60 * scale_factor)  # Length of arrow from top
            arrow_start_y = scaled_y - arrow_length
            arrow_width = int(4 * scale_factor)  # Thicker arrow for visibility
            
            # Draw arrow line pointing down to click location
            draw.line(
                [scaled_x, arrow_start_y, scaled_x, scaled_y],
                fill=(255, 0, 0),
                width=arrow_width
            )
            
            # Draw arrow head (triangle pointing down)
            arrow_head_size = int(12 * scale_factor)  # Width of arrow head
            arrow_head_height = int(16 * scale_factor)  # Height of arrow head
            draw.polygon(
                [
                    (scaled_x, scaled_y),  # Point at click location
                    (scaled_x - arrow_head_size, scaled_y - arrow_head_height),
                    (scaled_x + arrow_head_size, scaled_y - arrow_head_height)
                ],
                fill=(255, 0, 0)
            )
            
            # Save screenshot
            screenshot_num = len(self.screenshots) + 1
            filename = f"screenshot_{screenshot_num:03d}.png"
            filepath = self.session_dir / filename
            screenshot.save(filepath)
            
            # Store metadata
            self.screenshots.append({
                'number': screenshot_num,
                'filename': filename,
                'filepath': str(filepath),
                'timestamp': datetime.now().isoformat(),
                'click_position': {'x': click_x, 'y': click_y}
            })
            
            print(f"📸 Screenshot {screenshot_num} captured at ({click_x}, {click_y})")
            
        except Exception as e:
            print(f"❌ Error capturing screenshot: {e}")
    
    def generate_html(self):
        """Generate HTML tutorial page"""
        html_file = self.session_dir / "tutorial.html"
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Tutorial Screenshots - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        h1 {{
            color: #333;
            text-align: center;
        }}
        .info {{
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }}
        .screenshot {{
            background: white;
            margin: 30px 0;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .screenshot h2 {{
            color: #0066cc;
            margin-top: 0;
        }}
        .screenshot img {{
            max-width: 100%;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        .metadata {{
            margin-top: 10px;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 4px;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>📸 Tutorial Screenshots</h1>
    <div class="info">
        <p>Generated on {datetime.now().strftime('%B %d, %Y at %I:%M:%S %p')}</p>
        <p>Total screenshots: {len(self.screenshots)}</p>
    </div>
"""
        
        for screenshot in self.screenshots:
            timestamp = datetime.fromisoformat(screenshot['timestamp'])
            html += f"""
    <div class="screenshot">
        <h2>Step {screenshot['number']}</h2>
        <img src="{screenshot['filename']}" alt="Screenshot {screenshot['number']}">
        <div class="metadata">
            <strong>Time:</strong> {timestamp.strftime('%I:%M:%S %p')}<br>
            <strong>Click Position:</strong> ({screenshot['click_position']['x']}, {screenshot['click_position']['y']})
        </div>
    </div>
"""
        
        html += """
</body>
</html>
"""
        
        with open(html_file, 'w') as f:
            f.write(html)
        
        print(f"\n✅ Tutorial HTML generated: {html_file}")
        print(f"🌐 Open it in your browser to view all screenshots")
    
    def run(self):
        """Run the screenshot capturer"""
        print("=" * 60)
        print("Tutorial Screenshot Capturer - macOS Desktop App")
        print("=" * 60)
        print("\nCommands:")
        print("  Press ENTER to start capturing")
        print("  Press Ctrl+C to stop and generate HTML")
        print("=" * 60)
        
        try:
            input("\nPress ENTER to start capturing...")
            self.start_capture()
            
            # Start mouse listener
            with mouse.Listener(on_click=self.on_click) as listener:
                listener.join()
                
        except KeyboardInterrupt:
            self.stop_capture()
            print("\n👋 Goodbye!")

if __name__ == "__main__":
    capturer = ScreenshotCapturer()
    capturer.run()
