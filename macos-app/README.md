# Tutorial Screenshot Capturer - macOS Desktop App

A Python desktop application that captures screenshots on every click system-wide. Works on **ALL applications and websites** including Google AI Studio, Chrome settings, and any other page.

## Features

✅ **System-wide click detection** - Works everywhere on macOS  
✅ **Automatic screenshot capture** - Captures on every click  
✅ **Red circle highlights** - Shows where you clicked  
✅ **Rate limiting** - Prevents capturing too fast (500ms minimum)  
✅ **HTML export** - Generates beautiful tutorial page  
✅ **Works on ALL pages** - Including Google AI Studio, Chrome settings, etc.  

## Installation

### Prerequisites

- macOS (10.14 or later)
- Python 3.8 or later
- Homebrew (optional, for easy Python installation)

### Step 1: Install Python (if not already installed)

Check if Python is installed:
```bash
python3 --version
```

If not installed, install via Homebrew:
```bash
brew install python3
```

Or download from [python.org](https://www.python.org/downloads/)

### Step 2: Install Dependencies

Navigate to the macos-app directory and install required packages:

```bash
cd "macos-app"
pip3 install -r requirements.txt
```

### Step 3: Grant Accessibility Permissions

The app needs permission to monitor mouse clicks:

1. Run the app once (it will fail, but that's okay):
   ```bash
   python3 screenshot_capturer.py
   ```

2. Go to **System Settings** → **Privacy & Security** → **Accessibility**

3. Click the **+** button and add **Terminal** (or your terminal app)

4. Enable the checkbox next to Terminal

## Usage

### Start the App

```bash
cd "macos-app"
python3 screenshot_capturer.py
```

### Capture Screenshots

1. Press **ENTER** to start capturing
2. Click anywhere on your screen (any app, any website)
3. Each click will:
   - Capture a screenshot
   - Add a red circle highlight
   - Save to `~/TutorialScreenshots/session_YYYYMMDD_HHMMSS/`
4. Press **Ctrl+C** to stop capturing
5. HTML tutorial will be automatically generated

### View Your Tutorial

After stopping capture, open the generated HTML file:

```bash
open ~/TutorialScreenshots/session_*/tutorial.html
```

Or navigate to `~/TutorialScreenshots/` in Finder and open the latest session folder.

## How It Works

1. **Click Detection**: Uses `pynput` to monitor all mouse clicks system-wide
2. **Screenshot Capture**: Uses `Pillow` (PIL) to capture the entire screen
3. **Highlight Drawing**: Draws red circles on screenshots at click positions
4. **HTML Generation**: Creates a formatted tutorial page with all screenshots

## Output Structure

```
~/TutorialScreenshots/
└── session_20250930_063300/
    ├── screenshot_001.png
    ├── screenshot_002.png
    ├── screenshot_003.png
    └── tutorial.html
```

## Troubleshooting

### "Operation not permitted" error

You need to grant Accessibility permissions:
- Go to **System Settings** → **Privacy & Security** → **Accessibility**
- Add and enable your Terminal app

### Screenshots are blank

Make sure you granted Screen Recording permissions:
- Go to **System Settings** → **Privacy & Security** → **Screen Recording**
- Add and enable your Terminal app

### Python not found

Install Python 3:
```bash
brew install python3
```

### Module not found errors

Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Advantages Over Browser Extension

✅ Works on **ALL pages** (Google AI Studio, Chrome settings, etc.)  
✅ Works across **ALL applications** (not just browsers)  
✅ No browser restrictions or security policies  
✅ System-level access  
✅ More reliable screenshot capture  

## Limitations

- Requires Python installation
- Needs Accessibility permissions
- macOS only (for now)
- Captures entire screen (not just active window)

## Future Enhancements

- [ ] GUI interface (instead of command line)
- [ ] Active window only capture option
- [ ] Voice transcription with Google Gemini
- [ ] Markdown export option
- [ ] Custom highlight colors
- [ ] Keyboard shortcuts for start/stop

## License

Free to use and modify for personal and commercial projects.

## Support

If you encounter issues:
1. Check that Python 3.8+ is installed
2. Verify Accessibility permissions are granted
3. Make sure all dependencies are installed
4. Check the terminal output for error messages
