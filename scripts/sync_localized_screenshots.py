#!/usr/bin/env python3
"""
Sync and optimize localized App Store screenshots from source repos into liuys_website.
Converts high-res PNGs to high-quality optimized WebP images for fast web delivery.
"""

import os
import glob
from PIL import Image

BASE_DIR = '/Users/louisliu/Documents/repo/liuys_website'

# Target locales on web -> source locale directory mapping per app
LOCALE_MAP_STANDARD = {
    'zh-tw': ['zh-Hant', 'zh-TW', 'zh'],
    'de': ['de-DE', 'de'],
    'fr': ['fr-FR', 'fr'],
    'ja': ['ja-JP', 'ja'],
    'ko': ['ko-KR', 'ko'],
    'es': ['es-ES', 'es'],
    'it': ['it-IT', 'it'],
}

def optimize_image(src_path, dest_path, max_width=900, quality=85):
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    if os.path.exists(dest_path) and os.path.getmtime(dest_path) >= os.path.getmtime(src_path):
        return
    try:
        with Image.open(src_path) as img:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                pass
            else:
                img = img.convert('RGB')
            w, h = img.size
            if w > max_width:
                new_h = int(h * (max_width / float(w)))
                img = img.resize((max_width, new_h), Image.Resampling.LANCZOS)
            img.save(dest_path, 'WEBP', quality=quality, method=4)
            print(f"  [OK] Saved: {dest_path}")
    except Exception as e:
        print(f"  [ERR] {src_path} -> {dest_path}: {e}")

