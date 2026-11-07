#!/usr/bin/env python3
"""
Extract and optimize RAW (borderless/frameless) app screenshots specifically for the Hero Phone mockup.
Prevents "frame-in-frame" / double-border artifacts.
"""

import os
import glob
from PIL import Image

BASE_DIR = '/Users/louisliu/Documents/repo/liuys_website'

LOCALE_MAP = {
    'zh-tw': ['zh-Hant', 'zh-TW', 'zh'],
    'de': ['de-DE', 'de'],
    'fr': ['fr-FR', 'fr'],
    'ja': ['ja-JP', 'ja'],
    'ko': ['ko-KR', 'ko'],
    'es': ['es-ES', 'es'],
    'it': ['it-IT', 'it'],
}

def optimize_raw_hero(src_path, dest_path, target_width=540, quality=88):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    try:
        with Image.open(src_path) as img:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                img = img.convert('RGBA')
            else:
                img = img.convert('RGB')
            w, h = img.size
            if w > target_width:
                new_h = int(h * (target_width / float(w)))
                img = img.resize((target_width, new_h), Image.Resampling.LANCZOS)
            img.save(dest_path, 'WEBP', quality=quality, method=4)
            print(f"  [RAW HERO OK] {dest_path} ({img.size})")
    except Exception as e:
        print(f"  [RAW HERO ERR] {src_path} -> {dest_path}: {e}")

def process_alcohol_free_tracker():
    print("=== Processing Alcohol Free Tracker Raw Hero Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/Alcohol Free Tracker/Media/screenshots/raw'
    dest_base = os.path.join(BASE_DIR, 'alcohol-free-tracker/assets/screenshots_localized')
    
    for web_loc, cands in LOCALE_MAP.items():
        src_file = None
        for cand in cands:
            p = os.path.join(src_base, cand, 'iPhone 17 Pro Max-01Today.png')
            if os.path.isfile(p):
                src_file = p
                break
        if src_file:
            dest_file = os.path.join(dest_base, web_loc, 'hero-today-raw.webp')
            optimize_raw_hero(src_file, dest_file, target_width=540)
        else:
            print(f"  Warning: No raw 01Today found for {web_loc}")

def process_quit_vaping():
    print("=== Processing Quit Vaping Raw Hero Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/QuitSmokingTracker/fastlane/screenshots'
    dest_base = os.path.join(BASE_DIR, 'quit-vaping/assets/screenshots_localized')
    
    for web_loc, cands in LOCALE_MAP.items():
        src_file = None
        for cand in cands:
            p = os.path.join(src_base, cand, 'iPhone 17 Pro Max-01Hero.png')
            if os.path.isfile(p):
                src_file = p
                break
        if src_file:
            dest_file = os.path.join(dest_base, web_loc, 'hero-today-recovery-raw.webp')
            optimize_raw_hero(src_file, dest_file, target_width=720)
        else:
            print(f"  Warning: No raw 01Hero found for {web_loc}")

def process_pill_reminder():
    print("=== Processing Pill Reminder Raw Hero Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/Pill Reminder/screenshots/raw/20260804'
    dest_base = os.path.join(BASE_DIR, 'pill-reminder/assets/screenshots_localized')
    
    # 20260804 uses ISO folder names like zh-Hant, ja-JP (or ja), etc.
    pill_cands = {
        'zh-tw': ['zh-Hant', 'zh'],
        'de': ['de-DE', 'de'],
        'fr': ['fr-FR', 'fr'],
        'ja': ['ja-JP', 'ja'],
        'ko': ['ko-KR', 'ko'],
        'es': ['es-ES', 'es'],
        'it': ['it-IT', 'it'],
    }
    
    for web_loc, cands in pill_cands.items():
        src_file = None
        for cand in cands:
            p = os.path.join(src_base, cand, 'iPhone 17 Pro Max-01HomeScreen_WeekView.png')
            if os.path.isfile(p):
                src_file = p
                break
        if not src_file:
            # fallback to 20260729
            for cand in cands:
                p2 = os.path.join('/Users/louisliu/Documents/repo/Pill Reminder/screenshots/framed/20260729', cand, 'iPhone 17 Pro Max-01HomeScreen_WeekView.png')
                if os.path.isfile(p2):
                    src_file = p2
                    break
        if src_file:
            dest_file = os.path.join(dest_base, web_loc, 'hero-home-raw.webp')
            optimize_raw_hero(src_file, dest_file, target_width=540)
        else:
            print(f"  Warning: No raw HomeScreen found for {web_loc}")

def process_quit_weed():
    print("=== Processing Quit Weed Raw Hero Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/QuitWeedTracker/fastlane/screenshots'
    dest_base = os.path.join(BASE_DIR, 'quit-weed/assets/screenshots_localized')
    
    for web_loc, cands in LOCALE_MAP.items():
        src_file = None
        for cand in cands:
            p = os.path.join(src_base, cand, 'iPhone 17 Pro Max-01Hero.png')
            if os.path.isfile(p):
                src_file = p
                break
        if src_file:
            dest_file = os.path.join(dest_base, web_loc, 'hero-today-recovery-raw.webp')
            optimize_raw_hero(src_file, dest_file, target_width=720)

if __name__ == '__main__':
    process_alcohol_free_tracker()
    process_quit_vaping()
    process_pill_reminder()
    process_quit_weed()
    print("=== RAW Hero Screenshots Sync Done ===")
