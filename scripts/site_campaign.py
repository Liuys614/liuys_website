"""Shared App Store campaign settings for YS Liu Studio.

Change provider tokens here. Guide builders import this module, so the next
pipeline run keeps the same pt. Grocery Price landing pages and in-page tools
are static HTML and use GROCERY_LANDING_PROVIDER_TOKEN (pt=127596623). Every
other App Store link that already carries a pt uses DEFAULT_PROVIDER_TOKEN
(pt=1793695638), including grocery guide pages. Leave both values as they are
until the provider token is confirmed.

Static landing pages duplicate these pt values in HTML. After changing a token
here, update those pages (or re-run scripts/apply_unfog_release.py for Unfog)
so the HTML matches.
"""

import re

# Apple campaign token (ct) max length.
CT_MAX = 40

# Most apps, including grocery guide pages.
DEFAULT_PROVIDER_TOKEN = "1793695638"

# Grocery Price landing page and /grocery-price/tools/ pages only.
GROCERY_LANDING_PROVIDER_TOKEN = "127596623"

# Quit Weed / Unfog is not on the App Store yet. Its product URL 404s.
# Flip to True once app id 6825549617 is live, then run:
#   python3 scripts/apply_unfog_release.py
# and python3 quit-weed/scripts/build_guide.py
# The duplicate /quit-weed-tracker/ path is a symlink to /quit-weed/.
UNFOG_APP_ID = "6825549617"
UNFOG_RELEASED = False

HOME_CT = "site-home"

CF_BEACON = (
    "<script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
    "data-cf-beacon='{\"token\": \"5f06b65322f34626b2e5688ab29fd1df\"}'></script>"
)

PRIVACY_ANALYTICS_SENTENCE = (
    "This site uses Cloudflare Web Analytics, which is cookieless and collects aggregate traffic data."
)


def clean_ct(ct: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]", "-", ct.strip())
    return cleaned[:CT_MAX]


def guide_ct(slug: str) -> str:
    """Campaign token for a guide article: ct=seo-<page-slug>."""
    return clean_ct(f"seo-{slug}")


def guides_index_ct(app_slug: str) -> str:
    """Campaign token for an app's guide index."""
    return clean_ct(f"seo-{app_slug}-guides")


def landing_ct(app_slug: str) -> str:
    """Campaign token for an app landing page: ct=site-<app>-landing."""
    return clean_ct(f"site-{app_slug}-landing")


def app_is_released(app_id: str) -> bool:
    if str(app_id) == UNFOG_APP_ID:
        return UNFOG_RELEASED
    return True


def make_asc_url(app_id: str, pt: str, ct: str) -> str:
    return (
        f"https://apps.apple.com/app/apple-store/id{app_id}"
        f"?pt={pt}&ct={clean_ct(ct)}&mt=8"
    )


def smart_banner_tag(app_id: str) -> str:
    return f'<meta name="apple-itunes-app" content="app-id={app_id}" />'


def coming_soon_markup(class_name: str = "") -> str:
    classes = f"{class_name} is-coming-soon".strip()
    class_attr = f' class="{classes}"' if classes else ""
    return (
        f'<span{class_attr} role="text" aria-disabled="true">'
        "Coming soon to the App Store</span>"
    )


def store_cta(app_id: str, pt: str, ct: str, class_name: str, inner_html: str, extra_attrs: str = "") -> str:
    """App Store anchor, or a non-link coming-soon state when the app is unreleased."""
    if not app_is_released(app_id):
        return coming_soon_markup(class_name)
    attrs = f" {extra_attrs.strip()}" if extra_attrs.strip() else ""
    url = make_asc_url(app_id, pt, ct)
    return (
        f'<a href="{url}" class="{class_name}"{attrs} target="_blank" rel="noopener">'
        f"{inner_html}</a>"
    )
