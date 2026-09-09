// Portfolio Data for Louis Liu
export const PROFILE = {
  "name": "Louis Liu",
  "role": "iOS Software Engineer",
  "location": "United States",
  "email": "liuys614@gmail.com",
  "github": "https://github.com/liuys614",
  "linkedin": "https://www.linkedin.com/in/louisliu-ios",
  "avatar": "images/profile.jpg",
  "headline": "iOS Software Engineer",
  "bio": "I am an iOS software engineer and indie app maker passionate about crafting high-performance Apple platform experiences that not only perform at enterprise scale for millions of users, but also delight people with seamless everyday functionality.",
  "status": "Available for iOS Opportunities",
  "timeline": [
    {
      "id": "exp-indie",
      "type": "work",
      "period": "2024 – Present",
      "role": "Founder & Lead iOS Developer",
      "organization": "Independent App Studio",
      "location": "United States",
      "highlights": [
        "Architected, designed, and shipped 5 native iOS apps live on the App Store: Inkstone, Pill Reminder, Grocery Price Scanner, Alcohol Free Tracker, and Agricola Scorer.",
        "Engineered on-device camera OCR scanning, PDFKit digital signing pipelines, and offline-first local data synchronization.",
        "Automated CI/CD deployment pipelines, StoreKit 2 monetization, and App Store Connect localization across 40+ storefronts."
      ]
    },
    {
      "id": "exp-charter",
      "type": "work",
      "period": "2023 – 2026",
      "role": "iOS Software Engineer (Contract)",
      "organization": "Charter Communications — Spectrum TV",
      "location": "Remote, US",
      "highlights": [
        "Architected and delivered the complete VOD/cDVR player overlay from scratch in SwiftUI & UIKit, including custom scrubber, PiP, AirPlay, and Chromecast integration.",
        "Built the Seamless Entertainment swimlane end-to-end using Server-Driven UI (UINode), deep link routing, and full VoiceOver accessibility.",
        "Engineered a generic actor-based AsyncTaskDeduplicator utility, resolving production DRM playback crashes caused by concurrent async task races.",
        "Fixed 10+ critical production crashes and resolved complex iPad multitasking layout bugs using registerForTraitChanges and safe area APIs."
      ]
    },
    {
      "id": "exp-synopsys",
      "type": "work",
      "period": "Aug 2021 – Oct 2022",
      "role": "Compiler Senior Software Engineer",
      "organization": "Synopsys Inc (Verilog Compiler & Emulation)",
      "location": "Hsinchu, Taiwan",
      "highlights": [
        "Developed and optimized C/C++ compiler and runtime software inside VCS (Verilog Compiler Simulator) for ZeBu FPGA-based HW/SW co-simulation platforms.",
        "Achieved a 20x simulation performance acceleration for Tier-1 semiconductor design partners by engineering memory-efficient APIs and low-latency IPC bridges.",
        "Engineered Linux-based simulation infrastructure, debugging complex HW/SW integration and timing issues across compiler, simulator, and emulator verification flows.",
        "Authored automated diagnostic suites and test pipelines in Python and Bash to validate hardware models, compile configurations, and simulator integrity."
      ]
    },
    {
      "id": "exp-mindflow",
      "type": "work",
      "period": "Aug 2020 – May 2021",
      "role": "Founder & Tech Lead",
      "organization": "Mindflow Education Studio",
      "location": "Taiwan",
      "highlights": [
        "Founded an educational technology startup studio managing digital platforms and curriculum delivery.",
        "Taught computer science and coding principles to young students, fostering algorithmic thinking."
      ]
    },
    {
      "id": "exp-phison",
      "type": "work",
      "period": "Jun 2018 – Aug 2020",
      "role": "Senior Firmware Engineer",
      "organization": "Phison Electronics (NVMe & SSD Controllers)",
      "location": "Taiwan",
      "highlights": [
        "Designed and programmed SSD controller firmware in C/C++ implementing NVMe 1.3 protocol and PCIe initialization sequences for SD 7.0 (SD Express).",
        "Engineered Flash Translation Layer (FTL) modules—optimizing garbage collection, wear leveling, and bad block management—and implemented RTD3 low-power mode (LPM) hibernation, slashing power consumption by 80%.",
        "Built a C++ SSD simulation framework to model NVMe submission/completion queues (SQ/CQ) with NAND flash memory fetching and data pipeline processing.",
        "Automated hardware-in-the-loop (HIL) diagnostic testing and firmware deployment with custom Python and PowerShell pipelines."
      ]
    },
    {
      "id": "exp-syntec",
      "type": "work",
      "period": "Nov 2014 – Feb 2018",
      "role": "Embedded Software Engineer",
      "organization": "Syntec Technology (CNC Controllers & Industrial IoT)",
      "location": "Taiwan",
      "highlights": [
        "Migrated CNC motion controllers from Windows CE to Embedded Linux, porting real-time control software in C/C++ and re-hosting device daemons as Linux system services.",
        "Architected an Industrial IoT telemetry platform streaming CNC machine data via MQTT to cloud backends, designing compact serialization schemas for bandwidth-constrained links.",
        "Engineered low-level device communication drivers and concurrent socket networking, diagnosing shop-floor connectivity faults with Wireshark to reduce packet loss by 20%.",
        "Founded and led the Smart Factory engineering team across firmware, cloud, and web, successfully securing and delivering the company's first commercial deployment."
      ]
    },
    {
      "id": "edu-ms",
      "type": "education",
      "period": "2012 – 2014",
      "role": "Master of Science in Computer Science",
      "organization": "National Chiao-Tung University (NCTU)",
      "location": "Hsinchu, Taiwan",
      "highlights": [
        "Published IEEE research: <a href=\"https://ieeexplore.ieee.org/document/7051495\" target=\"_blank\" rel=\"noopener noreferrer\" class=\"timeline-link\">\"Foveation-Based Image Quality Assessment\"</a> at IEEE VCIP (Visual Communications and Image Processing Conference)."
      ]
    },
    {
      "id": "edu-bs",
      "type": "education",
      "period": "2008 – 2012",
      "role": "Bachelor of Science in Computer Science",
      "organization": "National Chiao-Tung University (NCTU)",
      "location": "Hsinchu, Taiwan",
      "highlights": [
        "Core computer science foundation: Data Structures, Algorithms, Operating Systems, Computer Architecture, and Object-Oriented Software Design."
      ]
    }
  ],
  "techStack": [
    "Swift",
    "SwiftUI",
    "UIKit",
    "Swift Concurrency (Actors, async/await)",
    "Combine",
    "AVFoundation & Streaming",
    "PDFKit & Digital Signatures",
    "Server-Driven UI",
    "Core Data / SwiftData",
    "StoreKit 2",
    "Accessibility (VoiceOver)",
    "Vision Pro & tvOS",
    "CI/CD & App Store Connect"
  ]
};

