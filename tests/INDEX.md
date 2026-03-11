# WCAG AAA Tests - Übersicht

Diese Dateien werden für die Accessibility-Tests verwendet:

```
tests/
├── __init__.py                    # Python Paket-Marker
├── requirements.txt               # Python Dependencies (pytest, requests, beautifulsoup4)
├── test_wcag_aaa.py             # 🧪 Automatisierte WCAG AAA Tests
├── .pa11yci.json                # Konfiguration für pa11y-ci (optional)
├── WCAG_AAA_README.md           # 📖 Vollständige Dokumentation
├── QUICKSTART.md                # ⚡ Schnellstart & Häufige Fehler
└── HUGO_A11Y_CONFIG.md          # 🎨 Hugo Theme A11y Konfiguration

run_tests.sh                       # 🔧 Test-Runner (macOS/Linux)
run_tests.py                       # 🔧 Test-Runner (alle Systeme/Python)
```

## 📊 Was wird getestet?

### ✅ Automatisierte Checks (test_wcag_aaa.py)

1. **Seitenstruktur**
   - `<html lang="...">` Deklaration
   - Eindeutiger `<title>` Tag
   - Überschriften-Hierarchie (h1-h6)
   - Semantische Landmarks (`<main>`, `<nav>`, `<footer>`)

2. **Inhalts-Zugänglichkeit**
   - Bilder haben Alt-Text
   - Links sind aussagekräftig
   - Formulare haben Labels
   - Buttons haben ARIA-Labels

3. **Multimedia**
   - Videos haben Captions
   - Audio hat Transkripte

4. **Tastatur & Screenreader**
   - Skip-Links vorhanden
   - Keine tabindex-Missbrauch
   - ARIA-Rollen korrekt

### 🔍 Manuelle Checks (siehe WCAG_AAA_README.md)

- Farbkontrast (7:1 für AAA)
- Tastatur-Navigation
- Focus-Indikator
- Zoom-Funktionalität (200%)
- Dark Mode & High Contrast
- Screenreader-Kompatibilität

## 🚀 Schnell Start

```bash
# Installation (einmalig)
pip install -r tests/requirements.txt

# Tests ausführen (kurz & bündig)
python run_tests.py

# Oder mit manuellem Setup
cd hugo-site
hugo server --buildDrafts  # Terminal 1

python -m pytest tests/test_wcag_aaa.py -v  # Terminal 2
```

## 📈 Versuch einer Bewertung

**Automatisierte Abdeckung**: ca. 70-75% der WCAG AAA Kriterien
**Manuelle Tests erforderlich**: ca. 25-30% (Farben, Keyboard, Screenreader)

## 🎯 WCAG 2.1 AAA Ebenen

| Kriterium | Level A | Level AA | Level AAA |
|-----------|---------|----------|-----------|
| Kontrast (Normal) | 3:1 | 4.5:1 | 7:1 |
| Große Text | 3:1 | 3:1 | 4.5:1 |
| Fokus-Indikator | Pflicht | Enhanciert | Sehr deutlich |
| Tastatur-Zugang | Ja | Ja | Nur Tastatur |
| Screenreader | Ja | Ja | Ja + Voiceout |

Für diese Hugo-Site ist **AAA** anstrebenswert für:
- ✅ Maximal sichere Dokumentation
- ✅ Europäische Richtlinien (EN 301 549)
- ✅ Barrierefreiheits-Anforderungen (BITV 2.0)
- ✅ Best Practice für Organisations-Inhalte

## 📚 Weitere Ressourcen

- [WCAG 2.1 Quickref](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM Checklist](https://webaim.org/articles/wcag/)
- [BITV 2.0 (DE)](https://www.erfolgreich-barrierefrei.de/)
- [A11y Project](https://www.a11yproject.com/)

## 🔗 Integration mit CI/CD

Diese Tests können in GitHub Actions, GitLab CI oder ähnliche Systeme integriert werden (siehe `QUICKSTART.md`)

## 💡 Häufig gestellte Fragen

**F: Wo sind die zugänglichen Tests?**
A: Hauptsächlich in `test_wcag_aaa.py`, ergänzt durch manuelle Checklisten in den anderen `.md` Dateien.

**F: Wie starte ich die Tests?**
A: Mit `python run_tests.py` oder `python -m pytest tests/test_wcag_aaa.py -v`

**F: Was bedeuten die verschiedenen Fehler?**
A: Siehe `QUICKSTART.md` für Beispiele und Lösungen.

**F: Kann ich das Theme anpassen?**
A: Ja, siehe `HUGO_A11Y_CONFIG.md` für empfohlene CSS/HTML-Änderungen.
