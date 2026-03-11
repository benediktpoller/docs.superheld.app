# WCAG AAA Hugo-Konfiguration

Diese Datei enthält Best Practices für die `hugo-site/hugo.toml` Konfiguration, um WCAG AAA Konformität zu erreichen.

## Hugo.toml für Accessibility

```toml
baseURL = "https://docs.superheld.app/"
title = "superheld.app - Schutzmittel gegen AI"
theme = "hugo-book"
languageCode = "de"
defaultContentLanguage = "de"

# HTML Output
[outputs]
  home = ["HTML", "JSON"]  # JSON für Suche

# Markup Settings für A11y
[markup]
  [markup.tableOfContents]
    startLevel = 2
    endLevel = 3
  
  [markup.highlight]
    style = "monokai"
    lineNos = true
    lineNumbersInTable = false

# Params für Theme-Anpassungen
[params]
  # Accessibility
  docTitle = "superheld.app Dokumentation"
  skipLink = true
  focusOutlineVisible = true
  contrastMode = "normal"  # oder "high" für WCAG AAA
  
  # Schriftgröße und Lesbarkeit
  fontSizeAdjustable = true
  lineHeight = 1.6
  letterSpacing = 0.02  # leicht erhöhter Zeichenabstand
  
  # Farben mit hohem Kontrast (WCAG AAA: 7:1 Ratio)
  themeColor = "#000000"  # Schwarz
  backgroundColor = "#FFFFFF"  # Weiß
  accentColor = "#0052CC"  # Schönes Blau mit guter Lesbarkeit
  
  # Navigation
  enableTOC = true
  enableBreadcrumb = true
  enableLanguageDropdown = true
  
  # Search
  enableSearch = true
  enableSearchHighlight = true
  
  # Code Blocks
  enableCodeCopy = true
  enableLang = true
  highlightColor = "#FFF3CD"  # Hoher Kontrast für Highlights
  
  # Weitere A11y Settings
  enableSmartQuotes = true
  enableFootnotes = true
  enableSpaceAfterHeading = true
```

## Hugo-Theme Anpassungen für A11y

### 1. Header/Navigation (`layouts/head.html`)

```html
<head>
  <!-- Essential Meta Tags -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
  <meta name="description" content="{{ .Description | default .Site.Params.description }}">
  
  <!-- Language Declaration -->
  <meta http-equiv="content-language" content="{{ .Lang }}">
  
  <!-- WCAG AAA: High Contrast Support -->
  <link rel="stylesheet" media="(prefers-contrast: more)" href="/css/high-contrast.css">
  
  <!-- WCAG AAA: Reduced Motion Support -->
  <link rel="stylesheet" media="(prefers-reduced-motion: reduce)" href="/css/no-motion.css">
  
  <!-- WCAG AAA: Dark Mode Support -->
  <link rel="stylesheet" media="(prefers-color-scheme: dark)" href="/css/dark-mode.css">
  
  <!-- Semantic Title -->
  <title>{{ .Title }} | {{ .Site.Title }}</title>
</head>
```

### 2. Navigation mit Skip-Links (`layouts/partials/nav.html`)

```html
<!-- Skip to main content link (sichtbar bei Tab) -->
<a href="#main-content" class="skip-link">Zum Hauptinhalt springen</a>

<nav role="navigation" aria-label="Main navigation">
  {{ range .Site.Menus.main }}
    <a href="{{ .URL }}" 
       aria-current="{{ if .URL | strings.HasPrefix .Site.BaseURL }}page{{ end }}">
      {{ .Name }}
    </a>
  {{ end }}
</nav>

<style>
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: #000;
    color: #fff;
    padding: 8px;
    text-decoration: none;
    z-index: 100;
  }
  
  .skip-link:focus {
    top: 0;  /* Sichtbar bei Tab */
  }
</style>
```

### 3. Alt-Text für Bilder (`layouts/shortcodes/figure.html`)

```html
{{ if .Get "alt" }}
  {{ $alt := .Get "alt" }}
{{ else }}
  {{ $alt := or (.Get "title") (.Get "caption") }}
{{ end }}

<figure role="imggroup" aria-labelledby="caption-{{ .Get 0 | md5 }}">
  <img 
    src="{{ .Get 0 }}" 
    alt="{{ $alt }}"
    decoding="async"
    loading="lazy"
    {{ if .Get "width" }}width="{{ .Get "width" }}"{{ end }}
    {{ if .Get "height" }}height="{{ .Get "height" }}"{{ end }}>
  
  {{ if .Get "caption" }}
    <figcaption id="caption-{{ .Get 0 | md5 }}">
      {{ .Get "caption" | markdownify }}
    </figcaption>
  {{ end }}
</figure>
```

