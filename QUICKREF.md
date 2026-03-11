# Entwickler Quick Reference

Schnelle Befehle und Shortcuts für die superheld.app Dokumentation

## 🚀 Server starten

### Einfach (empfohlen)

```bash
# macOS/Linux
bash dev-server.sh

# Windows/Alle Systeme
python dev-server.py

# Manuell (von überall)
cd hugo-site
hugo server --buildDrafts --disableFastRender -O
```

**Ergebnis:** Browser öffnet sich automatisch auf `http://127.0.0.1:1313`

## 🧪 Tests ausführen

```bash
# WCAG AAA Accessibility Tests
python run_tests.py

# Oder
python -m pytest tests/test_wcag_aaa.py -v

# Mit detailliertem Output
python tests/test_wcag_aaa.py
```

## 📝 Content Workflow

```bash
# Neue Seite erstellen
cd hugo-site
hugo new content/my-page.md

# Hugo wird automatisch geöffnet und die Änderungen sind live sichtbar
```

## 🔧 Git Workflow

```bash
# Feature Branch erstellen
git checkout -b feat/new-feature

# Änderungen testen
python run_tests.py  # Muss grün sein!

# Committen
git add .
git commit -m "feat: add new feature"

# Pushen → GitHub Actions laufen automatisch
git push -u origin feat/new-feature

# Pull Request erstellen auf GitHub
```

## 📊 Häufige Kommandos

| Task | Kommando |
|------|----------|
| Server starten | `bash dev-server.sh` |
| Tests lokal | `python run_tests.py` |
| Hugo bauen | `cd hugo-site && hugo` |
| Minified bauen | `cd hugo-site && hugo --minify` |
| Draft-Seite sehen | `hugo server --buildDrafts` |
| Mit Memory-Render | `hugo server -M` |
| Bestimmter Port | `hugo server -p 8000` |

## 🎯 Tipps

### Live Reload deaktivieren
```bash
hugo server --disableLiveReload
```

### Memory-Render (schneller für große Sites)
```bash
hugo server -M --disableFastRender
```

### Im Hintergrund laufen
```bash
# macOS/Linux
bash dev-server.sh &
# Später stoppen: kill %1

# Mit nohup (bleibt auch nach Terminal-Close aktiv)
nohup bash dev-server.sh > hugo.log 2>&1 &
```

### Performance-Profiling
```bash
cd hugo-site
hugo server --pprof
# Öffne http://localhost:6060/debug/pprof/
```

## 📁 Wichtigste Verzeichnisse

```
docs.superheld.app/
├── hugo-site/                     # Hugo Projekt
│   ├── hugo.toml                  # Konfiguration
│   ├── content/                   # Markdown-Seiten
│   │   ├── _index.md             # Startseite
│   │   ├── configuration.md
│   │   ├── installation.md
│   │   └── ...
│   ├── themes/hugo-book/         # Theme
│   └── public/                    # Build-Output
├── tests/                         # Test-Suite
│   └── test_wcag_aaa.py          # Accessibility Tests
├── .github/workflows/             # CI/CD
│   ├── accessibility.yml
│   ├── build-deploy.yml
│   └── validate.yml
├── dev-server.sh                  # Server Starter
├── run_tests.sh                   # Test Runner
└── run_tests.py
```

## 🔗 Wichtige Links

- [Hugo Dokumentation](https://gohugo.io/documentation/)
- [Hugo-Book Theme](https://github.com/alex-shpak/hugo-book)
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [Markdown Syntax](https://www.markdownguide.org/)

## 🐛 Problemlösung

### "Hugo server works but files don't update"
```bash
# Clear cache
rm -rf hugo-site/resources/
# Restart server
bash dev-server.sh
```

### "Theme not showing correctly"
```bash
cd hugo-site
hugo config mounts  # Prüfe Theme-Mounting
git submodule update --init --recursive  # Update Submodules
```

### "Tests crashen"
```bash
# Python deps updaten
pip install -r tests/requirements.txt --upgrade
# Hugo Server läuft noch?
lsof -i :1313  # Zeige Prozesse auf Port 1313
```

## ✅ Checkliste vor Deployment

- [ ] `python run_tests.py` ✅ (alle Tests grün)
- [ ] `cd hugo-site && hugo --minify` ✅ (keine Fehler)
- [ ] Links funktionieren (`http://127.0.0.1:1313`)
- [ ] Screenshot-Placeholder sind ersetzt
- [ ] Alt-Text bei allen Bildern
- [ ] Alle Seiten erreichbar
- [ ] Git changes committed
- [ ] Zu main gepusht → GitHub Actions laufen

