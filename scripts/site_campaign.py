"""Shared App Store campaign settings for YS Liu Studio.

Change the provider token here. Guide builders import this module, so the next
pipeline run keeps the same pt. Apple's campaign-link format is:

    https://apps.apple.com/app/apple-store/id<APPID>?pt=<PROVIDER_TOKEN>&ct=<campaign>&mt=8

PROVIDER_TOKEN is the App Store Connect provider token (127596623), confirmed
in App Store Connect's campaign link generator. 1793695638 is the developer
(artist) id used only on apps.apple.com/developer/... links, not a pt value.

Static landing pages and alcohol-free-tracker/script.js plus quit-vaping/script.js
duplicate this token. After changing it here, update those copies (or re-run
scripts/apply_unfog_release.py for Unfog) so the HTML matches.
"""

from __future__ import annotations

import re

# Apple campaign token (ct) max length.
CT_MAX = 40

# App Store Connect provider token. Not the developer/artist id.
PROVIDER_TOKEN = "127596623"

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


# ---------------------------------------------------------------------------
# Campaign token (ct) standard — adopted 2026-11-16
#
#   <surface>_<lang>[_<page>]_<pos>      lowercase, underscores, <= 40 chars
#
#   surface: g (guide) · gh (guide hub) · lp (app landing) · home (studio home) · tool (calculator)
#            sb (smart app banner) · sup (support / legal pages)
#   lang:    en ja de fr es it ko zhtw
#   page:    short guide slug (<= 20 chars), guides only
#   pos:     nav · hero · card · inline · side · sticky · foot
#
# The app itself is implied: ASC reports campaigns per app id.
# Examples: g_en_hydration_calculator_card · lp_ja_hero · sb_en_g_hydration_calculator
# ---------------------------------------------------------------------------

SLUG_STOPWORDS = {
    "a", "an", "and", "are", "can", "complete", "do", "does", "for", "from", "guide",
    "how", "i", "in", "is", "it", "of", "on", "or", "the", "to", "what", "when",
    "why", "with", "you", "your",
}
PAGE_MAX = 20


def lang_code(locale: str = "en") -> str:
    return re.sub(r"[^a-z]", "", (locale or "en").lower()) or "en"


def short_slug(slug: str, max_len: int = PAGE_MAX) -> str:
    """'sourdough-hydration-calculator-percentage-guide' -> 'sourdough_hydration'."""
    words = [w for w in re.split(r"[^a-z0-9]+", slug.lower()) if w]
    kept = [w for w in words if w not in SLUG_STOPWORDS] or words
    out = ""
    for w in kept:
        cand = f"{out}_{w}" if out else w
        if len(cand) > max_len:
            break
        out = cand
    return out or kept[0][:max_len]


def build_ct(surface: str, lang: str = "en", page: str = "", pos: str = "") -> str:
    parts = [surface, lang_code(lang), page, pos]
    return clean_ct("_".join(p for p in parts if p).lower())


def guide_ct(slug: str, pos: str = "card", lang: str = "en") -> str:
    """Guide article button/link: g_<lang>_<short-slug>_<pos>."""
    return build_ct("g", lang, short_slug(slug), pos)


def guides_index_ct(app_slug: str = "", pos: str = "nav", lang: str = "en") -> str:
    """Guide hub page: gh_<lang>_<pos>. app_slug kept for backwards-compatible calls."""
    return build_ct("gh", lang, "", pos)


def landing_ct(app_slug: str = "", pos: str = "hero", lang: str = "en") -> str:
    """App landing page: lp_<lang>_<pos>. app_slug kept for backwards-compatible calls."""
    return build_ct("lp", lang, "", pos)


def home_ct(pos: str = "card", lang: str = "en") -> str:
    return build_ct("home", lang, "", pos)


