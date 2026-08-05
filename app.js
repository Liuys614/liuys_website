import { APPS } from './apps-data.js';

class AppShowcase {
  constructor() {
    this.currentIndex = 0;
    this.apps = APPS;

    // DOM Elements
    this.eyebrowTag = document.getElementById('eyebrowTag');
    this.mainHeading = document.getElementById('mainHeading');
    this.conciseDesc = document.getElementById('conciseDesc');
    this.ctaActions = document.getElementById('ctaActions');
    this.appSelectorList = document.getElementById('appSelectorList');
    this.stepCardsGrid = document.getElementById('stepCardsGrid');
    this.skyStage = document.getElementById('skyStage');
    this.screenImg = document.getElementById('screenImg');
    this.appIconImg = document.getElementById('appIconImg');

    this.init();
  }

  init() {
    this.renderSelectorList();
    this.updateAppView(0);
    this.attachEventListeners();
  }

  renderSelectorList() {
    this.appSelectorList.innerHTML = this.apps.map((app, idx) => `
      <div class="selector-item ${idx === 0 ? 'active' : ''}" data-index="${idx}">
        <div class="item-left">
          <img src="${app.icon}" alt="${app.title} Icon" class="item-icon-small" />
          <span class="item-title">${app.title}</span>
        </div>
        <div class="item-arrow">→</div>
      </div>
    `).join('');

    // Attach click handlers to selector items
    Array.from(this.appSelectorList.children).forEach((item, idx) => {
      item.addEventListener('click', () => this.goTo(idx));
    });
  }

  goTo(index) {
    if (index === this.currentIndex) return;
    this.currentIndex = index;

    // Subtle fade effect on right screenshot
    this.screenImg.style.opacity = '0.3';
    this.screenImg.style.transform = 'scale(0.98)';

    setTimeout(() => {
      this.updateAppView(index);
      this.screenImg.style.opacity = '1';
      this.screenImg.style.transform = 'scale(1)';
    }, 200);
  }

  updateAppView(index) {
    const app = this.apps[index];

    // 1. Update Left Column Text Content
    this.eyebrowTag.textContent = app.eyebrow;
    this.mainHeading.textContent = app.heading;
    this.conciseDesc.textContent = app.description;

    // Render CTAs
    this.ctaActions.innerHTML = app.links.map(link => `
      <a href="${link.url}" target="_blank" rel="noopener noreferrer" class="${link.type === 'appstore' ? 'btn-appstore' : 'btn-web'}">
        ${link.type === 'appstore' ? ' Download on App Store' : '🌐 Visit Website'}
      </a>
    `).join('');

    // 2. Update Theme Colors
    document.documentElement.style.setProperty('--accent-color', app.theme.accent);
    document.documentElement.style.setProperty('--accent-soft', app.theme.accentSoft);
    this.skyStage.style.background = app.theme.bgGradient;

    // 3. Render 4 Step Cards at Bottom
    this.stepCardsGrid.innerHTML = app.features.map((feat, fIdx) => `
      <div class="step-card ${fIdx === 0 ? 'highlight' : ''}">
        <div class="step-num">${feat.step}.</div>
        <div class="step-title">${feat.title}</div>
      </div>
    `).join('');

    // 4. Update Right Device Real Screenshot & Real App Icon
    this.screenImg.src = app.screenshot;
    this.screenImg.alt = `${app.title} Screenshot`;
    this.appIconImg.src = app.icon;
    this.appIconImg.alt = `${app.title} Icon`;

    // 5. Update Selector Active State
    Array.from(this.appSelectorList.children).forEach((item, idx) => {
      if (idx === index) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }

  attachEventListeners() {
    // Keyboard Arrow Keys
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
        const nextIdx = (this.currentIndex + 1) % this.apps.length;
        this.goTo(nextIdx);
      } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
        const prevIdx = (this.currentIndex - 1 + this.apps.length) % this.apps.length;
        this.goTo(prevIdx);
      }
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new AppShowcase();
});
