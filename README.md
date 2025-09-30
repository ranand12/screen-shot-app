# Tutorial Screenshot Capturer

A macOS application that automatically captures screenshots during tutorial sessions and generates an HTML summary.

## Features

- Captures screenshots at regular intervals during tutorial sessions
- Generates an organized HTML page with all screenshots
- Saves sessions with timestamps for easy reference
- Simple command-line interface

## Installation

See [macos-app/QUICKSTART.md](macos-app/QUICKSTART.md) for quick installation instructions.

For detailed setup information, see [macos-app/README.md](macos-app/README.md).

## Quick Start

1. Install dependencies:
   ```bash
   cd macos-app
   ./install.sh
   ```

2. Run the application:
   ```bash
   python screenshot_capturer.py
   ```

3. Follow the prompts to start/stop capturing screenshots

## Requirements

- macOS (uses native screenshot capabilities)
- Python 3.x
- See [macos-app/requirements.txt](macos-app/requirements.txt) for Python dependencies

## Output

Screenshots are saved to `~/TutorialScreenshots/` with session-based organization and an HTML summary page.
