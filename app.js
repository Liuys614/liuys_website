import { PROFILE, APPS } from "./apps-data.js";

// ============================================================================
// State Management
// ============================================================================
let currentLightboxApp = null;
let currentLightboxIndex = 0;

// ============================================================================
// DOM Elements
// ============================================================================
const timelineStreamEl = document.getElementById("timelineStream");
const projectsListEl = document.getElementById("projectsList");

// Lightbox Elements
const lightboxEl = document.getElementById("lightbox");
const lightboxBackdropEl = document.getElementById("lightboxBackdrop");
const lightboxAppTitleEl = document.getElementById("lightboxAppTitle");
const lightboxCounterEl = document.getElementById("lightboxCounter");
const lightboxImgEl = document.getElementById("lightboxImg");
const lightboxBtnCloseEl = document.getElementById("lightboxBtnClose");
const lightboxPrevEl = document.getElementById("lightboxPrev");
const lightboxNextEl = document.getElementById("lightboxNext");

// Toast & Copy Elements
const toastEl = document.getElementById("toastNotification");
const toastMessageEl = document.getElementById("toastMessage");
const btnCopyEmail = document.getElementById("btnCopyEmail");
const copyEmailLabel = document.getElementById("copyEmailLabel");

// ============================================================================
// SVG Assets
// ============================================================================
const ICONS = {
  check: `<svg viewBox="0 0 20 20" fill="currentColor" class="bullet-icon"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg>`,
  featureCheck: `<svg viewBox="0 0 20 20" fill="currentColor" class="feature-check-icon"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg>`,
  apple: `<svg viewBox="0 0 170 170" fill="currentColor"><path d="M150.37 130.25c-2.45 5.66-5.35 10.87-8.71 15.66-4.58 6.53-8.33 11.05-11.22 13.56-4.48 4.12-9.28 6.23-14.42 6.35-3.69 0-8.14-1.05-13.32-3.18-5.19-2.12-9.97-3.17-14.34-3.17-4.58 0-9.49 1.05-14.75 3.17-5.26 2.13-9.5 3.24-12.74 3.35-4.35.13-9.16-1.9-14.42-6.08-3.7-3.04-7.6-7.77-11.71-14.19-5.78-9.02-10.3-19.34-13.57-30.95-3.26-11.61-4.9-22.75-4.9-33.42 0-14.65 3.7-26.65 11.09-36 7.4-9.35 16.63-14.11 27.69-14.28 5.34 0 11.2 1.34 17.58 4.02 6.38 2.68 10.4 4.07 12.06 4.17 2.05 0 6.39-1.48 13.01-4.44 6.63-2.96 12.19-4.27 16.7-3.92 12.38.83 22.35 5.48 29.9 13.97-10.88 6.59-16.2 15.69-15.96 27.32.25 9.17 3.77 16.96 10.58 23.36 6.8 6.4 14.88 10.02 24.23 10.85-2.22 6.64-4.8 12.96-7.75 18.96zM119.22 31.84c0-7.39 2.67-14.23 8.01-20.52 5.34-6.29 11.89-10.28 19.66-11.97.74 7.73-1.68 14.76-7.25 21.08-5.57 6.32-12.37 10.12-20.42 11.41z"/></svg>`,
  externalLink: `<svg viewBox="0 0 20 20" fill="currentColor" style="width: 14px; height: 14px;"><path fill-rule="evenodd" d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z" clip-rule="evenodd" /></svg>`,
  zoom: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>`,
  arrowLeft: `<svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clip-rule="evenodd" /></svg>`,
  arrowRight: `<svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" /></svg>`
};

// ============================================================================
// Render Functions
// ============================================================================

/**
 * Render Chronological Timeline (Experience & Education in unified order)
 */
function renderTimeline() {
  if (!timelineStreamEl || !PROFILE.timeline) return;

  timelineStreamEl.innerHTML = PROFILE.timeline.map(item => {
    const isWork = item.type === "work";
    const typeLabel = isWork ? "Work Experience" : "Education";
    const typeClass = isWork ? "type-work" : "type-education";

    return `
      <article class="timeline-card" data-type="${item.type}">
        <span class="timeline-node-marker" aria-hidden="true"></span>
        
        <div class="timeline-card-header">
          <span class="timeline-period-badge">${item.period}</span>
          <span class="timeline-type-pill ${typeClass}">${typeLabel}</span>
        </div>

        <h3 class="timeline-role-title">${item.role}</h3>
        <div class="timeline-org-name">${item.organization} ${item.location ? `· ${item.location}` : ""}</div>

        <ul class="timeline-bullets">
          ${item.highlights.map(h => `
            <li class="timeline-bullet">
              ${ICONS.check}
              <span>${h}</span>
            </li>
          `).join("")}
        </ul>
      </article>
    `;
  }).join("");
}

