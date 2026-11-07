/**
 * YS Liu Studio — Universal Multi-Language Switcher Controller & Link Locale Persistence
 */
(function () {
  const SUPPORTED_LOCALES = ["zh-tw", "de", "fr", "ja", "ko", "es", "it"];

  function getCurrentLocale() {
    const match = window.location.pathname.match(/^\/(zh-tw|de|fr|ja|ko|es|it)(\/|$)/);
    return match ? match[1] : null;
  }

  function rewriteInternalLinks(locale) {
    if (!locale) return;
    const links = document.querySelectorAll("a[href]");
    links.forEach((a) => {
      const href = a.getAttribute("href");
      if (!href) return;
      if (href.startsWith("http://") || href.startsWith("https://") || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) {
        return;
      }
      // If link is a lang-switcher option, do not rewrite
      if (a.classList.contains("lang-opt")) return;

      // Handle root or relative home links
      if (href === "/" || href === "/index.html" || href === "index.html" || href === "../" || href === "../../") {
        a.setAttribute("href", `/${locale}/`);
        return;
      }

      // Handle absolute app paths like /quit-vaping/ or /alcohol-free-tracker/
      if (href.startsWith("/")) {
        const clean = href.replace(/^\/+/, "");
        const firstSegment = clean.split("/")[0];
        if (!SUPPORTED_LOCALES.includes(firstSegment)) {
          a.setAttribute("href", `/${locale}/${clean}`);
        }
      }
    });
  }

  function initLangSwitcher() {
    const currentLocale = getCurrentLocale();
    if (currentLocale) {
      try {
        localStorage.setItem("user_locale", currentLocale);
      } catch (e) {}
    }

    const switchers = document.querySelectorAll(".lang-switcher");
    if (switchers.length) {
      switchers.forEach((switcher) => {
        const btn = switcher.querySelector(".lang-btn");
        if (!btn) return;

        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          const isOpen = switcher.classList.contains("is-open");
          switchers.forEach((s) => s.classList.remove("is-open"));
          if (!isOpen) {
            switcher.classList.add("is-open");
            btn.setAttribute("aria-expanded", "true");
          } else {
            switcher.classList.remove("is-open");
            btn.setAttribute("aria-expanded", "false");
          }
        });
      });

      document.addEventListener("click", (e) => {
        switchers.forEach((switcher) => {
          if (!switcher.contains(e.target)) {
            switcher.classList.remove("is-open");
            const btn = switcher.querySelector(".lang-btn");
            if (btn) btn.setAttribute("aria-expanded", "false");
          }
        });
      });

      document.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
          switchers.forEach((switcher) => {
            switcher.classList.remove("is-open");
            const btn = switcher.querySelector(".lang-btn");
            if (btn) btn.setAttribute("aria-expanded", "false");
          });
        }
      });
    }

    // Rewrite links to persist current locale across page navigation
    if (currentLocale) {
      rewriteInternalLinks(currentLocale);

      // Intercept clicks on internal links as a fallback guard
      document.addEventListener("click", (e) => {
        const anchor = e.target.closest("a[href]");
        if (!anchor) return;
        if (anchor.classList.contains("lang-opt")) return;

        const href = anchor.getAttribute("href");
        if (!href || href.startsWith("http://") || href.startsWith("https://") || href.startsWith("#") || href.startsWith("mailto:") || href.startsWith("tel:")) {
          return;
        }

        if (href.startsWith("/")) {
          const clean = href.replace(/^\/+/, "");
          const firstSegment = clean.split("/")[0];
          if (!SUPPORTED_LOCALES.includes(firstSegment)) {
            e.preventDefault();
            window.location.href = `/${currentLocale}/${clean}`;
          }
        }
      }, true);

      // Re-run rewriter when DOM changes dynamically (e.g. app.js timeline render)
      const observer = new MutationObserver(() => {
        rewriteInternalLinks(currentLocale);
      });
      observer.observe(document.body, { childList: true, subtree: true });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initLangSwitcher);
  } else {
    initLangSwitcher();
  }
})();
