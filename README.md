# Louis Liu — Apps & Projects Showcase

An ultra-modern personal showcase website designed for **GitHub Pages** (`liuys614.github.io`). It features full-viewport dynamic background color morphing, 3D device mockup UI previews, smooth transitions, and multi-device responsive layouts.

## Featured Apps

1. **Agricola Scorer** — Board game score calculation assistant (Earthy Forest Green theme `#1b4332`).
2. **Grocery Price Scanner** — Smart unit-price comparison & barcode scanner (Citrus Amber theme `#4a2307`).
3. **Pill Reminder** — Medicine schedule & pill tracking reminder (Electric Medical Blue theme `#003566`).
4. **Alcohol Free Tracker** — Mindful sobriety milestone tracker (Tranquil Deep Teal theme `#173f3d`).

## Local Preview

No build steps, node packages, or compilers required! Simply run a local HTTP server:

```bash
# Using Python
python3 -m http.server 8000

# Or using npx serve
npx serve .
```

Then open `http://localhost:8000` in your web browser.

## Deployment to GitHub Pages

1. Commit and push your changes to GitHub:
   ```bash
   git add .
   git commit -m "Build app showcase website"
   git push origin main
   ```

2. Enable GitHub Pages in your repository settings:
   - Go to **Settings** > **Pages**
   - Source: **Deploy from a branch**
   - Branch: `main` / `/ (root)`
   - Save and visit your live site!
