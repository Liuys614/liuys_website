#!/usr/bin/env python3
"""
Checks App Store Connect review status for T-Break & Quit Weed: Unfog (App ID: 6825549617).
Prints JSON summary with current appStoreState and whether it is ready for a new version / screenshot update.
"""
import json
import time
import urllib.request
import jwt

KEY_PATH = "/Users/louisliu/Documents/Key/AuthKey_42D88P78B4.p8"
ISSUER_ID = "5cf6d376-5011-419f-90ca-0906cbc2913f"
KEY_ID = "42D88P78B4"
APP_ID = "6825549617"


def main():
    with open(KEY_PATH, "r", encoding="utf-8") as f:
        private_key = f.read()

    now = int(time.time())
    token = jwt.encode(
        {
            "iss": ISSUER_ID,
            "iat": now,
            "exp": now + 1200,
            "aud": "appstoreconnect-v1",
        },
        private_key,
        algorithm="ES256",
        headers={"kid": KEY_ID},
    )

    url = f"https://api.appstoreconnect.apple.com/v1/apps/{APP_ID}/appStoreVersions?limit=5"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    versions = []
    for v in data.get("data", []):
        attrs = v.get("attributes", {})
        state = attrs.get("appStoreState", "")
        versions.append({
            "id": v.get("id"),
            "versionString": attrs.get("versionString"),
            "appStoreState": state,
            "createdDate": attrs.get("createdDate"),
            "approved_or_live": state in ("READY_FOR_SALE", "PENDING_DEVELOPER_RELEASE", "PROCESSING_FOR_APP_STORE"),
            "rejected_or_action_needed": state in ("REJECTED", "METADATA_REJECTED", "DEVELOPER_REJECTED", "INVALID_BINARY"),
        })

    print(json.dumps({"app_id": APP_ID, "app_name": "T-Break & Quit Weed: Unfog", "versions": versions}, indent=2))


if __name__ == "__main__":
    main()