export const APPS = [
  {
    "id": "inkstone",
    "trackId": "6801701847",
    "title": "Inkstone: Sign PDF & Docs",
    "category": "Business & Productivity",
    "year": "2026",
    "tagline": "eSign Contracts & Share Encrypted Signing Links",
    "description": "Prepare documents in seconds and share a secure signing link. Recipients sign directly in their mobile or desktop browser with zero app download or account creation required.",
    "icon": "images/icons/inkstone.png",
    "accent": "#6366f1",
    "features": [
      "Instant PDF import & camera document scanning",
      "Signatures, initials, dates, and form fields",
      "Encrypted browser signing links with zero friction",
      "SHA-256 digital certificate & audit trail"
    ],
    "links": [
      {
        "label": "Visit Website",
        "url": "https://inkstone-app-prod.web.app",
        "type": "web"
      },
      {
        "label": "App Store",
        "url": "https://apps.apple.com/app/id6801701847",
        "type": "appstore"
      }
    ],
    "appStoreRating": null,
    "appStoreReviews": 0,
    "screenshots": [
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/5f/4a/85/5f4a85ba-998d-76f4-a7d1-2de6c0ff47db/01.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/5f/4a/85/5f4a85ba-998d-76f4-a7d1-2de6c0ff47db/01.png/1280x0w.webp",
        "alt": "Inkstone: Sign PDF & Docs Screenshot 1"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/33/82/14/338214dc-9025-6f22-9ee4-3b4d935c3bf2/02.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/33/82/14/338214dc-9025-6f22-9ee4-3b4d935c3bf2/02.png/1280x0w.webp",
        "alt": "Inkstone: Sign PDF & Docs Screenshot 2"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/a8/eb/ae/a8ebae6e-93d7-0823-7fa3-74502bed83f6/03.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/a8/eb/ae/a8ebae6e-93d7-0823-7fa3-74502bed83f6/03.png/1280x0w.webp",
        "alt": "Inkstone: Sign PDF & Docs Screenshot 3"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/7d/fd/df/7dfddf85-498a-2aca-dcda-460a6fba66d1/04.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/7d/fd/df/7dfddf85-498a-2aca-dcda-460a6fba66d1/04.png/1280x0w.webp",
        "alt": "Inkstone: Sign PDF & Docs Screenshot 4"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/e4/17/95/e41795f4-1bb1-a029-110a-16a8917e1504/05.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/e4/17/95/e41795f4-1bb1-a029-110a-16a8917e1504/05.png/1280x0w.webp",
        "alt": "Inkstone: Sign PDF & Docs Screenshot 5"
      }
    ]
  },
  {
    "id": "pill-reminder",
    "trackId": "6794415548",
    "title": "Supplement & Pill Reminder",
    "category": "Health & Medical",
    "year": "2026",
    "tagline": "Reliable Medicine & Supplement Tracker",
    "description": "Stay on top of your daily health regimen with reliable schedule notifications, dosage tracking, automated refill alerts, and exportable doctor logs.",
    "icon": "images/icons/pill.png",
    "accent": "#3b82f6",
    "features": [
      "Smart recurring medication & vitamin schedules",
      "Low-supply alerts before medicine runs out",
      "Doctor-ready PDF & CSV health export",
      "100% on-device privacy with zero tracking"
    ],
    "links": [
      {
        "label": "App Store",
        "url": "https://apps.apple.com/app/id6794415548",
        "type": "appstore"
      }
    ],
    "appStoreRating": "5.0",
    "appStoreReviews": 2,
    "screenshots": [
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/a0/10/75/a01075c7-f77f-d55b-7b2c-9e12b47448f6/01_0_APP_IPHONE_67_0.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/a0/10/75/a01075c7-f77f-d55b-7b2c-9e12b47448f6/01_0_APP_IPHONE_67_0.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 1"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/00/38/56/003856f2-c9ad-f45c-4085-a386b44e84b0/02_1_APP_IPHONE_67_1.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/00/38/56/003856f2-c9ad-f45c-4085-a386b44e84b0/02_1_APP_IPHONE_67_1.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 2"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/83/31/82/8331821d-06fc-d637-7d31-c74cc23eea37/03_2_APP_IPHONE_67_2.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/83/31/82/8331821d-06fc-d637-7d31-c74cc23eea37/03_2_APP_IPHONE_67_2.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 3"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/18/e9/4c/18e94c8b-b12d-322e-6f54-ebd3c3a96f2f/04_3_APP_IPHONE_67_3.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/18/e9/4c/18e94c8b-b12d-322e-6f54-ebd3c3a96f2f/04_3_APP_IPHONE_67_3.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 4"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/37/f8/82/37f88206-c78d-d36b-ebf7-9be0624c8dcf/05_4_APP_IPHONE_67_4.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/37/f8/82/37f88206-c78d-d36b-ebf7-9be0624c8dcf/05_4_APP_IPHONE_67_4.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 5"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/89/06/d6/8906d622-4781-10bb-bae2-e67209d0f90c/06_5_APP_IPHONE_67_5.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/89/06/d6/8906d622-4781-10bb-bae2-e67209d0f90c/06_5_APP_IPHONE_67_5.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 6"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/da/d8/c5/dad8c57f-528b-3a3c-8333-d1d691e23d2c/07_6_APP_IPHONE_67_6.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/da/d8/c5/dad8c57f-528b-3a3c-8333-d1d691e23d2c/07_6_APP_IPHONE_67_6.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 7"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/a6/c7/2d/a6c72d17-54cb-fd8d-2793-c07300999878/08_7_APP_IPHONE_67_7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/a6/c7/2d/a6c72d17-54cb-fd8d-2793-c07300999878/08_7_APP_IPHONE_67_7.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 8"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/54/a1/9a/54a19ab7-6075-657f-b5fb-a88f7e8af26a/09_8_APP_IPHONE_67_8.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/54/a1/9a/54a19ab7-6075-657f-b5fb-a88f7e8af26a/09_8_APP_IPHONE_67_8.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 9"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/2d/e7/56/2de75670-c710-5d93-169a-f7c3ba64b352/10_9_APP_IPHONE_67_9.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/2d/e7/56/2de75670-c710-5d93-169a-f7c3ba64b352/10_9_APP_IPHONE_67_9.png/1280x0w.webp",
        "alt": "Supplement & Pill Reminder Screenshot 10"
      }
    ]
  },
  {
    "id": "grocery-price-scanner",
    "trackId": "6773533304",
    "title": "Grocery Price Scanner",
    "category": "Shopping & Finance",
    "year": "2026",
    "tagline": "Unit Price Comparator & Budget Tracker",
    "description": "Instantly scan supermarket price tags, normalize unit prices across ounces, grams, and count, and discover the true best deal before checkout.",
    "icon": "images/icons/grocery.png",
    "accent": "#f59e0b",
    "features": [
      "Camera tag scanning & OCR price recognition",
      "Automatic unit cost normalization ($/oz, $/lb, $/kg)",
      "Multi-store price comparison & inflation log",
      "Offline-first speed for quick supermarket aisles"
    ],
    "links": [
      {
        "label": "Visit Website",
        "url": "https://groceryprice.app/",
        "type": "web"
      },
      {
        "label": "App Store",
        "url": "https://apps.apple.com/app/id6773533304",
        "type": "appstore"
      }
    ],
    "appStoreRating": "5.0",
    "appStoreReviews": 3,
    "screenshots": [
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/21/25/9c/21259cd0-85fc-f860-7230-2e6903edc86a/screen_1_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/21/25/9c/21259cd0-85fc-f860-7230-2e6903edc86a/screen_1_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 1"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/bf/b4/70/bfb47097-20fb-18f2-c719-9c9e7fa44667/screen_2_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/bf/b4/70/bfb47097-20fb-18f2-c719-9c9e7fa44667/screen_2_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 2"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/bb/29/89/bb298941-6ed3-eab1-fb1d-aac9d83cda94/screen_3_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/bb/29/89/bb298941-6ed3-eab1-fb1d-aac9d83cda94/screen_3_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 3"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/f7/35/51/f73551ca-f05a-f7db-2b8d-26e90c6da90f/screen_4_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/f7/35/51/f73551ca-f05a-f7db-2b8d-26e90c6da90f/screen_4_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 4"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/67/d0/27/67d0272a-d320-967c-c2b0-6cb0a841bc1e/screen_5_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/67/d0/27/67d0272a-d320-967c-c2b0-6cb0a841bc1e/screen_5_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 5"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/77/e1/2b/77e12b3e-5ef4-3b0c-ab82-3ac72bb5fe19/screen_6_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/77/e1/2b/77e12b3e-5ef4-3b0c-ab82-3ac72bb5fe19/screen_6_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 6"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/3f/af/ac/3fafaccd-caf3-e7f6-19e1-9ebda1720f0d/screen_7_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/3f/af/ac/3fafaccd-caf3-e7f6-19e1-9ebda1720f0d/screen_7_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 7"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/cb/e4/0a/cbe40a69-ce6c-5426-2e9d-a4404bdd0a41/screen_8_6.7.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/cb/e4/0a/cbe40a69-ce6c-5426-2e9d-a4404bdd0a41/screen_8_6.7.png/1280x0w.webp",
        "alt": "Grocery Price Scanner Screenshot 8"
      }
    ]
  },
  {
    "id": "alcohol-free-tracker",
    "trackId": "6791035303",
    "title": "Alcohol Free Tracker",
    "category": "Lifestyle & Wellness",
    "year": "2026",
    "tagline": "Mindful Sobriety & Habit Milestone Companion",
    "description": "Track your sobriety streak in real-time, celebrate health and financial milestones, and reflect in a private, distraction-free journal.",
    "icon": "images/icons/alcohol.png",
    "accent": "#10b981",
    "features": [
      "Real-time streak counter for days & hours",
      "Calculators for money and calories saved",
      "Private reflection journal & trigger tracker",
      "Milestone badges and customizable widgets"
    ],
    "links": [
      {
        "label": "Visit Website",
        "url": "https://liuys614.github.io/AlcoholFreeTracker-Website",
        "type": "web"
      },
      {
        "label": "App Store",
        "url": "https://apps.apple.com/app/id6791035303",
        "type": "appstore"
      }
    ],
    "appStoreRating": "5.0",
    "appStoreReviews": 1,
    "screenshots": [
      {
        "thumb": "images/screenshots/alcohol/0_APP_IPHONE_69_0_thumb.jpg",
        "full": "images/screenshots/alcohol/0_APP_IPHONE_69_0.jpg",
        "alt": "Alcohol Free Tracker Screenshot 1"
      },
      {
        "thumb": "images/screenshots/alcohol/1_APP_IPHONE_69_1_thumb.jpg",
        "full": "images/screenshots/alcohol/1_APP_IPHONE_69_1.jpg",
        "alt": "Alcohol Free Tracker Screenshot 2"
      },
      {
        "thumb": "images/screenshots/alcohol/2_APP_IPHONE_69_2_thumb.jpg",
        "full": "images/screenshots/alcohol/2_APP_IPHONE_69_2.jpg",
        "alt": "Alcohol Free Tracker Screenshot 3"
      },
      {
        "thumb": "images/screenshots/alcohol/3_APP_IPHONE_69_3_thumb.jpg",
        "full": "images/screenshots/alcohol/3_APP_IPHONE_69_3.jpg",
        "alt": "Alcohol Free Tracker Screenshot 4"
      },
      {
        "thumb": "images/screenshots/alcohol/4_APP_IPHONE_69_4_thumb.jpg",
        "full": "images/screenshots/alcohol/4_APP_IPHONE_69_4.jpg",
        "alt": "Alcohol Free Tracker Screenshot 5"
      },
      {
        "thumb": "images/screenshots/alcohol/5_APP_IPHONE_69_5_thumb.jpg",
        "full": "images/screenshots/alcohol/5_APP_IPHONE_69_5.jpg",
        "alt": "Alcohol Free Tracker Screenshot 6"
      },
      {
        "thumb": "images/screenshots/alcohol/6_APP_IPHONE_69_6_thumb.jpg",
        "full": "images/screenshots/alcohol/6_APP_IPHONE_69_6.jpg",
        "alt": "Alcohol Free Tracker Screenshot 7"
      },
      {
        "thumb": "images/screenshots/alcohol/7_APP_IPHONE_69_7_thumb.jpg",
        "full": "images/screenshots/alcohol/7_APP_IPHONE_69_7.jpg",
        "alt": "Alcohol Free Tracker Screenshot 8"
      },
      {
        "thumb": "images/screenshots/alcohol/8_APP_IPHONE_69_8_thumb.jpg",
        "full": "images/screenshots/alcohol/8_APP_IPHONE_69_8.jpg",
        "alt": "Alcohol Free Tracker Screenshot 9"
      },
      {
        "thumb": "images/screenshots/alcohol/9_APP_IPHONE_69_9_thumb.jpg",
        "full": "images/screenshots/alcohol/9_APP_IPHONE_69_9.jpg",
        "alt": "Alcohol Free Tracker Screenshot 10"
      }
    ]
  },
  {
    "id": "agricola-scorer",
    "trackId": "6741305872",
    "title": "Agricola Score Sheet",
    "category": "Board Games & Strategy",
    "year": "2026",
    "tagline": "Effortless Board Game Scorekeeping",
    "description": "Effortlessly score your Agricola board game sessions with automated scoring for pastures, grain, livestock, and Farmers of the Moor expansions.",
    "icon": "images/icons/agricola.png",
    "accent": "#16a34a",
    "features": [
      "Digital scorepad replacing paper score sheets",
      "Full expansion & Farmers of the Moor support",
      "Game history, leaderboard, and high scores",
      "Fast, touch-first input with zero offline friction"
    ],
    "links": [
      {
        "label": "Visit Website",
        "url": "https://agricolascorer.io",
        "type": "web"
      },
      {
        "label": "App Store",
        "url": "https://apps.apple.com/app/id6741305872",
        "type": "appstore"
      }
    ],
    "appStoreRating": "5.0",
    "appStoreReviews": 2,
    "screenshots": [
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/a2/27/09/a22709fa-fe89-3bb4-d601-aa01ec97b1b2/01.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/a2/27/09/a22709fa-fe89-3bb4-d601-aa01ec97b1b2/01.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 1"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/44/e7/b2/44e7b2ef-fda9-4680-a318-7ee3f2faf460/02.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/44/e7/b2/44e7b2ef-fda9-4680-a318-7ee3f2faf460/02.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 2"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/8e/0d/6c/8e0d6c0f-7e9c-3f8d-3fa4-acbfce576cdc/03.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/8e/0d/6c/8e0d6c0f-7e9c-3f8d-3fa4-acbfce576cdc/03.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 3"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/e3/90/94/e3909427-07fa-8763-3b85-9c8f7c547b88/04.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/e3/90/94/e3909427-07fa-8763-3b85-9c8f7c547b88/04.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 4"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/7b/2c/cb/7b2ccb75-a83a-bc95-870a-a905e332b552/05.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/7b/2c/cb/7b2ccb75-a83a-bc95-870a-a905e332b552/05.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 5"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/6b/cd/7a/6bcd7a3f-d956-66cb-427c-76368b7ea104/06.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource221/v4/6b/cd/7a/6bcd7a3f-d956-66cb-427c-76368b7ea104/06.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 6"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/9f/56/42/9f564256-2eb0-c6f2-d120-7c94714c4663/07.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/9f/56/42/9f564256-2eb0-c6f2-d120-7c94714c4663/07.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 7"
      },
      {
        "thumb": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/ae/91/a7/ae91a70c-383a-c7c7-26c4-89d8a40ab0a4/08.png/640x0w.webp",
        "full": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/ae/91/a7/ae91a70c-383a-c7c7-26c4-89d8a40ab0a4/08.png/1280x0w.webp",
        "alt": "Agricola Score Sheet Screenshot 8"
      }
    ]
  }
];
