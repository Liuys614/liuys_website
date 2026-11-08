#!/usr/bin/env python3
"""
build_device_framed_mockups.py
Generates pixel-perfect iPhone 17 Pro Max mockups with authentic Apple Titanium outer frame,
Dynamic Island, speaker slit, and transparent alpha corners (zero jagged black artifacts).
Covers:
- Alcohol Free Tracker (Hero Today + Privacy Body Recovery)
- Quit Vaping (Hero Today Recovery)
- Pill Reminder (Hero Home)
- Quit Weed (Hero Today Recovery)
Across English + 7 Storefront Locales: zh-tw, de, fr, ja, ko, es, it
"""

import os
from PIL import Image, ImageDraw

BASE_DIR = '/Users/louisliu/Documents/repo/liuys_website'
APPLE_FRAME_PATH = '/Users/louisliu/.fastlane/frameit/latest/Apple iPhone 16 Pro Max Black Titanium.png'

LOCALE_MAP = {
    'zh-tw': ['zh-Hant', 'zh-TW', 'zh'],
    'de': ['de-DE', 'de'],
    'fr': ['fr-FR', 'fr'],
    'ja': ['ja-JP', 'ja'],
    'ko': ['ko-KR', 'ko'],
    'es': ['es-ES', 'es'],
    'it': ['it-IT', 'it'],
}

def frame_raw_screenshot(raw_img, dest_webp_path, target_width=720, quality=90):
    os.makedirs(os.path.dirname(dest_webp_path), exist_ok=True)
    try:
        frame = Image.open(APPLE_FRAME_PATH).convert('RGBA')
        frame_w, frame_h = frame.size # 1470, 3000

        raw = raw_img.convert('RGBA')
        if raw.size != (1320, 2868):
            raw = raw.resize((1320, 2868), Image.Resampling.LANCZOS)
        
        # Mask raw with rounded rectangle (corner radius 146px for iPhone 16/17 Pro Max)
        mask = Image.new('L', (1320, 2868), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0, 0, 1320, 2868], radius=146, fill=255)
        
        masked_raw = Image.new('RGBA', (1320, 2868), (0, 0, 0, 0))
        masked_raw.paste(raw, (0, 0), mask=mask)
        
        # Composite onto 1470x3000 canvas
        canvas = Image.new('RGBA', (frame_w, frame_h), (0, 0, 0, 0))
        # Screen offset is +75, +66
        canvas.paste(masked_raw, (75, 66), mask=masked_raw)
        # Overlay frame
        canvas.paste(frame, (0, 0), mask=frame)
        
        # Downsample to target width
        if canvas.width > target_width:
            target_height = int(frame_h * (target_width / float(frame_w)))
            canvas = canvas.resize((target_width, target_height), Image.Resampling.LANCZOS)
        
        canvas.save(dest_webp_path, 'WEBP', quality=quality, method=4)
        print(f"  [OK] Saved framed mockup: {dest_webp_path} ({canvas.size})")
    except Exception as e:
        print(f"  [ERR] Failed to frame -> {dest_webp_path}: {e}")

def build_alcohol_free_tracker():
    print("=== Building Alcohol Free Tracker Framed Mockups ===")
    raw_base = '/Users/louisliu/Documents/repo/Alcohol Free Tracker/Media/screenshots/raw'
    appstore_base = '/Users/louisliu/Documents/repo/Alcohol Free Tracker/Media/appstore_Screenshots/20260908'
    dest_base = os.path.join(BASE_DIR, 'alcohol-free-tracker/assets/screenshots_localized')
    
    # 1. English Hero
    en_raw = os.path.join(raw_base, 'en-US/iPhone 17 Pro Max-01Today.png')
    if os.path.isfile(en_raw):
        with Image.open(en_raw) as img:
            frame_raw_screenshot(img, os.path.join(BASE_DIR, 'alcohol-free-tracker/assets/screens/06-today-light.webp'))
    
    # 2. English Privacy (Body Recovery)
    en_appstore = os.path.join(appstore_base, 'en-US/iphone/1_APP_IPHONE_69_1.png')
    if os.path.isfile(en_appstore):
        with Image.open(en_appstore) as im:
            inner = im.crop((177, 142, 1143, 2242))
            frame_raw_screenshot(inner, os.path.join(BASE_DIR, 'alcohol-free-tracker/assets/screens/body-recovery-phone.webp'))
    
    # 3. Localized Hero and Privacy
    for web_loc, cands in LOCALE_MAP.items():
        # Hero
        hero_raw = None
        for cand in cands:
            p = os.path.join(raw_base, cand, 'iPhone 17 Pro Max-01Today.png')
            if os.path.isfile(p):
                hero_raw = p
                break
        if hero_raw:
            with Image.open(hero_raw) as img:
                frame_raw_screenshot(img, os.path.join(dest_base, web_loc, 'hero-today.webp'))
        
        # Privacy Body Recovery
        rec_card = None
        for cand in cands:
            p = os.path.join(appstore_base, cand, 'iphone/1_APP_IPHONE_69_1.png')
            if os.path.isfile(p):
                rec_card = p
                break
        if rec_card:
            with Image.open(rec_card) as im:
                inner = im.crop((177, 142, 1143, 2242))
                frame_raw_screenshot(inner, os.path.join(dest_base, web_loc, 'privacy-phone.webp'))