def sync_quit_vaping():
    print("=== Syncing Quit Vaping Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/QuitSmokingTracker/fastlane/screenshots_framed'
    dest_base = os.path.join(BASE_DIR, 'quit-vaping/assets/screenshots_localized')
    
    file_mapping = [
        ('01-calm-progress.webp', ['*01Hero_framed*']),
        ('02-body-recovery.webp', ['*02BodyRecovery_framed*']),
        ('03-urge-surfing.webp', ['*03SOSBreathing_framed*']),
        ('04-savings.webp', ['*04Savings_framed*']),
        ('05-milestones.webp', ['*05Milestones_framed*']),
        ('06-calendar.webp', ['*06Calendar_framed*']),
        ('07-check-in.webp', ['*07CheckIn_framed*']),
        ('08-privacy.webp', ['*08Privacy_framed*']),
        ('09-dark-mode.webp', ['*09TodayDark_framed*']),
        ('10-streak.webp', ['*10LoggedStreak_framed*']),
        ('hero-today-recovery.webp', ['*01Hero_framed*']),
    ]
    
    for web_loc, candidates in LOCALE_MAP_STANDARD.items():
        loc_dir = None
        for cand in candidates:
            p = os.path.join(src_base, cand)
            if os.path.isdir(p):
                loc_dir = p
                break
        if not loc_dir:
            print(f"  Skipping {web_loc}: no source folder")
            continue
        
        for out_name, patterns in file_mapping:
            dest_file = os.path.join(dest_base, web_loc, out_name)
            found = False
            for pat in patterns:
                matches = glob.glob(os.path.join(loc_dir, pat))
                if matches:
                    optimize_image(matches[0], dest_file)
                    found = True
                    break
            if not found:
                print(f"  Warning: {out_name} not found in {loc_dir}")

def sync_alcohol_free_tracker():
    print("=== Syncing Alcohol Free Tracker Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/Alcohol Free Tracker/Media/screenshots/framed'
    dest_base = os.path.join(BASE_DIR, 'alcohol-free-tracker/assets/screenshots_localized')
    
    file_mapping = [
        ('01-calm-progress.webp', ['*iPhone*01Today_framed*']),
        ('02-body-recovery.webp', ['*iPhone*02Calendar_framed*']),
        ('03-urge-surfing.webp', ['*iPhone*03Milestones_framed*']),
        ('04-savings.webp', ['*iPhone*04Privacy_framed*', '*iPhone*04CheckIn_framed*']),
        ('05-calendar.webp', ['*iPhone*05CheckIn_framed*', '*iPhone*05TodayDark_framed*']),
        ('06-milestones.webp', ['*iPhone*06SavingsDark_framed*', '*iPhone*06TodayDark_framed*']),
        ('07-check-in.webp', ['*iPhone*07LoggedStreak_framed*', '*iPhone*07SavingsDark_framed*']),
        ('08-private.webp', ['*iPhone*08LoggedStreak_framed*', '*iPhone*08SoberClock_framed*']),
        ('09-dark-mode.webp', ['*iPhone*06TodayDark_framed*', '*iPhone*05TodayDark_framed*']),
        ('10-streak.webp', ['*iPhone*08LoggedStreak_framed*', '*iPhone*07LoggedStreak_framed*']),
        ('hero-today.webp', ['*iPhone*01Today_framed*']),
    ]
    
    for web_loc, candidates in LOCALE_MAP_STANDARD.items():
        loc_dir = None
        for cand in candidates:
            p = os.path.join(src_base, cand)
            if os.path.isdir(p):
                loc_dir = p
                break
        if not loc_dir:
            print(f"  Skipping {web_loc}: no source folder")
            continue
            
        for out_name, patterns in file_mapping:
            dest_file = os.path.join(dest_base, web_loc, out_name)
            for pat in patterns:
                matches = glob.glob(os.path.join(loc_dir, pat))
                if matches:
                    optimize_image(matches[0], dest_file)
                    break

def sync_pill_reminder():
    print("=== Syncing Pill Reminder Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/Pill Reminder/screenshots/appstore_v2'
    dest_base = os.path.join(BASE_DIR, 'pill-reminder/assets/screenshots_localized')
    
    file_indices = [
        ('01-never-miss-a-dose.webp', 0),
        ('02-missed-dose-alarm.webp', 1),
        ('03-flexible-schedules.webp', 2),
        ('04-medicine-details.webp', 3),
        ('05-one-tap-check-in.webp', 4),
        ('06-privacy-face-id.webp', 5),
        ('07-refill-alerts.webp', 6),
        ('08-export-data.webp', 7),
        ('hero-home.webp', 0),
    ]
    
    for web_loc, candidates in LOCALE_MAP_STANDARD.items():
        loc_dir = None
        for cand in candidates:
            p = os.path.join(src_base, cand, 'iphone')
            if os.path.isdir(p):
                loc_dir = p
                break
        if not loc_dir:
            # Fallback to framed 20260729 if needed
            for cand in candidates:
                p2 = os.path.join('/Users/louisliu/Documents/repo/Pill Reminder/screenshots/framed/20260729', cand)
                if os.path.isdir(p2):
                    loc_dir = p2
                    break
        if not loc_dir:
            print(f"  Skipping {web_loc}: no source folder")
            continue
            
        files = sorted(glob.glob(os.path.join(loc_dir, '*.png')))
        if not files:
            continue
        for out_name, idx in file_indices:
            if idx < len(files):
                dest_file = os.path.join(dest_base, web_loc, out_name)
                optimize_image(files[idx], dest_file)

def sync_levain():
    print("=== Syncing Levain Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/sourdoughTimer/appleStore/screenshots/framed'
    dest_base = os.path.join(BASE_DIR, 'levain/assets/screenshots_localized')
    
    shots = [
        ('shot-1.webp', '*00Timer*'),
        ('shot-2.webp', '*01Editor*'),
        ('shot-3.webp', '*02Activity*'),
        ('shot-4.webp', '*03Detail*'),
        ('shot-5.webp', '*04Calendar*'),
        ('shot-6.webp', '*05Picker*'),
    ]
    
    for web_loc, candidates in LOCALE_MAP_STANDARD.items():
        loc_dir = None
        for cand in candidates:
            p = os.path.join(src_base, cand)
            if os.path.isdir(p):
                loc_dir = p
                break
        if not loc_dir:
            continue
        for out_name, pat in shots:
            dest_file = os.path.join(dest_base, web_loc, out_name)
            matches = glob.glob(os.path.join(loc_dir, pat))
            if matches:
                optimize_image(matches[0], dest_file)

def sync_quit_weed():
    print("=== Syncing Quit Weed Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/QuitWeedTracker/fastlane/screenshots'
    dest_base = os.path.join(BASE_DIR, 'quit-weed/assets/screenshots_localized')
    
    file_mapping = [
        ('hero-today-recovery.webp', ['*iPhone*01Hero*']),
        ('01-hero.webp', ['*iPhone*01Hero*']),
        ('02-recovery.webp', ['*iPhone*02BodyRecovery*']),
        ('03-breathing.webp', ['*iPhone*03SOSBreathing*']),
        ('04-savings.webp', ['*iPhone*04Savings*']),
        ('05-milestones.webp', ['*iPhone*05Milestones*']),
        ('06-calendar.webp', ['*iPhone*06Calendar*']),
    ]
    
    for web_loc, candidates in LOCALE_MAP_STANDARD.items():
        loc_dir = None
        for cand in candidates:
            p = os.path.join(src_base, cand)
            if os.path.isdir(p):
                loc_dir = p
                break
        if not loc_dir:
            continue
        for out_name, patterns in file_mapping:
            dest_file = os.path.join(dest_base, web_loc, out_name)
            for pat in patterns:
                matches = glob.glob(os.path.join(loc_dir, pat))
                if matches:
                    optimize_image(matches[0], dest_file)
                    break

def sync_inkstone():
    print("=== Syncing Inkstone Screenshots ===")
    src_base = '/Users/louisliu/Documents/repo/inkstone/appleStore/screenshots/final/iphone-69'
    dest_base = os.path.join(BASE_DIR, 'inkstone/assets/screenshots_localized')
    
    for web_loc, candidates in LOCALE_MAP_STANDARD.items():
        loc_dir = None
        for cand in candidates:
            p = os.path.join(src_base, cand)
            if os.path.isdir(p):
                loc_dir = p
                break
        if not loc_dir:
            continue
        for num in ['01', '02', '03', '04', '05']:
            src_f = os.path.join(loc_dir, f"{num}.png")
            if os.path.exists(src_f):
                dest_file = os.path.join(dest_base, web_loc, f"{num}.webp")
                optimize_image(src_f, dest_file)

if __name__ == '__main__':
    sync_quit_vaping()
    sync_alcohol_free_tracker()
    sync_pill_reminder()
    sync_levain()
    sync_quit_weed()
    sync_inkstone()
    print("=== Done Syncing Localized Screenshots ===")
