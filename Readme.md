# Electron + Python

## Quick Start

1. Install dependencies:
```bash
npm install
pip install -r requirements.txt

2. Run in development:
```bash
python backend.py    
npm start 

3. Build for production:
```bash
pyinstaller --onefile backend.py
npm run build

# 🏗️ Architecture Overview

┌─────────────────────────────────────────────────────────────┐
│                    Final .AppImage File                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │   Electron App  │    │     Python Backend              │ │
│  │                 │    │                                 │ │
│  │ • main.js       │◄──►│ • backend (executable)          │ │
│  │ • index.html    │    │ • Flask server                  │ │
│  │ • JavaScript    │    │ • REST API                      │ │
│  │ • CSS           │    │                                 │ │
│  └─────────────────┘    └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘

# 🔄 How Communication Works

## Development Mode:

┌─────────────────┐    HTTP Requests    ┌─────────────────┐
│  Electron App   │ ───────────────────► │  Python Server  │
│  (localhost)    │ ◄─────────────────── │  (localhost:5000)│
│                 │    JSON Responses    │                 │
└─────────────────┘                     └─────────────────┘

## Production Mode (Built App):

┌─────────────────────────────────────────────────────────┐
│                Single .AppImage File                    │
│  ┌─────────────────┐    HTTP/JSON    ┌───────────────┐  │
│  │  Electron App   │ ◄─────────────► │ Python Backend│  │
│  │  (Frontend)     │   localhost:5000 │ (Embedded)   │  │
│  └─────────────────┘                 └───────────────┘  │
└─────────────────────────────────────────────────────────┘

## What's Inside the Final .AppImage
AppImage contents:
├── electron                    Electron runtime
├── resources/
│   ├── app.asar                Your JavaScript code (compressed)
│   │   ├── main.js
│   │   ├── index.html
│   │   └── package.json
│   └── backend                 Python executable
├── locales/                    Electron localization
├── chrome_100_percent.pak      Chromium resources
└── ... (other Electron files)