### 4. Code Blocks mit Syntax Highlighting

```html
{{ $language := .Type }}
<pre><code class="language-{{ $language }}" 
          aria-label="Code example in {{ $language }}">{{ .Inner }}</code></pre>
```

### 5. CSS für WCAG AAA Kompatibilität

Datei: `static/css/a11y-base.css`

```css
/* Basis Accessibility Styles */

:root {
  /* Farb-Palette mit AAA Kontrast (7:1 minimum) */
  --color-text: #000000;      /* Schwarz */
  --color-bg: #FFFFFF;         /* Weiß */
  --color-link: #0052CC;       /* Royal Blue */
  --color-link-visited: #5E35B1; /* Purple */
  --color-accent: #FF6B35;     /* Orange */
  --color-border: #CCCCCC;
  
  /* Typography für Lesbarkeit */
  --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  --font-mono: "Courier New", monospace;
  --line-height: 1.6;
  --letter-spacing: 0.02em;
}

/* Fokus-Indikator für Tastatur-Navigation */
:focus {
  outline: 3px solid var(--color-link);
  outline-offset: 2px;
}

/* Keine Outline auf Mouse-Click */
:focus:not(:focus-visible) {
  outline: none;
}

/* Text-Grundstil */
body {
  font-family: var(--font-base);
  font-size: 16px; /* 1em = 16px, keine 12px+ */
  line-height: var(--line-height);
  letter-spacing: var(--letter-spacing);
  color: var(--color-text);
  background: var(--color-bg);
}

/* Überschriften mit ausreichendem Spacing */
h1, h2, h3, h4, h5, h6 {
  margin-top: 1.5em;
  margin-bottom: 0.5em;
  font-weight: 600;
  line-height: 1.3;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }
h4 { font-size: 1.25rem; }
h5 { font-size: 1.1rem; }
h6 { font-size: 1rem; }

/* Links mit ausreichendem Kontrast */
a {
  color: var(--color-link);
  text-decoration: underline;
  text-decoration-thickness: 2px;
  text-underline-offset: 4px;
}

a:visited {
  color: var(--color-link-visited);
}

a:hover, a:focus {
  text-decoration-thickness: 3px;
}

/* Code Blocks mit hohem Kontrast */
code, pre {
  background: #F4F4F4;
  border: 1px solid var(--color-border);
  padding: 0.5em;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 0.95em;
}

/* Reduzierte Bewegung respektieren */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* High Contrast Mode */
@media (prefers-contrast: more) {
  :root {
    --color-text: #000000;
    --color-bg: #FFFFFF;
    --color-link: #000080; /* Navy für Maximum Kontrast */
    --color-border: #000000;
  }
}

/* Dark Mode */
@media (prefers-color-scheme: dark) {
  :root {
    --color-text: #FFFFFF;
    --color-bg: #121212;
    --color-link: #64B5F6; /* Blaues Hell */
    --color-border: #424242;
  }
}

/* Print Stylesheet */
@media print {
  a[href]:after {
    content: " (" attr(href) ")";
  }
  
  nav, [role="navigation"] {
    display: none;
  }
  
  body {
    background: white;
    color: black;
  }
}
```

## Checkliste für Hugo-Theme

- [ ] `hugo.toml` mit Accessibility-Parametern
- [ ] Skip-Links in Navigation
- [ ] `<html lang="...">` Tag korrekt
- [ ] Semantische HTML-Tags (`<main>`, `<nav>`, `<footer>`, `<article>`)
- [ ] Focus-Indikator visible
- [ ] AAA-Farb-Kontrast in CSS
- [ ] Lesbare Schriftgröße (mind. 16px base)
- [ ] Zeilenhöhe >= 1.5
- [ ] Responsive ohne Horizontal-Scroll
- [ ] Keyboard-Navigation vollständig
- [ ] Alle Bilder haben Alt-Text
- [ ] Videos haben Captions
- [ ] Formulare haben Labels
- [ ] Fehler werden klar angezeigt
- [ ] Reduzierte Bewegung wird respektiert
- [ ] High Contrast Mode wird unterstützt
- [ ] Dark Mode wird unterstützt

## Testing nach Änderungen

Nach jeder Theme-Änderung:

```bash
cd hugo-site
hugo server --buildDrafts

# In separatem Terminal:
python run_tests.py
```