/**
 * Render 5 App Project Showcase Rows
 */
function renderProjects() {
  if (!projectsListEl || !APPS) return;

  projectsListEl.innerHTML = APPS.map((app, appIdx) => {
    const screenshotCount = app.screenshots ? app.screenshots.length : 0;

    return `
      <article class="project-card" id="project-${app.id}">
        <!-- Left Meta Column -->
        <div class="project-left">
          <div class="project-meta-header">
            <img src="${app.icon}" alt="${app.title} Icon" class="project-app-icon" loading="lazy" />
            <div>
              <div class="project-badges-row">
                <span class="category-tag">${app.category}</span>
              </div>
              <h3 class="project-title">${app.title}</h3>
            </div>
          </div>

          <div class="project-tagline">${app.tagline}</div>
          <p class="project-desc">${app.description}</p>

          <ul class="project-features">
            ${app.features.map(f => `
              <li class="feature-bullet">
                ${ICONS.featureCheck}
                <span>${f}</span>
              </li>
            `).join("")}
          </ul>

          <div class="project-actions">
            ${app.links.map(link => {
              if (link.type === "appstore") {
                return `
                  <a href="${link.url}" target="_blank" rel="noopener noreferrer" class="btn-appstore-link">
                    ${ICONS.apple}
                    <span>Download on App Store</span>
                  </a>
                `;
              } else {
                return `
                  <a href="${link.url}" target="_blank" rel="noopener noreferrer" class="btn-site-link">
                    <span>${link.label}</span>
                    ${ICONS.externalLink}
                  </a>
                `;
              }
            }).join("")}
          </div>
        </div>

        <!-- Right Gallery Column -->
        <div class="project-right">
          <div class="gallery-header">
            <div class="gallery-controls">
              <button type="button" class="gallery-nav-btn btn-track-left" data-target="track-${app.id}" aria-label="Scroll left">
                ${ICONS.arrowLeft}
              </button>
              <button type="button" class="gallery-nav-btn btn-track-right" data-target="track-${app.id}" aria-label="Scroll right">
                ${ICONS.arrowRight}
              </button>
            </div>
          </div>

          <div class="project-screenshots-track" id="track-${app.id}">
            ${app.screenshots.map((s, sIdx) => `
              <div class="screenshot-tile" data-app-index="${appIdx}" data-screenshot-index="${sIdx}">
                <img 
                  src="${s.thumb}" 
                  alt="${s.alt}" 
                  class="tile-img" 
                  loading="lazy" 
                  onerror="this.onerror=null; this.src='${app.icon}'" 
                />
                <div class="tile-hover-cue">
                  <span class="inspect-pill">
                    ${ICONS.zoom}
                    <span>Inspect</span>
                  </span>
                </div>
              </div>
            `).join("")}
          </div>
        </div>
      </article>
    `;
  }).join("");

  attachGalleryControls();
}

/**
 * Attach Event Handlers for Carousel Tracks, Mouse Scrolling & Lightbox
 */
function attachGalleryControls() {
  // Arrow Button Navigation
  document.querySelectorAll(".btn-track-left").forEach(btn => {
    btn.addEventListener("click", () => {
      const trackId = btn.getAttribute("data-target");
      const track = document.getElementById(trackId);
      if (track) track.scrollBy({ left: -360, behavior: "smooth" });
    });
  });

  document.querySelectorAll(".btn-track-right").forEach(btn => {
    btn.addEventListener("click", () => {
      const trackId = btn.getAttribute("data-target");
      const track = document.getElementById(trackId);
      if (track) track.scrollBy({ left: 360, behavior: "smooth" });
    });
  });

  // Track Drag Scrolling (Horizontal wheel is handled natively by the browser)
  document.querySelectorAll(".project-screenshots-track").forEach(track => {
    // Mouse Click & Drag Scrolling
    let isDown = false;
    let startX = 0;
    let scrollLeft = 0;
    let hasDragged = false;

    track.addEventListener("mousedown", (e) => {
      isDown = true;
      hasDragged = false;
      track.classList.add("dragging");
      startX = e.pageX - track.offsetLeft;
      scrollLeft = track.scrollLeft;
    });

    track.addEventListener("mouseleave", () => {
      isDown = false;
      track.classList.remove("dragging");
    });

    track.addEventListener("mouseup", () => {
      isDown = false;
      track.classList.remove("dragging");
    });

    track.addEventListener("mousemove", (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - track.offsetLeft;
      const walk = (x - startX) * 1.5;
      if (Math.abs(walk) > 5) {
        hasDragged = true;
      }
      track.scrollLeft = scrollLeft - walk;
    });

    // Prevent lightbox opening if user was dragging
    track.querySelectorAll(".screenshot-tile").forEach(tile => {
      tile.addEventListener("click", (e) => {
        if (hasDragged) {
          e.stopPropagation();
          hasDragged = false;
          return;
        }
        const appIndex = parseInt(tile.getAttribute("data-app-index"), 10);
        const screenshotIndex = parseInt(tile.getAttribute("data-screenshot-index"), 10);
        openLightbox(appIndex, screenshotIndex);
      });
    });
  });
}

