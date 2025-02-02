# Advanced URL Scanner

## Description
This is an advanced URL scanner built using Python and Tkinter. It analyzes URLs for known malicious content by checking their hash signatures and providing alerts. The application allows users to check URLs, store scan results, and review previous scans.

## Features
- Fetches URL content and calculates MD5 hash.
- Compares hash against a list of known malicious signatures.
- Displays real-time scan results with visual indicators.
- Stores scan history in a text file.
- Allows users to review previous scans.
- User-friendly GUI with dark mode.

## Technologies Used
- Python
- Tkinter (for GUI)
- Requests (for fetching URLs)
- Hashlib (for hashing URL content)
- PIL (for handling images in GUI)
- Datetime (for logging scan time)

## Installation
1. Install Python (3.x recommended) if not already installed.
2. Install the required dependencies using pip:
   ```sh
   pip install requests pillow
   ```
3. Run the script:
   ```sh
   python url_scanner.py
   ```

## How to Use
1. Run the script to launch the application.
2. Enter a URL in the input field.
3. Click on **"فحص URL"** (Scan URL) to analyze the link.
4. If a suspicious signature is detected, an alert will appear.
5. Click on **"النتائج السابقة"** (Previous Results) to view scan history.
6. Click **"مسح النتائج"** (Clear Results) to clear the display.

## Files and Structure
```
url_scanner.py        # Main application file
scan_results.txt      # Log file for stored scan results
image/logo.png        # Logo for GUI
image/safe_icon.png   # Icon for safe URLs
image/danger_icon.png # Icon for malicious URLs
README.md             # Documentation
```

## Future Enhancements
- Integrate with online virus databases for real-time threat detection.
- Add multi-hash comparison (SHA-256, SHA-1) for better security.
- Improve visualization with dynamic threat reports.

## Disclaimer
This application is for educational and security monitoring purposes only. It should not be used for unauthorized URL analysis.

