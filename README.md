# 🏆 FIFA World Cup 2026 – Wall Chart

**➡ [Open Wall Chart](https://YOUR-USERNAME.github.io/wc2026-wallchart/)**

An interactive bracket and group-stage wall chart for the 2026 FIFA World Cup.

---

## How this works

There is no live score API. After investigating several "free" World Cup
score feeds, none of them are reliable, properly documented, or accessible
from a browser (CORS-blocked). Rather than show a fake "Live" indicator
that never actually connects, this wall chart uses **accurate static data
that gets updated by hand** each time results come in.

**To get fresh scores:** just ask in chat for an update and the data in
`index.html` will be refreshed with the latest confirmed results, then
re-deployed.

---

## ✨ Features

- 🏟 All 12 groups with full standings (MP, W, D, L, GF, GA, GD, PTS)
- 🏆 Full TV-style bracket — Round of 32 through the Final
- ✏️ Fully editable — click any score or team name to override
- 💾 Saves to your browser automatically (localStorage)
- 🖼 Real World Cup trophy image embedded directly in the page
- 📱 Mobile friendly

---

## 🚀 Deploy to GitHub Pages

### 1. Create a repository
Go to [github.com/new](https://github.com/new) → name it `wc2026-wallchart` →
**Public** → Create.

### 2. Upload files
Click **"uploading an existing file"**, drag in everything from this
package (including the hidden `.github` folder — press `Cmd+Shift+.` on
Mac to reveal it), then commit.

### 3. Enable Pages
Settings → Pages → Source: **GitHub Actions** → Save.

### 4. Done
Live in about a minute at:
```
https://YOUR-USERNAME.github.io/wc2026-wallchart/
```

---

## ⚠️ If you see "Invalid workflow file"

GitHub sometimes auto-creates a second workflow called `static.yml` when
Pages is first enabled. If you have both `static.yml` and `pages.yml` in
`.github/workflows/`, delete `static.yml` — only `pages.yml` is needed.

---

## 📁 Files

```
index.html   ← entire wall chart (single file, no dependencies)
README.md
.github/workflows/pages.yml   ← deploys to GitHub Pages on every push
```

## 📜 License
MIT — free to use, share, modify.
