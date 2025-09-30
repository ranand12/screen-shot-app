#!/bin/bash
# Installation script for Tutorial Screenshot Capturer

echo "=============================================="
echo "Tutorial Screenshot Capturer - Installation"
echo "=============================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo ""
    echo "Please install Python 3:"
    echo "  Option 1: brew install python3"
    echo "  Option 2: Download from https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"
echo ""

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed"
    echo "Please install pip3 or reinstall Python 3"
    exit 1
fi

echo "✅ pip3 found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Installation complete!"
    echo ""
    echo "=============================================="
    echo "Next Steps:"
    echo "=============================================="
    echo ""
    echo "1. Grant Accessibility permissions:"
    echo "   - Go to System Settings → Privacy & Security → Accessibility"
    echo "   - Click + and add Terminal (or your terminal app)"
    echo "   - Enable the checkbox"
    echo ""
    echo "2. Grant Screen Recording permissions:"
    echo "   - Go to System Settings → Privacy & Security → Screen Recording"
    echo "   - Add and enable Terminal"
    echo ""
    echo "3. Run the app:"
    echo "   python3 screenshot_capturer.py"
    echo ""
    echo "=============================================="
else
    echo ""
    echo "❌ Installation failed"
    echo "Please check the error messages above"
    exit 1
fi
