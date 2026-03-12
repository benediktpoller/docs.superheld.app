# Test Execution Guide

## Quick Start

```bash
# 1. Umgebung vorbereiten
source .venv/bin/activate
pip install -r tests/requirements.txt -q

# 2. Hugo Server start in einem anderen Terminal
cd hugo-site && hugo server --buildDrafts

# 3. Tests ausführen
cd ..
python -m pytest tests/test_wcag_aaa.py -v
```

## Detaillierte Schritte

### Schritt 1: Python Environment

```bash
# Falls noch nicht vorhanden:
python3 -m venv .venv

# Aktivieren
source .venv/bin/activate

# Dependencies installieren
pip install -r tests/requirements.txt
```

### Schritt 2: Hugo Server

Der Test-Suite braucht einen laufenden Hugo Server auf `http://localhost:1313`:

```bash
cd hugo-site
hugo server --buildDrafts
# Output sollte sein:
# Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
```

### Schritt 3: Tests Ausführen

```bash
# Alle Tests
python -m pytest tests/test_wcag_aaa.py -v

# Nur WCAG AAA Tests
python -m pytest tests/test_wcag_aaa.py::TestWCAGAAA -v

# Spezifischer Test
python -m pytest tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility -v

# Mit detailliertem Output
python -m pytest tests/test_wcag_aaa.py -vv --tb=long
```

## Expected Output

✅ Erfolgreiche Test-Laufzeit sollte zeigen:

```
============================= test session starts ==============================
collected 8 items

tests/test_wcag_aaa.py::TestWCAGAAA::test_hugo_server_running PASSED     [ 12%]
tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility[/] PASSED   [ 25%]
tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility[/configuration/] PASSED [ 37%]
tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility[/installation/] PASSED [ 50%]
tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility[/usage/] PASSED [ 62%]
tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility[/faq/] PASSED [ 75%]
tests/test_wcag_aaa.py::TestWCAGAAA::test_page_accessibility[/screenshots/] PASSED [ 87%]
tests/test_wcag_aaa.py::TestWCAGAAA::test_all_pages_have_proper_structure PASSED [100%]

============================== 8 passed in 0.13s ===============================
```

## Troubleshooting

### ❌ `connection refused` Error

**Problem:** `ConnectionRefusedError: [Errno 61] Connection refused`

**Lösung:**
```bash
# Überprüfe ob Hugo läuft
curl http://localhost:1313

# Falls nicht:
cd hugo-site
hugo server --buildDrafts
```

### ❌ `ModuleNotFoundError: No module named 'pytest'`

**Problem:** pytest nicht installiert

**Lösung:**
```bash
source .venv/bin/activate
pip install -r tests/requirements.txt
```

### ❌ Hugo theme not found

**Problem:** `Error: error building site: theme not found`

**Lösung:**
```bash
cd hugo-site
git clone --depth 1 https://github.com/McShelby/hugo-theme-relearn.git themes/relearn
cd ..
```

### ❌ Hugo build errors

**Problem:** `ERROR error building site:`

**Lösung:**
```bash
cd hugo-site
hugo --minify  # Siehe detaillierte Error Messages
```

## GitHub Actions Simulation

Die komplette Workflow-Simulation lokal:

```bash
./validate-workflow.sh
```

Dies führt durch:
1. Hugo Build
2. Python Dependencies
3. Hugo Server Start
4. WCAG AAA Tests

## Test Coverage

Überprüfte Bereiche:

| Category | Tests | Details |
|----------|-------|---------|
| Page Loading | 7 | Homepage + 6 Content-Seiten |
| Accessibility | 8 | WCAG 2.1 AAA Richtlinien |
| Structure | 1 | Landmarks, Headings, etc. |
| **Total** | **8** | **Vollständige Validation** |

## Performance

Typische Laufzeiten:

| Schritt | Dauer |
|---------|-------|
| Hugo Build | ~100ms |
| Server Start | ~3 sec |
| 8 Tests | ~0.2 sec |
| **Gesamt** | **~3.5 sec** |

## Continuous Testing

Während der Entwicklung:

```bash
# Watch mode (neustart bei Datei-Änderungen)
python -m pytest tests/test_wcag_aaa.py -v --watch
```

## Integration mit Git

Before commit:

```bash
# Validiere alles
./validate-workflow.sh

# Falls erfolgreich: commit & push
git add .
git commit -m "..."
git push  # Triggert GitHub Actions automatisch!
```

---

**Last Updated:** 12. März 2026  
**Test Framework:** pytest 7.4.3  
**Python:** 3.11.x
