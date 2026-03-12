# Workflow Validierung

## Status: ✅ READY

Dieser Guide erklärt, wie du die GitHub Actions Workflows lokal validierst.

## Lokal Testen

Führe das Validierungsskript aus:

```bash
./validate-workflow.sh
```

Das Skript simuliert alle GitHub Actions Workflows lokal und prüft:

1. **Hugo Build** - `hugo --minify` ohne Fehler
2. **Python Dependencies** - Alle Test-Abhängigkeiten installiert
3. **Hugo Server** - Server startet auf `http://localhost:1313`
4. **WCAG AAA Tests** - Alle 8 Accessibility Tests bestehen

## Workflow Überblick

### 1. Build & Deploy (`build-deploy.yml`)
- Hugo Extended installieren
- Hugo Site bauen mit `--minify`
- Zu Netlify deployen (optional, mit Secrets)

**Status lokal:** ✅ Baut erfolgreich

### 2. WCAG AAA Tests (`accessibility.yml`)
- Python 3.11 setup
- Dependencies installieren: `pip install -r tests/requirements.txt`
- Hugo Server starten
- WCAG AAA Tests ausführen: `pytest tests/test_wcag_aaa.py`

**Status lokal:** ✅ 8/8 Tests bestehen

### 3. Link & Content Validation (`validate.yml`)
- HTML / Link Validator
- Markdown Syntax Check
- Wöchentlicher Schedule

**Status lokal:** ✅ Validierung funktioniert

## Test-Details

### 8 WCAG AAA Tests werden überprüft:

| Test | Beschreibung | Status |
|------|-------------|--------|
| `test_hugo_server_running` | Hugo Server läuft auf Port 1313 | ✅ PASS |
| `test_page_accessibility[/]` | Homepage ist WCAG AAA konform | ✅ PASS |
| `test_page_accessibility[/configuration/]` | Config-Seite ist WCAG AAA konform | ✅ PASS |
| `test_page_accessibility[/installation/]` | Installation-Seite ist WCAG AAA konform | ✅ PASS |
| `test_page_accessibility[/usage/]` | Usage-Seite ist WCAG AAA konform | ✅ PASS |
| `test_page_accessibility[/faq/]` | FAQ-Seite ist WCAG AAA konform | ✅ PASS |
| `test_page_accessibility[/screenshots/]` | Screenshots-Seite ist WCAG AAA konform | ✅ PASS |
| `test_all_pages_have_proper_structure` | Alle Seiten haben korrekte Struktur | ✅ PASS |

### Geprüfte Accessibility-Richtlinien:

- ✅ HTML lang-Attribut
- ✅ Aussagekräftige Seitentitel
- ✅ Überschriften-Hierarchie (h1-h6)
- ✅ Bilder mit Alt-Text
- ✅ Links mit aussagekräftigem Text
- ✅ Formulare mit Labels
- ✅ Farb-Kontrast (Warnung für manuelle Überprüfung)
- ✅ Lesbarkeit des Textes
- ✅ Tastatur-Navigation
- ✅ Seitenstruktur mit Landmarks (main, nav, footer)
- ✅ ARIA Labels für Buttons
- ✅ Video/Audio mit Captions

## Lokale Fehlerbehebung

### Hugo Build fehlgeschlagen?

```bash
cd hugo-site
hugo --minify
```

Häufige Probleme:
- **Theme nicht gefunden:** `git clone --depth 1 https://github.com/McShelby/hugo-theme-relearn.git themes/relearn`
- **Deprecated Config:** Siehe `hugo.toml` deprecation warnings

### Tests fehlgeschlagen?

```bash
source .venv/bin/activate
pip install -r tests/requirements.txt
python -m pytest tests/test_wcag_aaa.py -v
```

Häufige Probleme:
- **Hugo Server nicht erreichbar:** `hugo server -s hugo-site --buildDrafts` in anderem Terminal starten
- **Module nicht installiert:** `pip install pytest beautifulsoup4 requests`

### Hugo Server startet nicht?

```bash
# Alte Prozesse killen
pkill -f "hugo server"

# Neu starten
cd hugo-site
hugo server --buildDrafts
```

## Continuous Integration

Nach Push zu `main` werden automatisch alle Tests ausgeführt:

1. **GitHub Actions startet automatisch**
2. **Alle Workflows durchlaufen parallel**
3. **Status Badges im README** zeigen Ergebnis

Status Badges:
- ![WCAG AAA Tests](https://github.com/benediktpoller/docs.superheld.app/actions/workflows/accessibility.yml/badge.svg)
- ![Build & Deploy](https://github.com/benediktpoller/docs.superheld.app/actions/workflows/build-deploy.yml/badge.svg)
- ![Link Validation](https://github.com/benediktpoller/docs.superheld.app/actions/workflows/validate.yml/badge.svg)

## Änderungen pushen

Nach jeder Änderung:

```bash
# 1. Lokal validieren
./validate-workflow.sh

# 2. Commits machen
git add .
git commit -m "..."

# 3. Pushen (triggert GitHub Actions automatisch!)
git push
```

## FAQ

**F: Warum brauche ich den Hugo Server für Tests?**  
A: Die Tests laden die aktuelle Seite live über HTTP und überprüfen HTML/Accessibility. Der Server muss laufen.

**F: Kann ich nur einen Test ausführen?**  
A: Ja: `pytest tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility -k "/configuration/"`

**F: Warum gibt es Warnungen in Hugo?**  
A: Einige Theme-Konfigurationen sind deprecated (z.B. `params.author`). Diese sind nicht kritisch.

---

**Last Updated:** 12. März 2026  
**Tests Status:** ✅ All Green
