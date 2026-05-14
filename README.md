# Mukesh Singh — Portfolio

My personal portfolio built with **MkDocs + Material theme**, hosted free on **GitHub Pages**.

🌐 **Live site:** https://Mukesh29s.github.io/portfolio

---

## 🚀 How to Set Up (First Time Only)

### Step 1 — Install Python
Make sure Python is installed. Check by opening your terminal and typing:
```bash
python --version
```
If you see a version number, you're good. If not, download Python from https://python.org

---

### Step 2 — Clone this repo to your computer
```bash
git clone https://github.com/Mukesh29s/portfolio.git
cd portfolio
```

---

### Step 3 — Install the tools
```bash
pip install mkdocs mkdocs-material ghp-import
```
This installs three things:
- `mkdocs` — the tool that builds your site
- `mkdocs-material` — the beautiful theme
- `ghp-import` — the tool that pushes to GitHub Pages

---

### Step 4 — Preview your site locally
```bash
mkdocs serve
```
Then open your browser and go to: **http://localhost:8000**

You'll see your portfolio exactly as it will look online. 
Press `Ctrl+C` to stop the preview.

---

### Step 5 — Deploy to GitHub Pages
```bash
python deploy.py
```
That's it! Your site will be live at: **https://Mukesh29s.github.io/portfolio**

---

## ✏️ How to Make Changes

1. Edit any `.md` file in the `docs/` folder
2. Preview with `mkdocs serve`
3. When happy, run `python deploy.py` to publish

### Folder structure
```
portfolio/
│
├── deploy.py           ← Run this to publish your site
├── mkdocs.yml          ← Site settings and navigation
│
└── docs/
    ├── index.md              ← Home page
    ├── certifications.md     ← Certifications page
    ├── contact.md            ← Contact page
    │
    ├── experience/
    │   └── index.md          ← Work experience
    │
    ├── projects/
    │   ├── index.md                  ← Projects overview
    │   ├── aws-dms-migration.md      ← Project 1
    │   ├── monitoring.md             ← Project 2
    │   └── zero-etl-redshift.md      ← Project 3
    │
    └── stylesheets/
        └── extra.css         ← Custom styles
```

---

## 📦 Tech Stack

| Tool | Purpose | Cost |
|------|---------|------|
| MkDocs | Site generator | Free |
| Material theme | Beautiful design | Free |
| GitHub Pages | Hosting | Free |
| Python | Deploy script | Free |

**Total cost: £0 / $0 / €0**
