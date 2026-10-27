#!/usr/bin/env python3
"""
Portfolio SEO Status & Pipeline Overview.
Inspects all 4 programmatic SEO app pipelines:
  - Alcohol Free Tracker (alcohol-free-tracker)
  - Quit Weed / Unfog (quit-weed)
  - Quit Vaping (quit-vaping)
  - Supplement & Pill Reminder (pill-reminder)
"""
import json
import os
import subprocess

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS = [
    ("alcohol-free-tracker", "Alcohol Free Tracker"),
    ("quit-weed", "Quit Weed: Unfog"),
    ("quit-vaping", "Quit Vaping"),
    ("pill-reminder", "Supplement & Pill Reminder"),
]


def inspect_app(app_dir_name: str, app_title: str):
    app_path = os.path.join(ROOT_DIR, app_dir_name)
    guides_dir = os.path.join(app_path, "guides")
    manifest_path = os.path.join(guides_dir, "published_manifest.json")
    queue_path = os.path.join(guides_dir, "topic_queue.json")

    published_count = 0
    if os.path.exists(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as f:
            published_count = len(json.load(f))

    pending_topics = []
    if os.path.exists(queue_path):
        with open(queue_path, "r", encoding="utf-8") as f:
            queue = json.load(f)
            pending_topics = [q for q in queue if q.get("status") != "published"]

    print(f"📦 {app_title} ({app_dir_name})")
    print(f"   • Published Guides: {published_count}")
    print(f"   • Queue Remaining:  {len(pending_topics)} pending topics")
    if pending_topics:
        next_topic = pending_topics[0]
        print(f"   • Next Candidate:   \"{next_topic['slug']}\"")
        print(f"     Target Keyword:   \"{next_topic['target_keyword']}\"")
    else:
        print(f"   • Next Candidate:   [Queue Exhausted - Needs New Topics]")
    print()


def main():
    print("=" * 64)
    print("   YS Liu Studio — Programmatic SEO Portfolio Dashboard")
    print("=" * 64)
    print()
    for app_dir, title in APPS:
        inspect_app(app_dir, title)
    print("=" * 64)


if __name__ == "__main__":
    main()
