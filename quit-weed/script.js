/* ==========================================================================
   T-Break & Quit Weed: Unfog — Interactive Lab & Animations Controller
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  /* --------------------------------------------------------------------------
     1. HERO MODE SWITCHER: [30-Day T-Break] vs [Quit for Good]
     -------------------------------------------------------------------------- */
  const modeBtns = document.querySelectorAll('.mode-pill');
  const heroDynamicSub = document.getElementById('heroDynamicSub');
  const heroDynamicDesc = document.getElementById('heroDynamicDesc');

  const modeCopy = {
    tbreak: {
      sub: 'Reset Your CB1.',
      desc: 'Take a structured 7, 14, or 30-day tolerance break. Watch your CB1 receptors upregulate and reclaim deep REM sleep—100% private.'
    },
    quit: {
      sub: 'Unfog for Good.',
      desc: 'Leave daily THC haze behind without shame. Surf 3-minute cravings, track every gram skipped, and watch your dopamine baseline heal.'
    }
  };

  modeBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      modeBtns.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const mode = btn.dataset.mode;
      if (modeCopy[mode] && heroDynamicSub && heroDynamicDesc) {
        heroDynamicSub.textContent = modeCopy[mode].sub;
        heroDynamicDesc.textContent = modeCopy[mode].desc;
      }
    });
  });

  /* --------------------------------------------------------------------------
     2. LAB 01: INTERACTIVE CB1 RECEPTOR & BRAIN FOG UNFOGGER
     -------------------------------------------------------------------------- */
  const dayData = [
    {
      badge: 'Day 1 · THC Saturation',
      cb1: 20,
      rem: 15,
      clarity: 25,
      blurPx: 7,
      fogOpacity: 0.78,
      img: 'assets/recovery/24h.webp',
      quote: '"First 24h: Blood oxygen normalizes while residual THC begins clearing."'
    },
    {
      badge: 'Day 2 · Upregulation Starts',
      cb1: 45,
      rem: 30,
      clarity: 42,
      blurPx: 4,
      fogOpacity: 0.5,
      img: 'assets/recovery/48h.webp',
      quote: '"48 hours THC-free: PET scans show CB1 cannabinoid receptors begin rebuilding."'
    },
    {
      badge: 'Day 7 · REM Dream Rebound',
      cb1: 72,
      rem: 85,
      clarity: 68,
      blurPx: 1.8,
      fogOpacity: 0.25,
      img: 'assets/recovery/7d.webp',
      quote: '"Day 7: Deep REM sleep rebounds strongly—vivid dreams and overnight memory return."'
    },
    {
      badge: 'Day 14 · Hippocampus Unfogs',
      cb1: 88,
      rem: 94,
      clarity: 86,
      blurPx: 0.5,
      fogOpacity: 0.08,
      img: 'assets/recovery/14d.webp',
      quote: '"Day 14: Verbal recall, focus, and morning energy stabilize near baseline."'
    },
    {
      badge: 'Day 28 · 100% CB1 Baseline',
      cb1: 100,
      rem: 100,
      clarity: 100,
      blurPx: 0,
      fogOpacity: 0,
      img: 'assets/recovery/30d.webp',
      quote: '"Day 28: Full CB1 receptor density restored across cortex and hippocampus!"'
    }
  ];

  const dayBtns = document.querySelectorAll('.day-btn');
  const unfogDayBadge = document.getElementById('unfogDayBadge');
  const unfogRingCircle = document.getElementById('unfogRingCircle');
  const unfogBrainImg = document.getElementById('unfogBrainImg');
  const fogCloudOverlay = document.getElementById('fogCloudOverlay');
  const unfogPercentVal = document.getElementById('unfogPercentVal');
  const metricCb1Text = document.getElementById('metricCb1Text');
  const metricCb1Bar = document.getElementById('metricCb1Bar');
  const metricRemText = document.getElementById('metricRemText');
  const metricRemBar = document.getElementById('metricRemBar');
  const metricClarityText = document.getElementById('metricClarityText');
  const metricClarityBar = document.getElementById('metricClarityBar');
  const unfogStatusQuote = document.getElementById('unfogStatusQuote');

  const CIRCUMFERENCE = 603; // 2 * pi * 96

  function setUnfogStage(index) {
    const stage = dayData[index];
    if (!stage) return;

    dayBtns.forEach((b, idx) => b.classList.toggle('active', idx === index));

    if (unfogDayBadge) unfogDayBadge.textContent = stage.badge;
    if (unfogPercentVal) unfogPercentVal.textContent = `${stage.cb1}%`;

    if (unfogRingCircle) {
      const offset = CIRCUMFERENCE - (stage.cb1 / 100) * CIRCUMFERENCE;
      unfogRingCircle.style.strokeDashoffset = offset;
      unfogRingCircle.style.stroke = stage.cb1 === 100 ? '#D99B26' : '#2D6A4F';
    }

    if (unfogBrainImg) {
      unfogBrainImg.src = stage.img;
      unfogBrainImg.style.filter = `blur(${stage.blurPx}px) saturate(${0.7 + (stage.cb1 / 100) * 0.4})`;
      unfogBrainImg.style.transform = `scale(${0.92 + (stage.cb1 / 100) * 0.1})`;
    }

    if (fogCloudOverlay) {
      fogCloudOverlay.style.opacity = stage.fogOpacity;
    }

    if (metricCb1Text) metricCb1Text.textContent = `${stage.cb1}%`;
    if (metricCb1Bar) metricCb1Bar.style.width = `${stage.cb1}%`;

    if (metricRemText) metricRemText.textContent = `${stage.rem}%`;
    if (metricRemBar) metricRemBar.style.width = `${stage.rem}%`;

    if (metricClarityText) metricClarityText.textContent = `${stage.clarity}%`;
    if (metricClarityBar) metricClarityBar.style.width = `${stage.clarity}%`;

    if (unfogStatusQuote) unfogStatusQuote.textContent = stage.quote;
  }

  dayBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const idx = parseInt(btn.dataset.day, 10);
      setUnfogStage(idx);
    });
  });

  // Initialize at Day 2 (index 1)
  setUnfogStage(1);

  /* --------------------------------------------------------------------------
     3. LAB 02: LIVE 4-7-8 VAGUS NERVE BREATHING LOTUS
     -------------------------------------------------------------------------- */
  const lotusBloom = document.getElementById('lotusBloom');
  const lotusTimerNum = document.getElementById('lotusTimerNum');
  const lotusPhaseText = document.getElementById('lotusPhaseText');
  const pillInhale = document.getElementById('pillInhale');
  const pillHold = document.getElementById('pillHold');
  const pillExhale = document.getElementById('pillExhale');
  const btnLotusToggle = document.getElementById('btnLotusToggle');

  const phases = [
    { name: 'INHALE', seconds: 4, cls: 'phase-inhale', pill: pillInhale },
    { name: 'HOLD', seconds: 7, cls: 'phase-hold', pill: pillHold },
    { name: 'EXHALE', seconds: 8, cls: 'phase-exhale', pill: pillExhale }
  ];

  let currentPhaseIdx = 0;
  let secondsLeft = phases[0].seconds;
  let isBreathing = true;
  let breathInterval = null;

  function applyPhaseVisuals(phase) {
    if (!lotusBloom) return;
    lotusBloom.classList.remove('phase-inhale', 'phase-hold', 'phase-exhale');
    lotusBloom.classList.add(phase.cls);

    [pillInhale, pillHold, pillExhale].forEach((p) => {
      if (p) p.classList.remove('active');
    });
    if (phase.pill) phase.pill.classList.add('active');

    if (lotusPhaseText) lotusPhaseText.textContent = phase.name;
    if (lotusTimerNum) lotusTimerNum.textContent = `${secondsLeft}s`;
  }

  function startBreathingLoop() {
    applyPhaseVisuals(phases[currentPhaseIdx]);
    breathInterval = setInterval(() => {
      if (!isBreathing) return;
      secondsLeft -= 1;
      if (secondsLeft <= 0) {
        currentPhaseIdx = (currentPhaseIdx + 1) % phases.length;
        secondsLeft = phases[currentPhaseIdx].seconds;
        applyPhaseVisuals(phases[currentPhaseIdx]);
      } else if (lotusTimerNum) {
        lotusTimerNum.textContent = `${secondsLeft}s`;
      }
    }, 1000);
  }

  startBreathingLoop();

  if (btnLotusToggle) {
    btnLotusToggle.addEventListener('click', () => {
      isBreathing = !isBreathing;
      btnLotusToggle.querySelector('span').textContent = isBreathing
        ? 'Pause Breathing Guide'
        : 'Resume 4-7-8 Breathing';
    });
  }

  /* --------------------------------------------------------------------------
     4. SCREENSHOT GALLERY CAROUSEL BUTTONS
     -------------------------------------------------------------------------- */
  const carousel = document.getElementById('screenshotsCarousel');
  const prevBtn = document.getElementById('galleryPrev');
  const nextBtn = document.getElementById('galleryNext');

  if (carousel && prevBtn && nextBtn) {
    prevBtn.addEventListener('click', () => {
      carousel.scrollBy({ left: -300, behavior: 'smooth' });
    });
    nextBtn.addEventListener('click', () => {
      carousel.scrollBy({ left: 300, behavior: 'smooth' });
    });
  }
});
