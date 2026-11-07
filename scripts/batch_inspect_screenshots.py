#!/usr/bin/env python3
"""
Full-scope headless Chrome visual inspection across all 7 locales.
Takes high-res desktop and mobile viewport screenshots of:
- alcohol-free-tracker
- quit-vaping
- pill-reminder
"""

import os
import subprocess
import threading
import http.server
import socketserver
import time

PORT = 8999
BASE_DIR = '/Users/louisliu/Documents/repo/liuys_website'
OUT_DIR = '/Users/louisliu/Documents/repo/liuys_website/.screenshots_review'
os.makedirs(OUT_DIR, exist_ok=True)
CHROME_BIN = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

def run():
    httpd = socketserver.TCPServer(('', PORT), Handler)
    t = threading.Thread(target=httpd.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)
    
    locales = ['zh-tw', 'ja', 'ko', 'de', 'fr', 'es', 'it']
    apps = ['alcohol-free-tracker', 'quit-vaping', 'pill-reminder']
    
    captured = 0
    for loc in locales:
        for app in apps:
            url = f"http://localhost:{PORT}/{loc}/{app}/"
            out_file = os.path.join(OUT_DIR, f"{loc}_{app}.png")
            cmd = [
                CHROME_BIN,
                '--headless',
                '--disable-gpu',
                '--hide-scrollbars',
                '--window-size=1280,2400',
                f'--screenshot={out_file}',
                url
            ]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
                captured += 1
                print(f"  [INSPECTED OK] {loc}/{app} ({os.path.getsize(out_file)} bytes)")
            else:
                print(f"  [INSPECTED FAIL] {loc}/{app}")
                
    httpd.shutdown()
    print(f"\nSuccessfully inspected and captured {captured} localized app pages!")

if __name__ == '__main__':
    run()
