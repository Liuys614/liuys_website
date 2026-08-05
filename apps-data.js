export const APPS = [
  {
    id: "agricola-scorer",
    title: "Agricola Scorer",
    tagline: "Fast, Effortless Board Game Scorekeeping",
    category: "Board Games & Strategy",
    year: "2026",
    status: "Published",
    theme: {
      bgPrimary: "#0b2017",
      bgSecondary: "#1b4332",
      accent: "#52b788",
      accentGlow: "rgba(82, 183, 136, 0.35)",
      textPrimary: "#f8f9fa",
      textMuted: "#b7e4c7",
      cardBg: "rgba(27, 67, 50, 0.45)",
      border: "rgba(82, 183, 136, 0.25)"
    },
    description: "The ultimate score calculation companion for Agricola players. Say goodbye to pen-and-paper scorepads. Automatically calculate scores for fields, pastures, grain, vegetables, livestock, rooms, and card bonuses in seconds.",
    features: [
      "Instant Score Auto-Calculation",
      "Expansion & Farmers of Moor Support",
      "Game History & Player Statistics",
      "100% Offline Capable & Clean Interface"
    ],
    links: [
      { label: "Visit Website", url: "https://agricolascorer.io", type: "web" },
      { label: "App Store", url: "#", type: "appstore" }
    ],
    mockup: {
      icon: "🌾",
      headerTitle: "Agricola Scorepad",
      screenColor: "#112a1f",
      badge: "Game #42",
      stats: [
        { label: "Fields & Pastures", value: "18 pts" },
        { label: "Grain & Veggies", value: "14 pts" },
        { label: "Livestock Total", value: "16 pts" },
        { label: "Final Score", value: "48 PTS", highlight: true }
      ]
    }
  },
  {
    id: "grocery-price-scanner",
    title: "Grocery Price Scanner",
    tagline: "Smart Unit Price Comparison & Budgeting",
    category: "Shopping & Finance",
    year: "2026",
    status: "Published",
    theme: {
      bgPrimary: "#291304",
      bgSecondary: "#4a2307",
      accent: "#f39c12",
      accentGlow: "rgba(243, 156, 18, 0.35)",
      textPrimary: "#fff8f0",
      textMuted: "#fbe4c8",
      cardBg: "rgba(74, 35, 7, 0.45)",
      border: "rgba(243, 156, 18, 0.25)"
    },
    description: "Never overpay at the supermarket again. Easily scan shelf tags, compare true unit costs ($/oz, $/kg, $/unit), evaluate store deals instantly, and keep your grocery bill under control.",
    features: [
      "Instant Unit-Price Normalizer",
      "Price Tag Camera Scanner",
      "Multi-Item Deal Comparison",
      "Historical Price Tracker"
    ],
    links: [
      { label: "App Store", url: "#", type: "appstore" },
      { label: "View Source", url: "https://github.com/Liuys614/GroceryPrice", type: "github" }
    ],
    mockup: {
      icon: "🛒",
      headerTitle: "Unit Price Comparator",
      screenColor: "#331908",
      badge: "Best Value",
      stats: [
        { label: "Brand A (16 oz)", value: "$0.31 / oz" },
        { label: "Brand B (24 oz)", value: "$0.24 / oz", highlight: true },
        { label: "Potential Savings", value: "Save 22%" },
        { label: "Total In Cart", value: "$42.50" }
      ]
    }
  },
  {
    id: "pill-reminder",
    title: "Pill Reminder",
    tagline: "Reliable Medicine & Health Tracker",
    category: "Health & Medical",
    year: "2026",
    status: "Published",
    theme: {
      bgPrimary: "#03172e",
      bgSecondary: "#003566",
      accent: "#00b4d8",
      accentGlow: "rgba(0, 180, 216, 0.35)",
      textPrimary: "#f0f8ff",
      textMuted: "#90e0ef",
      cardBg: "rgba(0, 53, 102, 0.45)",
      border: "rgba(0, 180, 216, 0.25)"
    },
    description: "Stay on top of your health regimen with peace of mind. Flexible schedule reminders, dosage tracking, pill inventory alerts, and detailed log histories formatted for doctor visits.",
    features: [
      "Smart Custom Schedules",
      "Refill & Inventory Warnings",
      "Archived History & Export",
      "Private On-Device Storage"
    ],
    links: [
      { label: "App Store", url: "#", type: "appstore" },
      { label: "View Code", url: "https://github.com/Liuys614/Pill-Reminder", type: "github" }
    ],
    mockup: {
      icon: "💊",
      headerTitle: "Today's Schedule",
      screenColor: "#052242",
      badge: "Next: 2:00 PM",
      stats: [
        { label: "Morning Dose", value: "Taken at 8:00 AM", highlight: true },
        { label: "Afternoon Dose", value: "Vitamin D3 (1 Pill)" },
        { label: "Evening Dose", value: "Omega 3 (2 Pills)" },
        { label: "Streak", value: "14 Days Continuous" }
      ]
    }
  },
  {
    id: "alcohol-free-tracker",
    title: "Alcohol Free Tracker",
    tagline: "Mindful Sobriety & Milestone Companion",
    category: "Lifestyle & Wellness",
    year: "2026",
    status: "Published",
    theme: {
      bgPrimary: "#091a18",
      bgSecondary: "#173f3d",
      accent: "#4f8a80",
      accentGlow: "rgba(79, 138, 128, 0.35)",
      textPrimary: "#f5f7f6",
      textMuted: "#b8c6b8",
      cardBg: "rgba(23, 63, 61, 0.45)",
      border: "rgba(79, 138, 128, 0.25)"
    },
    description: "Celebrate every single day of your alcohol-free journey. Track your streak milestones, calculate money saved, monitor health recovery progress, and journal daily thoughts in a serene environment.",
    features: [
      "Sobriety Streak & Milestone Counters",
      "Money & Health Savings Calculator",
      "Mindful Craving & Reflection Journal",
      "Motivation Badges & Analytics"
    ],
    links: [
      { label: "Visit Website", url: "https://liuys614.github.io/AlcoholFreeTracker-Website", type: "web" },
      { label: "App Store", url: "#", type: "appstore" }
    ],
    mockup: {
      icon: "🌱",
      headerTitle: "Sobriety Journey",
      screenColor: "#102d2c",
      badge: "30 Days Milestone",
      stats: [
        { label: "Clean Streak", value: "30 Days", highlight: true },
        { label: "Money Saved", value: "$450.00" },
        { label: "Calorie Avoided", value: "18,000 kcal" },
        { label: "Current Mindset", value: "Calm & Energetic" }
      ]
    }
  }
];
