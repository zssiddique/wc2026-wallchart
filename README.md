# 🏆 FIFA World Cup 2026 – Live Wall Chart

**➡ [Open Live Wall Chart](https://YOUR-USERNAME.github.io/wc2026-wallchart/)**

---

## 📡 Live feed — how it actually works

Previous versions tried ESPN via CORS proxies. Those are unreliable.
This version uses **4 sources that are genuinely browser-safe** (all serve `Access-Control-Allow-Origin: *`):

| Priority | Source | Type | Notes |
|----------|--------|------|-------|
| 1st | `worldcup26.ir/get/games` | Purpose-built WC2026 API | CORS enabled, no key |
| 2nd | `wcup2026.org/api/data.php` | Community PHP project | CORS enabled, no key |
| 3rd | `openfootball` GitHub raw JSON | Static file on GitHub | Always CORS-open |
| 4th | `scores.json` in this repo | Your own GitHub Pages file | Same origin, zero CORS |

**The 4th source is the safety net** — GitHub Actions fetches scores every 5 minutes server-side (no CORS) and saves `scores.json` into this repo. Your browser loads it from the same domain. It always works.

---

## 🚀 Deploy to GitHub Pages (5 minutes)

### Step 1 — Create repo
1. Go to **[github.com/new](https://github.com/new)**
2. Name: `wc2026-wallchart` · Set to **Public** · No checkboxes · **Create**

### Step 2 — Upload files
1. Click **"uploading an existing file"**
2. Unzip the downloaded package
3. On **Mac**: press `Cmd+Shift+.` to show hidden files, then drag everything in
4. On **Windows**: View → tick "Hidden items", then drag everything in
5. Commit

### Step 3 — Enable GitHub Pages
Settings → Pages → Source: **GitHub Actions** → Save

### Step 4 — Done!
`https://YOUR-USERNAME.github.io/wc2026-wallchart/`

---

## ✨ Features
- Auto-syncs live scores every 60 seconds
- 4-source fallback chain — if one fails, tries the next instantly
- All 12 groups with live standings
- TV-style left/right knockout bracket
- Click any score or team to edit manually
- Saves to browser storage automatically
- Mobile friendly

## 📁 Files
```
index.html          ← Entire wall chart (single file)
scores.json         ← Auto-updated by GitHub Actions every 5 min
README.md
.github/workflows/pages.yml   ← Fetches scores + deploys
```
