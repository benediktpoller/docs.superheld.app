# Schnellstart: WCAG AAA Tests

## 1️⃣ Installation (einmalig)

```bash
# Requirements installieren
pip install -r tests/requirements.txt
```

## 2️⃣ Tests ausführen

### Variante A: Automatisches Skript (einfach)

```bash
# macOS/Linux
bash run_tests.sh

# Windows/Alle Systeme
python run_tests.py
```

### Variante B: Manuell (für Debugging)

```bash
# Terminal 1: Hugo Server starten
cd hugo-site
hugo server --buildDrafts

# Terminal 2: Tests ausführen
python -m pytest tests/test_wcag_aaa.py -v

# Oder mit CLI Runner
python tests/test_wcag_aaa.py
```

## 3️⃣ Fehler beheben

Die Test-Ausgabe zeigt:
- 🔴 **FEHLER**: Muss vor Deployment behoben werden
- 🟡 **WARNUNG**: Sollte überprüft werden
- ℹ️ **INFO**: Benötigt manuelle Überprüfung

### Häufige Fehler und Lösungen

### ❌ Fehler: "Bild hat keinen Alt-Text"

**Problem:**
```html
<img src="screenshot.png">
```

**Lösung:**
```html
<img src="screenshot.png" alt="Screenshot der App-Einstellungen mit Suchleiste">
```

### ❌ Fehler: "Link hat keinen Text"

**Problem:**
```html
<a href="/docs">Click here</a>
```

**Lösung:**
```html
<a href="/docs">Dokumentation ansehen</a>
```

### ❌ Fehler: "Überschriften-Sprung von h1 zu h3"

**Problem:**
```html
<h1>Titel</h1>
<h3>Untertitel</h3>
```

**Lösung:**
```html
<h1>Titel</h1>
<h2>Untertitel</h2>
```

### ❌ Fehler: "Input hat kein zugeordnetes Label"

**Problem:**
```html
<input type="text" placeholder="Name">
```

**Lösung:**
```html
<label for="name-input">Name:</label>
<input type="text" id="name-input" placeholder="Name">
```

### ❌ Fehler: "Seite hat keine h1"

**Problem:**
```html
<h2>Willkommen</h2>
```

**Lösung:**
```html
<h1>Willkommen</h1>
```

## 📋 Manuelle Checkliste vor Deployment

- [ ] Alle automatisierten Tests grün
- [ ] Seite mit Tastatur navigierbar (Tab, Enter, Esc)
- [ ] Focus-Indikator sichtbar auf allen fokussierbaren Elementen
- [ ] Farbkontrast ausreichend (7:1 für AAA)
- [ ] Mit Screenreader testbar (VoiceOver/NVDA)
- [ ] Zoom auf 200% funktioniert
- [ ] Keine Fehler in Browser-Console
- [ ] Alle Bilder haben beschreibenden Alt-Text
- [ ] Videos haben Untertitel
- [ ] PDF-Dokumente sind accessible (falls vorhanden)

## 🔗 Nützliche Tools

### Im Browser
- **Chrome/Edge Lighthouse**: DevTools > Lighthouse > Accessibility
- **Firefox WAVE**: [webaim.org/articles/wave/](https://webaim.org/articles/wave/)
- **axe DevTools**: Browser Extension testen

### Screenreader testen
- **macOS**: VoiceOver (Cmd + F5)
- **Windows**: NVDA [nvaccess.org](https://www.nvaccess.org/)
- **Linux**: Orca

### Keyboard Navigation testen
```
Tab:         Nächstes Element
Shift+Tab:   Vorheriges Element
Enter:       Button/Link aktivieren
Space:       Checkbox/Radio/Button aktivieren
Esc:         Modal schließen
Arrow Keys:  In Menüs navigieren
```

## 📊 Test-Abdeckung

Aktuelle Test-Abdeckung für **WCAG 2.1 AAA**:

| Kriterium | Status | Note |
|-----------|--------|------|
| Seitenstruktur | ✅ Automatisiert | h1-h6, Landmarks |
| Bilder & Alt-Text | ✅ Automatisiert | |
| Link-Text | ✅ Automatisiert | |
| Formular-Labels | ✅ Automatisiert | |
| Farb-Kontrast | 🔍 Manuell | Benötigt Browser/Pixel-Analyse |
| Tastatur-Navigation | 🔍 Manuell | Benötigt Benutzerinteraktion |
| Screenreader | 🔍 Manuell | Spezifische Tools erforderlich |
| Video/Audio | ✅ Automatisiert | Captions & Transkripte |
| ARIA-Labels | ✅ Automatisiert | |

## ❓ FAQ

**F: Was ist WCAG AAA?**
A: Web Content Accessibility Guidelines Level AAA ist der höchste Accessibility-Standard. Empfohlen für Regierungen, Bildung, Gesundheit.

**F: Worin unterscheidet sich AAA von AA?**
A: AAA ist strenger (z.B. 7:1 Farbkontrast vs. 4.5:1 bei AA)

**F: Sind diese Tests ausreichend?**
A: Diese automatisierten Tests fangen ~70% auf. Manuelle Tests & Screenreader-Verifikation sind auch wichtig.

**F: Wie oft sollten Tests laufen?**
A: Mindestens nach jedem Commit. Ideal: In CI/CD Pipeline integriert.

## 🚀 Integration in CI/CD

### GitHub Actions Beispiel

```yaml
name: Accessibility Tests

on: [push, pull_request]

jobs:
  accessibility:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.11
      - name: Install dependencies
        run: pip install -r tests/requirements.txt
      - name: Run Hugo
        run: cd hugo-site && hugo &
      - name: Wait for server
        run: sleep 3
      - name: Run WCAG AAA tests
        run: python -m pytest tests/test_wcag_aaa.py -v
```

## 📞 Support

Fragen zu WCAG AAA?
- [W3C WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM](https://webaim.org/)
- [A11y Check](https://www.a11yproject.com/)
