# Quick Start Guide

## Step-by-Step Instructions to Run the App

### Step 1: Open Terminal

1. Press `Cmd + Space` to open Spotlight
2. Type "Terminal" and press Enter

### Step 2: Navigate to the App Folder

```bash
cd "/Users/rajanandk/Gemini CLI experiments 2025/tutorial capturer/macos-app"
```

### Step 3: Install Dependencies (First Time Only)

```bash
pip3 install -r requirements.txt
```

If you don't have pip3, install it first:
```bash
brew install python3
```

### Step 4: Run the App

```bash
python3 screenshot_capturer.py
```

### Step 5: Start Capturing

1. You'll see a welcome message
2. Press **ENTER** to start capturing
3. Click anywhere on your screen (Google AI Studio, any app, any website)
4. Each click will capture a screenshot with a red circle
5. Press **Ctrl+C** when done

### Step 6: View Your Tutorial

The app will tell you where the files are saved. Open the HTML file:

```bash
open ~/TutorialScreenshots/session_*/tutorial.html
```

Or use Finder:
1. Press `Cmd + Shift + G`
2. Type: `~/TutorialScreenshots`
3. Open the latest session folder
4. Double-click `tutorial.html`

## Troubleshooting

### "Permission denied" or "Operation not permitted"

You need to grant permissions:

1. **Go to System Settings** (or System Preferences on older macOS)
2. Click **Privacy & Security**
3. Click **Accessibility** in the left sidebar
4. Click the **+** button
5. Navigate to **Applications** → **Utilities** → **Terminal**
6. Click **Open**
7. Enable the checkbox next to Terminal

Also do the same for **Screen Recording**:
1. In Privacy & Security, click **Screen Recording**
2. Add Terminal and enable it

### "python3: command not found"

Install Python:
```bash
brew install python3
```

If you don't have Homebrew:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### "No module named 'pynput'" or "No module named 'PIL'"

Install dependencies:
```bash
pip3 install -r requirements.txt
```

## That's It!

You're ready to capture tutorial screenshots on ANY page including Google AI Studio!
