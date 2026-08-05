import { APPS } from './apps-data.js';

class AppShowcase {
  constructor() {
    this.currentIndex = 0;
    this.apps = APPS;
    this.isTransitioning = false;

    // DOM Elements
    this.container = document.getElementById('appContainer');
    this.ambientGlow = document.getElementById('ambientGlow');
    this.tabsNav = document.getElementById('appTabsNav');
    this.infoPane = document.getElementById('infoPane');
    this.categoryEl = document.getElementById('appCategory');
    this.statusEl = document.getElementById('appStatus');
    this.titleEl = document.getElementById('appTitle');
    this.taglineEl = document.getElementById('appTagline');
    this.descEl = document.getElementById('appDescription');
    this.featuresListEl = document.getElementById('featuresList');
    this.ctaGroupEl = document.getElementById('ctaGroup');

    // Phone Mockup Elements
    this.iphoneFrame = document.getElementById('iphoneFrame');
    this.screenContent = document.getElementById('screenContent');
    this.screenIcon = document.getElementById('screenIcon');
    this.screenBadge = document.getElementById('screenBadge');
    this.screenHeaderTitle = document.getElementById('screenHeaderTitle');
    this.screenStats = document.getElementById('screenStats');

    // Controls
    this.prevBtn = document.getElementById('prevBtn');
    this.nextBtn = document.getElementById('nextBtn');
    this.currentIndexEl = document.getElementById('currentIndex');
    this.totalIndexEl = document.getElementById('totalIndex');

    this.init();
  }

  init() {
    this.renderTabs();
    this.updateShowcase(0);
    this.attachEventListeners();
  }

  renderTabs() {
    this.tabsNav.innerHTML = '';
    this.apps.forEach((app, idx) => {
      const btn = document.createElement('button');
      btn.className = `tab-btn ${idx === 0 ? 'active' : ''}`;
      btn.dataset.index = idx;
      btn.innerHTML = `<span>${app.mockup.icon}</span> ${app.title}`;
      btn.addEventListener('click', () => this.goTo(idx));
      this.tabsNav.appendChild(btn);
    });

    this.totalIndexEl.textContent = String(this.apps.length).padStart(2, '0');
  }

  goTo(index) {
    if (index === this.currentIndex || this.isTransitioning) return;
    if (index < 0) index = this.apps.length - 1;
    if (index >= this.apps.length) index = 0;

    this.isTransitioning = true;
    this.currentIndex = index;

    // Trigger subtle out-animation
    this.infoPane.classList.add('transitioning');
    this.screenContent.style.opacity = '0';
    this.screenContent.style.transform = 'scale(0.96)';

    setTimeout(() => {
      this.updateShowcase(index);

      // Trigger in-animation
      this.infoPane.classList.remove('transitioning');
      this.screenContent.style.opacity = '1';
      this.screenContent.style.transform = 'scale(1)';

      setTimeout(() => {
        this.isTransitioning = false;
      }, 350);
    }, 250);
  }

  next() {
    this.goTo(this.currentIndex + 1);
  }

  prev() {
    this.goTo(this.currentIndex - 1);
  }

  updateShowcase(index) {
    const app = this.apps[index];

    // 1. Update CSS Custom Variables on Container & Root
    const theme = app.theme;
    this.container.style.setProperty('--app-bg-primary', theme.bgPrimary);
    this.container.style.setProperty('--app-bg-secondary', theme.bgSecondary);
    this.container.style.setProperty('--app-accent', theme.accent);
    this.container.style.setProperty('--app-accent-glow', theme.accentGlow);
    this.container.style.setProperty('--app-text-primary', theme.textPrimary);
    this.container.style.setProperty('--app-text-muted', theme.textMuted);
    this.container.style.setProperty('--app-card-bg', theme.cardBg);
    this.container.style.setProperty('--app-border', theme.border);

    // 2. Update Info Pane Content
    this.categoryEl.textContent = app.category;
    this.statusEl.textContent = `${app.status} • ${app.year}`;
    this.titleEl.textContent = app.title;
    this.taglineEl.textContent = app.tagline;
    this.descEl.textContent = app.description;

    // Render Features
    this.featuresListEl.innerHTML = app.features.map(feat => `
      <div class="feature-item">
        <span class="feature-icon">✦</span>
        <span>${feat}</span>
      </div>
    `).join('');

    // Render CTAs
    this.ctaGroupEl.innerHTML = app.links.map(link => `
      <a href="${link.url}" target="_blank" rel="noopener noreferrer" class="${link.type === 'appstore' ? 'btn-primary' : 'btn-secondary'}">
        ${link.type === 'appstore' ? ' App Store' : link.type === 'web' ? '🌐 Launch Website' : '💻 GitHub Repo'}
      </a>
    `).join('');

    // 3. Update iPhone Mockup Content
    this.screenIcon.textContent = app.mockup.icon;
    this.screenBadge.textContent = app.mockup.badge;
    this.screenHeaderTitle.textContent = app.mockup.headerTitle;

    this.screenStats.innerHTML = app.mockup.stats.map(stat => `
      <div class="stat-card ${stat.highlight ? 'highlight' : ''}">
        <span class="stat-label">${stat.label}</span>
        <span class="stat-val">${stat.value}</span>
      </div>
    `).join('');

    // 4. Update Header Tabs & Counter
    Array.from(this.tabsNav.children).forEach((btn, idx) => {
      if (idx === index) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    this.currentIndexEl.textContent = String(index + 1).padStart(2, '0');
  }

  attachEventListeners() {
    // Arrow Controls
    this.prevBtn.addEventListener('click', () => this.prev());
    this.nextBtn.addEventListener('click', () => this.next());

    // Keyboard Navigation
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        this.next();
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        this.prev();
      }
    });

    // Mouse wheel / trackpad swipe
    let wheelTimeout;
    window.addEventListener('wheel', (e) => {
      clearTimeout(wheelTimeout);
      wheelTimeout = setTimeout(() => {
        if (e.deltaY > 30 || e.deltaX > 30) {
          this.next();
        } else if (e.deltaY < -30 || e.deltaX < -30) {
          this.prev();
        }
      }, 60);
    }, { passive: true });

    // Touch Swipe for Mobile
    let touchStartX = 0;
    let touchStartY = 0;

    window.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
    }, { passive: true });

    window.addEventListener('touchend', (e) => {
      const touchEndX = e.changedTouches[0].screenX;
      const touchEndY = e.changedTouches[0].screenY;
      const diffX = touchStartX - touchEndX;
      const diffY = touchStartY - touchEndY;

      if (Math.abs(diffX) > 50 && Math.abs(diffX) > Math.abs(diffY)) {
        if (diffX > 0) {
          this.next();
        } else {
          this.prev();
        }
      }
    }, { passive: true });
  }
}

// Initialize on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  new AppShowcase();
});
