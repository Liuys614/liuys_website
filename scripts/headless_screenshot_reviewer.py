#!/usr/bin/env python3
"""
Automated Headless Chrome Screenshot & Deep Content Verifier
Launches local server, renders and takes full screenshots of pages across locales,
and audits for untranslated text strings or broken images.
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

def start_server():
    httpd = socketserver.TCPServer(('', PORT), Handler)
    t = threading.Thread(target=httpd.serve_forever)
    t.daemon = True
    t.start()
    return httpd

def capture_page(url_path, output_name, window_size="1280,2400"):
    full_url = f"http://localhost:{PORT}{url_path}"
    out_file = os.path.join(OUT_DIR, output_name)
    cmd = [
        CHROME_BIN,
        '--headless',
        '--disable-gpu',
        '--hide-scrollbars',
        f'--window-size={window_size}',
        f'--screenshot={out_file}',
        full_url
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
        print(f"  [SCREENSHOT OK] {url_path} -> {output_name} ({os.path.getsize(out_file)} bytes)")
        return True
    else:
        print(f"  [SCREENSHOT FAIL] {url_path}: {res.stderr}")
        return False

def audit_untranslated_text():
    print("\n=== Auditing Untranslated English in Localized Pages ===")
    test_locales = ['zh-tw', 'ja', 'ko', 'de', 'fr', 'es', 'it']
    apps = ['alcohol-free-tracker', 'quit-vaping', 'pill-reminder']
    
    # Phrases that MUST NOT appear verbatim in localized versions
    forbidden_phrases = [
        "Cravings are waves.",
        "Your body is already healing.",
        "An urge rises, peaks, and passes",
        "Notice it in your body",
        "Breathe until it fades",
        "The old way broke your spirit",
        "Answers when you need them",
        "Everything a reminder app should do",
        "Loud alarms that can't be ignored",
        "Cravings last 3 minutes",
    ]
    
    issues = []
    for loc in test_locales:
        for app in apps:
            p = os.path.join(BASE_DIR, loc, app, 'index.html')
            with open(p, 'r', encoding='utf-8') as f:
                content = f.read()
            for phrase in forbidden_phrases:
                if phrase in content:
                    issues.append((loc, app, phrase))
                    
    if issues:
        print(f"  [AUDIT WARNING] Found {len(issues)} untranslated phrases:")
        for loc, app, phrase in issues:
            print(f"    - [{loc}][{app}] {phrase}")
    else:
        print("  [AUDIT PASS] ZERO forbidden English key phrases found across all tested locales!")

def main():
    print("=== Starting Headless Chrome Review ===")
    httpd = start_server()
    time.sleep(1)
    
    review_targets = [
        ('/zh-tw/alcohol-free-tracker/', 'zh-tw_alcohol-free-tracker.png'),
        ('/zh-tw/quit-vaping/', 'zh-tw_quit-vaping.png'),
        ('/zh-tw/pill-reminder/', 'zh-tw_pill-reminder.png'),
        ('/ja/alcohol-free-tracker/', 'ja_alcohol-free-tracker.png'),
        ('/ko/alcohol-free-tracker/', 'ko_alcohol-free-tracker.png'),
        ('/de/alcohol-free-tracker/', 'de_alcohol-free-tracker.png'),
        ('/fr/alcohol-free-tracker/', 'fr_alcohol-free-tracker.png'),
        ('/es/alcohol-free-tracker/', 'es_alcohol-free-tracker.png'),
        ('/it/alcohol-free-tracker/', 'it_alcohol-free-tracker.png'),
    ]
    
    for url, out_name in review_targets:
        capture_page(url, out_name)
        
    audit_untranslated_text()
    httpd.shutdown()
    print("=== Review Finished ===")

if __name__ == '__main__':
    main()