// ============================================================================
// Lightbox Implementation
// ============================================================================

function openLightbox(appIndex, screenshotIndex) {
  currentLightboxApp = APPS[appIndex];
  if (!currentLightboxApp || !currentLightboxApp.screenshots.length) return;

  currentLightboxIndex = screenshotIndex;
  updateLightboxContent();

  lightboxEl.classList.add("active");
  lightboxEl.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";
}

function closeLightbox() {
  lightboxEl.classList.remove("active");
  lightboxEl.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
}

function updateLightboxContent() {
  if (!currentLightboxApp) return;

  const currentScreenshot = currentLightboxApp.screenshots[currentLightboxIndex];
  const totalScreenshots = currentLightboxApp.screenshots.length;

  lightboxAppTitleEl.textContent = currentLightboxApp.title;
  lightboxCounterEl.textContent = `${currentLightboxIndex + 1} of ${totalScreenshots}`;

  lightboxImgEl.style.opacity = "0.3";
  lightboxImgEl.src = currentScreenshot.full;
  lightboxImgEl.alt = currentScreenshot.alt;

  lightboxImgEl.onload = () => {
    lightboxImgEl.style.opacity = "1";
  };
}

function showPrevScreenshot() {
  if (!currentLightboxApp) return;
  const total = currentLightboxApp.screenshots.length;
  currentLightboxIndex = (currentLightboxIndex - 1 + total) % total;
  updateLightboxContent();
}

function showNextScreenshot() {
  if (!currentLightboxApp) return;
  const total = currentLightboxApp.screenshots.length;
  currentLightboxIndex = (currentLightboxIndex + 1) % total;
  updateLightboxContent();
}

// Lightbox Listeners
if (lightboxBtnCloseEl) lightboxBtnCloseEl.addEventListener("click", closeLightbox);
if (lightboxBackdropEl) lightboxBackdropEl.addEventListener("click", closeLightbox);
if (lightboxPrevEl) lightboxPrevEl.addEventListener("click", showPrevScreenshot);
if (lightboxNextEl) lightboxNextEl.addEventListener("click", showNextScreenshot);

window.addEventListener("keydown", (e) => {
  if (!lightboxEl.classList.contains("active")) return;
  if (e.key === "Escape") closeLightbox();
  else if (e.key === "ArrowLeft") showPrevScreenshot();
  else if (e.key === "ArrowRight") showNextScreenshot();
});

// ============================================================================
// Clipboard Copy Email
// ============================================================================

function setupCopyEmail() {
  if (!btnCopyEmail) return;

  btnCopyEmail.addEventListener("click", async () => {
    const email = PROFILE.email || "liuys614@gmail.com";
    try {
      await navigator.clipboard.writeText(email);
      showToast(`Copied ${email} to clipboard!`);

      const originalText = copyEmailLabel.textContent;
      copyEmailLabel.textContent = "Copied!";
      btnCopyEmail.style.borderColor = "#00dc82";

      setTimeout(() => {
        copyEmailLabel.textContent = originalText;
        btnCopyEmail.style.borderColor = "";
      }, 2000);
    } catch (err) {
      window.location.href = `mailto:${email}`;
    }
  });
}

function showToast(message) {
  if (!toastEl || !toastMessageEl) return;
  toastMessageEl.textContent = message;
  toastEl.classList.add("show");

  setTimeout(() => {
    toastEl.classList.remove("show");
  }, 2800);
}

// ============================================================================
// Initialization
// ============================================================================
document.addEventListener("DOMContentLoaded", () => {
  renderTimeline();
  renderProjects();
  setupCopyEmail();
});