def build_quit_vaping():
    print("=== Building Quit Vaping Framed Mockups ===")
    raw_base = '/Users/louisliu/Documents/repo/QuitSmokingTracker/fastlane/screenshots'
    dest_base = os.path.join(BASE_DIR, 'quit-vaping/assets/screenshots_localized')
    
    # English Hero
    en_raw = os.path.join(raw_base, 'en-US/iPhone 17 Pro Max-01Hero.png')
    if os.path.isfile(en_raw):
        with Image.open(en_raw) as img:
            frame_raw_screenshot(img, os.path.join(BASE_DIR, 'quit-vaping/assets/screens/hero-today-recovery.webp'))
    
    for web_loc, cands in LOCALE_MAP.items():
        hero_raw = None
        for cand in cands:
            p = os.path.join(raw_base, cand, 'iPhone 17 Pro Max-01Hero.png')
            if os.path.isfile(p):
                hero_raw = p
                break
        if hero_raw:
            with Image.open(hero_raw) as img:
                frame_raw_screenshot(img, os.path.join(dest_base, web_loc, 'hero-today.webp'))

def build_pill_reminder():
    print("=== Building Pill Reminder Framed Mockups ===")
    raw_base = '/Users/louisliu/Documents/repo/Pill Reminder/screenshots/raw/20260804'
    dest_base = os.path.join(BASE_DIR, 'pill-reminder/assets/screenshots_localized')
    
    # English Hero
    en_raw = os.path.join(raw_base, 'en-US/iPhone 17 Pro Max-01HomeScreen_WeekView.png')
    if os.path.isfile(en_raw):
        with Image.open(en_raw) as img:
            frame_raw_screenshot(img, os.path.join(BASE_DIR, 'pill-reminder/assets/screens/hero-home.webp'))
        
    for web_loc, cands in LOCALE_MAP.items():
        hero_raw = None
        for cand in cands:
            p = os.path.join(raw_base, cand, 'iPhone 17 Pro Max-01HomeScreen_WeekView.png')
            if os.path.isfile(p):
                hero_raw = p
                break
        if hero_raw:
            with Image.open(hero_raw) as img:
                frame_raw_screenshot(img, os.path.join(dest_base, web_loc, 'hero-home.webp'))

def build_quit_weed():
    print("=== Building Quit Weed Framed Mockups ===")
    raw_base = '/Users/louisliu/Documents/repo/QuitWeedTracker/fastlane/screenshots'
    dest_base = os.path.join(BASE_DIR, 'quit-weed/assets/screenshots_localized')
    
    # English Hero
    en_raw = os.path.join(raw_base, 'en-US/iPhone 17 Pro Max-01Hero.png')
    if os.path.isfile(en_raw):
        with Image.open(en_raw) as img:
            frame_raw_screenshot(img, os.path.join(BASE_DIR, 'quit-weed/assets/screens/hero-today-recovery.webp'))
        
    for web_loc, cands in LOCALE_MAP.items():
        hero_raw = None
        for cand in cands:
            p = os.path.join(raw_base, cand, 'iPhone 17 Pro Max-01Hero.png')
            if os.path.isfile(p):
                hero_raw = p
                break
        if hero_raw:
            with Image.open(hero_raw) as img:
                frame_raw_screenshot(img, os.path.join(dest_base, web_loc, 'hero-today.webp'))

if __name__ == '__main__':
    build_alcohol_free_tracker()
    build_quit_vaping()
    build_pill_reminder()
    build_quit_weed()
