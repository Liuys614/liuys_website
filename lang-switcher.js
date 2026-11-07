/**
 * YS Liu Studio — Universal Multi-Language Switcher Controller
 */
(function () {
  function initLangSwitcher() {
    const switchers = document.querySelectorAll(".lang-switcher");
    if (!switchers.length) return;

    switchers.forEach((switcher) => {
      const btn = switcher.querySelector(".lang-btn");
      if (!btn) return;

      btn.addEventListener("click", (e) => {
        e.stopPropagation();
        const isOpen = switcher.classList.contains("is-open");
        // Close all others
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

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initLangSwitcher);
  } else {
    initLangSwitcher();
  }
})();