def banner_ct(page_kind: str, slug: str = "", lang: str = "en") -> str:
    """Smart App Banner: sb_<lang>_<g|gh|lp|home>[_<short-slug>]."""
    page = f"{page_kind}_{short_slug(slug)}" if slug else page_kind
    return build_ct("sb", lang, page, "")


_ASC_CT_RE = re.compile(r"(apps\.apple\.com/app/[^\"'\s<>]*?[?&](?:amp;)?ct=)([A-Za-z0-9_\-%.]+)")


def normalize_body_ct(body_html: str, slug: str, lang: str = "en") -> str:
    """Rewrite App Store links written inside post body_html to the standard.

    Old tokens ending in _text become 'inline'; everything else is the pitch 'card'.
    """
    def repl(m: re.Match) -> str:
        old = m.group(2)
        pos = "inline" if old.endswith("_text") or old.endswith("_inline") else "card"
        return m.group(1) + guide_ct(slug, pos, lang)

    return _ASC_CT_RE.sub(repl, body_html)


def app_is_released(app_id: str) -> bool:
    if str(app_id) == UNFOG_APP_ID:
        return UNFOG_RELEASED
    return True


def make_asc_url(app_id: str, pt: str, ct: str) -> str:
    return (
        f"https://apps.apple.com/app/apple-store/id{app_id}"
        f"?pt={pt}&ct={clean_ct(ct)}&mt=8"
    )


def smart_banner_tag(app_id: str, ct: str = "", app_argument: str = "") -> str:
    """Safari Smart App Banner. With ct, installs from the banner show up as that ASC campaign."""
    content = f"app-id={app_id}"
    if ct:
        content += f", affiliate-data=pt={PROVIDER_TOKEN}&ct={clean_ct(ct)}"
    if app_argument:
        content += f", app-argument={app_argument}"
    return f'<meta name="apple-itunes-app" content="{content}" />'


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


# Per-app medical / YMYL disclaimers for health guide pages.
HEALTH_GUIDE_DISCLAIMERS = {
    "alcohol-free-tracker": (
        "This guide is for general information only and is not medical advice. "
        "It doesn't replace a qualified health professional. Alcohol withdrawal can be "
        "dangerous—seek medical help for severe shaking, seizures, confusion, or "
        "hallucinations. In an emergency, call your local emergency number."
    ),
    "quit-weed": (
        "This guide is for general information only and is not medical advice. "
        "It doesn't replace a doctor or other qualified health professional. "
        "If withdrawal or mental-health symptoms are severe, or you are unsure what to do, "
        "talk to a professional. In an emergency, call your local emergency number."
    ),
    "quit-vaping": (
        "This guide is for general information only and is not medical advice. "
        "It doesn't replace a doctor or other qualified health professional. "
        "Talk to a professional if nicotine withdrawal is severe, you are pregnant, "
        "or you also use other tobacco products. In an emergency, call your local emergency number."
    ),
    "pill-reminder": (
        "This guide is for general information only and is not medical advice. "
        "It doesn't replace a doctor, pharmacist, or your package leaflet. "
        "Follow your prescriber's instructions for timing and missed doses. "
        "If you have symptoms, are pregnant, or are unsure what to do, talk to a professional. "
        "In an emergency, call your local emergency number."
    ),
}


def medical_disclaimer_html(app_key: str, reviewed_date: str | None = None) -> str:
    """Return a guide-callout medical disclaimer for health apps, or empty string."""
    import html as _html

    body = HEALTH_GUIDE_DISCLAIMERS.get(app_key)
    if not body:
        return ""
    reviewed = ""
    if reviewed_date:
        reviewed = (
            f'<p class="guide-disclaimer-reviewed">'
            f"Last reviewed: {_html.escape(reviewed_date)}</p>"
        )
    return (
        f'<aside class="guide-callout guide-medical-disclaimer" role="note" '
        f'aria-label="Medical disclaimer">'
        f"<strong>Medical disclaimer</strong>"
        f"<p>{_html.escape(body)}</p>"
        f"{reviewed}"
        f"</aside>"
    )
