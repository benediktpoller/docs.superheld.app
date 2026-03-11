# superheld.app Dokumentation

[![Tests](https://github.com/benediktpoller/docs.superheld.app/workflows/WCAG%20AAA%20Accessibility%20Tests/badge.svg)](https://github.com/benediktpoller/docs.superheld.app/actions)
[![Build](https://github.com/benediktpoller/docs.superheld.app/workflows/Build%20%26%20Deploy/badge.svg)](https://github.com/benediktpoller/docs.superheld.app/actions)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Offizielle End-User Dokumentation für **[superheld.app](https://superheld.app)** – dein Schutzmittel gegen KI und Datenverlust.

## 📖 Über diese Dokumentation

Diese Dokumentation wird mit **Hugo** statisch generiert und richtet sich an:
- 👥 **End-User** – Leicht verständliche Anleitung zur App-Nutzung
- 👨‍💻 **Entwickler** – Technische Details und API-Beschreibungen  
- ⚙️ **Administratoren** – Deployment und Konfiguration

**Status:** ✅ In Entwicklung | **Theme:** [hugo-book](https://github.com/alex-shpak/hugo-book) | **License:** MIT

---

## 🚀 Schnellstart

### Voraussetzungen
- **Hugo** (Extended) – [Installation](https://gohugo.io/installation/)
- **Python 3.9+** (für Tests) – [Installation](https://www.python.org/downloads/)
- **Git** – [Installation](https://git-scm.com/)

### Entwicklungsserver starten

```bash
# Option 1: Mit make (empfohlen)
make dev

# Option 2: Bash-Skript
bash dev-server.sh

# Option 3: Direkt
cd hugo-site && hugo server --buildDrafts --disableFastRender -O
```

Server läuft unter: **http://127.0.0.1:1313** (Browser öffnet sich automatisch)

---

## 📂 Projektstruktur

```
docs.superheld.app/
├── hugo-site/                    # Hugo Projekt
│   ├── hugo.toml                 # Konfiguration
│   ├── content/                  # Markdown-Seiten
│   │   ├── _index.md            # Startseite
│   │   ├── installation.md
│   │   ├── configuration.md
│   │   ├── usage.md
│   │   └── faq.md
│   ├── themes/hugo-book/         # Theme
│   └── public/                   # Build-Output
├── tests/                        # Accessibility Tests
│   ├── test_wcag_aaa.py         # WCAG 2.1 AAA Tests
│   └── requirements.txt
├── .github/workflows/            # GitHub Actions CI/CD
│   ├── accessibility.yml
│   ├── build-deploy.yml
│   └── validate.yml
├── Makefile                      # Entwickler-Commands
├── QUICKREF.md                   # Quick Reference
└── README.md                     # Diese Datei
```

---

## 🧪 Qualitätssicherung

### Lokale Tests

```bash
# WCAG AAA Accessibility Tests laufen
make test

# oder direkt
python run_tests.py
```

**Automatisierte Prüfungen:**
- ✅ WCAG 2.1 AAA Konformität (Seitenstruktur, Alt-Text, Labels)
- ✅ HTML-Validität
- ✅ Kaputte Links
- ✅ Markdown-Syntax

**Testdetails:** Siehe [tests/WCAG_AAA_README.md](tests/WCAG_AAA_README.md)

### GitHub Actions CI/CD

Automatische Tests & Deployment bei jedem Push:

| Workflow | Trigger | Aktion |
|----------|---------|--------|
| **accessibility.yml** | Push/PR | WCAG AAA Tests |
| **build-deploy.yml** | Push zu main | Build + Deploy zu Netlify |
| **validate.yml** | Wöchentlich | Links & HTML validieren |

**Details:** Siehe [.github/CI_CD_SETUP.md](.github/CI_CD_SETUP.md)

---

## 📝 Content bearbeiten

### Neue Seite erstellen

```bash
cd hugo-site
hugo new content/my-page.md
```

### Seite bearbeiten

1. Markdown-Datei in `hugo-site/content/` öffnen
2. Änderungen speichern
3. Browser aktualisiert sich automatisch (Live Reload)

### Best Practices für Content

- **Sprache:** Deutsch, klar und einfach
- **Zielgruppe:** End-User (technisch nicht versiert)
- **Struktur:** h1 → h2 → h3 (keine Sprünge)
- **Bilder:** Aussagekräftigen Alt-Text hinzufügen
- **Links:** Deskriptive Link-Texte verwenden

**Template:** `hugo-site/archetypes/default.md`

---

## 🎨 Theme & Customization

**Aktuelles Theme:** [hugo-book](https://github.com/alex-shpak/hugo-book)

### Konfiguration

- **Hugo-Config:** `hugo-site/hugo.toml`
- **Theme-Config:** `hugo-site/themes/hugo-book/`
- **CSS Customization:** `hugo-site/assets/_custom.scss`

### Accessibility (WCAG AAA)

Siehe [tests/HUGO_A11Y_CONFIG.md](tests/HUGO_A11Y_CONFIG.md) für:
- Farb-Kontrast Richtlinien
- Dark Mode / High Contrast Support
- Tastatur-Navigation
- Screenreader-Optimierung

---

## 🚀 Deployment

### Voraussetzungen

- GitHub Repository eingerichtet ✅
- (Optional) Netlify Account mit verbundener Site

### Automatisches Deployment (CI/CD)

```bash
# 1. Commit & Push zu main
git add .
git commit -m "feat: add new content"
git push origin main

# 2. GitHub Actions laufen automatisch
# → Tests durchgeführt
# → Zu Netlify deployed (falls konfiguriert)

# 3. Live! 🎉
```

### Manuelles Deployment

```bash
# Build for production
cd hugo-site
hugo --minify

# Ergebnis: hugo-site/public/
# Hochladen zu Netlify/GitHub Pages/eigenem Server
```

**Deployment-Details:** Siehe [.github/CI_CD_SETUP.md](.github/CI_CD_SETUP.md)

---

## 🔧 Entwickler-Commands

| Command | Beschreibung |
|---------|------------|
| `make dev` | Hugo Server starten (mit Browser) |
| `make test` | Tests laufen |
| `make build` | Hugo bauen |
| `make build-minify` | Minified Build for Production |
| `make clean` | Caches löschen |
| `make help` | Alle Commands anzeigen |

Oder siehe [QUICKREF.md](QUICKREF.md) für detaillierte Anleitung.

---

## 🤝 Contributing

### Bug Reports & Suggestions

Fehler gefunden? Feature-Idee?  
→ [Issues auf GitHub erstellen](https://github.com/benediktpoller/docs.superheld.app/issues/new)

### Code / Content Beiträge

```bash
# 1. Fork & Clone
git clone https://github.com/<dein-username>/docs.superheld.app.git
cd docs.superheld.app

# 2. Feature Branch erstellen
git checkout -b feat/my-feature

# 3. Lokal testen
make test

# 4. Commit & Push
git add .
git commit -m "feat: add awesome feature"
git push origin feat/my-feature

# 5. Pull Request auf GitHub erstellen
```

**Richtlinien:**
- Tests müssen bestanden (grün) sein
- Commit-Messages auf Deutsch/Englisch
- Alt-Text für alle Bilder
- WCAG AAA Konformität

---

## 📚 Dokumentation

| Datei | Inhalt |
|-------|--------|
| [QUICKREF.md](QUICKREF.md) | Schnelle Befehle & Shortcuts |
| [tests/QUICKSTART.md](tests/QUICKSTART.md) | Test-Anleitung mit Fehler-Lösungen |
| [tests/WCAG_AAA_README.md](tests/WCAG_AAA_README.md) | Accessibility Details |
| [.github/CI_CD_SETUP.md](.github/CI_CD_SETUP.md) | CI/CD Konfiguration |
| [tests/HUGO_A11Y_CONFIG.md](tests/HUGO_A11Y_CONFIG.md) | Theme Accessibility |

---

## 🔗 Links & Ressourcen

**Projekt:**
- 🌐 **Website:** [superheld.app](https://superheld.app)
- 📱 **GitHub:** [benediktpoller/docs.superheld.app](https://github.com/benediktpoller/docs.superheld.app)
- 🐛 **Issues:** [GitHub Issues](https://github.com/benediktpoller/docs.superheld.app/issues)

**Tools & Libraries:**
- 📘 [Hugo Dokumentation](https://gohugo.io/documentation/)
- 🎨 [hugo-book Theme](https://github.com/alex-shpak/hugo-book)
- ♿ [WCAG 2.1 Quickref](https://www.w3.org/WAI/WCAG21/quickref/)
- 📝 [Markdown Guide](https://www.markdownguide.org/)

---

## 📋 Checkliste für neue Features

Vor dem Merge in `main`:

- [ ] Content ist verständlich & korrekt (Grammatik)
- [ ] Hugo bauen funktioniert: `make build` ✅
- [ ] Tests bestanden: `make test` ✅
- [ ] Bilder haben Alt-Text
- [ ] Links funktionieren
- [ ] Keine Überschriften-Sprünge (h1 → h2 → h3)
- [ ] Lokal getestet unter http://127.0.0.1:1313
- [ ] Committed & gepusht

---

## 📄 Lizenz

MIT License – [LICENSE](LICENSE)

---

## ❓ Support & Questions

Fragen oder Hilfe benötigt?

1. **Dokumentation lesen:** Siehe [QUICKREF.md](QUICKREF.md)
2. **Tests prüfen:** Siehe [tests/QUICKSTART.md](tests/QUICKSTART.md#häufige-fehler-und-lösungen)
3. **Issue erstellen:** [GitHub Issues](https://github.com/benediktpoller/docs.superheld.app/issues)
4. **Kontakt:** superheld.app Team

---

**Happy documenting! 🎉**