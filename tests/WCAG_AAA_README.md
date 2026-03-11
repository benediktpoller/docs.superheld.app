# WCAG AAA Accessibility Test Suite

Diese Test-Suite überprüft die hugo-site Dokumentation auf Konformität mit **WCAG 2.1 AAA** (Web Content Accessibility Guidelines - Level AAA, der höchste Standard).

## Automatisierte Tests

### Installation

```bash
# Abhängigkeiten installieren
pip install -r tests/requirements.txt
```

### Tests ausführen

```bash
# Hugo Server starten (in separatem Terminal)
cd hugo-site
hugo server --buildDrafts

# In anderm Terminal: Tests ausführen
pytest tests/test_wcag_aaa.py -v

# Oder mit CLI Runner:
python tests/test_wcag_aaa.py
```

## Was wird getestet?

### ✅ Automatische Checks

- **Seitensprache**: `<html lang="...">` ist definiert
- **Seitentitel**: Aussagekräftiger, eindeutiger `<title>`
- **Überschriften-Hierarchie**: Keine Sprünge (h1 > h2 > h3 etc)
- **Bild Alt-Text**: Alle Bilder haben beschreibenden Alt-Text
- **Link-Text**: Links sind nicht generisch ("hier klicken")
- **Formular-Labels**: Alle Inputs haben zugeordnete `<label>`
- **Seiten-Landmarks**: `<main>`, `<nav>`, `<footer>` vorhanden
- **ARIA-Labels**: Icons und Buttons sind beschriftet
- **Video/Audio**: Captions und Transkripte vorhanden

### 🔍 Manuelle Checks

Die folgenden Punkte erfordern manuelle Überprüfung:

- [ ] **Farbkontrast**: Text vs. Hintergrund (AAA: min 7:1)
- [ ] **Tastatur-Navigation**: Seite funktioniert komplett ohne Maus
- [ ] **Focus-Indikator**: Sichtbar, wo man sich befindet (auf interaktiven Elementen)
- [ ] **Zoom**: Seite funktioniert mit 200% Zoom
- [ ] **Reader-Mode**: Safari/Firefox Reader-Modus funktioniert
- [ ] **Screenreader**: VoiceOver/NVDA kann alles vorlesen
- [ ] **Tab-Reihenfolge**: Tab-Reihenfolge ist logisch
- [ ] **Animationen**: Keine Blitzeffekte (< 3 Hz)
- [ ] **PDF/Dokumente**: Falls vorhanden - sind sie accessible?
- [ ] **Video**: Mit Untertiteln und Audio-Deskription
- [ ] **Fehlerbehandlung**: Fehler werden klar eingegeben
- [ ] **Zeitvorgaben**: Keine erzwungenen Zeitlimits

## WCAG AAA Checkliste für diese Site

### Wahrnehmbarkeit (Perceivable)

- [ ] **1.1.1 Non-text Content (Level A)**: Alle Nicht-Text-Inhalte haben Alternativen
- [ ] **1.3.1 Info and Relationships (Level A)**: Struktur ist semantisch korrekt
- [ ] **1.3.2 Meaningful Sequence (Level A)**: Lesereiefolge ist sinnvoll
- [ ] **1.4.3 Contrast (Minimum) (Level A)**: Mindest-Kontrast 4.5:1
- [ ] **1.4.4 Resize Text (Level AA)**: Text kann auf 200% gezoomt werden
- [ ] **1.4.11 Non-text Contrast (Level AA)**: Kontrast auch bei UI-Elementen
- [ ] **1.4.6 Contrast (Enhanced) (Level AAA)**: Erweiterter Kontrast 7:1
- [ ] **1.4.8 Visual Presentation (Level AAA)**: Text-Hintergrund, Zeilenhöhe angepasst

### Bedienbarkeit (Operable)

- [ ] **2.1.1 Keyboard (Level A)**: Alles ist per Tastatur zugänglich
- [ ] **2.1.2 No Keyboard Trap (Level A)**: Kein Element fängt den Focus ein
- [ ] **2.1.3 Keyboard (No Exception) (Level AAA)**: Nur Tastatur-Zugang
- [ ] **2.2.1 Timing Adjustable (Level A)**: Keine erzwungenen Zeitlimits
- [ ] **2.3.1 Three Flashes (Level A)**: Keine blitzenden Inhalte (< 3x pro Sekunde)
- [ ] **2.3.3 Animation from Interactions (Level AAA)**: Bewegungen können deaktiviert werden
- [ ] **2.4.1 Bypass Blocks (Level A)**: Skip-Links zu Hauptinhalten
- [ ] **2.4.3 Focus Order (Level A)**: Focus-Reihenfolge ist logisch
- [ ] **2.4.7 Focus Visible (Level AA)**: Focus-Indikator ist sichtbar
- [ ] **2.4.8 Focus Visible (Enhanced) (Level AAA)**: Fokus gut sichtbar

### Verständlichkeit (Understandable)

- [ ] **3.1.1 Language of Page (Level A)**: Seitensprache ist definiert
- [ ] **3.1.2 Language of Parts (Level AA)**: Sprachliche Abschnitte sind markiert
- [ ] **3.2.1 On Focus (Level A)**: Fokus-Änderungen lösen keine unerwarteten Aktionen aus
- [ ] **3.2.2 On Input (Level A)**: Eingaben lösen keine unerwarteten Kontextänderungen aus
- [ ] **3.3.1 Error Identification (Level A)**: Fehler werden identifiziert
- [ ] **3.3.3 Error Suggestion (Level AA)**: Fehlersuggestions werden angeboten
- [ ] **3.3.4 Error Prevention (Level AA)**: Kritische Änderungen können verhindert werden
- [ ] **3.3.5 Help (Level AAA)**: Kontext-Hilfe ist vorhanden

### Robustheit (Robust)

- [ ] **4.1.1 Parsing (Level A)**: HTML ist valide
- [ ] **4.1.2 Name, Role, Value (Level A)**: ARIA-Rollen sind korrekt
- [ ] **4.1.3 Status Messages (Level AA)**: Dynamische Status-Meldungen sind accessible

## Tools für erweiterte Tests

### Browser DevTools
- Chrome/Edge DevTools > Lighthouse > Accessibility
- Firefox: WAVE Browser Extension

### Kommandozeilen-Tools
```bash
# Pa11y Installation (Node.js erforderlich)
npm install -g pa11y-ci

# Tests durchführen
pa11y-ci --config .pa11yci.json
```

### Online-Validator
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)

## Anmerkungen für Hugo-Theme

Das verwendete Theme **hugo-book** sollte bereits ein modernes, accessibility-freundliches Design haben. Achte darauf:

1. **Custom CSS**: Nicht zu klein Schrift, hoher Kontrast
2. **Code Blocks**: Haben genug Kontrast
3. **Navigation**: Skip-Links vorhanden
4. **Bilder**: Alt-Text in allen Screenshots
5. **Links**: Nicht nur Farbe zur Unterscheidung nutzen

## Referenzen

- [W3C WCAG 2.1 Dokumentation](https://www.w3.org/WAI/WCAG21/quickref/)
- [WebAIM - Web Accessibility In Mind](https://webaim.org/)
- [Barrierefreie Digitale Welt - Bund](https://www.erfolgreich-barrierefrei.de/)
