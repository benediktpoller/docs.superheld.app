# CI/CD Setup Anleitung

Deine GitHub Actions Workflows sind konfiguriert und laufen automatisch. Hier ist, was du wissen musst:

## 🚀 Automatische Workflows

### 1. **accessibility.yml** - WCAG AAA Tests
- ✅ Läuft bei jedem **Push** und **Pull Request**
- ✅ Testet alle Seiten auf WCAG AAA Konformität
- ✅ Startet Hugo Server automatisch
- ✅ Kommentiert PR mit Ergebnissen

**Branches:** `main`, `develop`, `master`

### 2. **build-deploy.yml** - Build & Deploy
- ✅ Baut Hugo-Site
- ✅ Führt WCAG Tests durch
- ✅ Deployed zu **Netlify** (bei Push zu `main`)
- ✅ Gibt Feedback in PRs

**Deployment zu Netlify:** Benötigt Secrets (siehe unten)

### 3. **validate.yml** - Link & Content Checks
- ✅ Überprüft HTML-Validität
- ✅ Prüft auf kaputte Links
- ✅ Kontrolliert Markdown-Syntax
- ✅ Läuft wöchentlich + bei Änderungen

## 🔧 Setup erforderlich

### Ohne Netlify Deploy (einfach)
Die Accessibility und Build Workflows laufen automatisch ohne zusätzliche Konfiguration!

### Mit Netlify Deploy (empfohlen)
Füge diese Secretes in GitHub hinzu:

**In GitHub:**
1. Gehe zu: **Settings** → **Secrets and variables** → **Actions**
2. Erstelle neue Secrets:
   - `NETLIFY_SITE_ID`: Deine Netlify Site ID
   - `NETLIFY_AUTH_TOKEN`: Dein Netlify Personal Access Token

**Netlify Daten finden:**

**Netlify Site ID:**
```bash
# Auf Netlify Login
# Team Overview → Wähle Site → Settings → General → Site information → Site ID
```

Oder in `hugo-site/netlify.toml`:
```toml
[build]
  command = "hugo --minify"
  publish = "public"

[build.environment]
  HUGO_VERSION = "0.120"
```

**Netlify Auth Token:**
```bash
# User Menu → Account → Applications → New access token
# Name: GitHub CI/CD
# Scope: full
```

## 📊 GitHub Actions Status

**Status Badge für README.md:**

```markdown
![WCAG AAA Tests](https://github.com/YOUR_USERNAME/docs.superheld.app/workflows/WCAG%20AAA%20Accessibility%20Tests/badge.svg)
![Build & Deploy](https://github.com/YOUR_USERNAME/docs.superheld.app/workflows/Build%20%26%20Deploy%20Hugo%20Site/badge.svg)
```

## 🔍 Workflows überwachen

1. **GitHub Repository öffnen**
2. **Actions** Tab klicken
3. Letzten Run auswählen

Jeder Workflow zeigt:
- ✅ Tests bestanden / ❌ Fehler
- 📊 Dauer
- 📝 Logs
- 🎨 Artefakte

## 📈 Workflow-Ausgabe verstehen

### ✅ Erfolgreiche Accessibility Tests
```
✅ Run WCAG AAA Tests
- test_page_accessibility PASSED
- Seite / - OK
- Seite /configuration/ - OK
- Seite /installation/ - OK
```

### ❌ Fehlerhafte Tests
```
❌ Run WCAG AAA Tests
- test_page_accessibility FAILED
  FEHLER: Bild 'screenshot.png' hat keinen Alt-Text
  FEHLER: Link hat keinen Text
```

**Zu beheben:** Commit mit Fixes pushen → Workflow läuft automatisch neu

## 🔄 Manual Re-run

Tests können manuell neugestartet werden:

1. **Actions** → Workflow auswählen
2. **Run workflow** Button
3. **Use workflow from Branch (main)** → ▶️ **Run workflow**

## 📨 Notifikationen

GitHub benachrichtigt dich automatisch:
- ✅ Bei erfolgreichem Build
- ❌ Bei fehlgeschlagenen Tests
- 📬 Via Email oder GitHub Notifications

Um Notifikationen zu konfigurieren:
**GitHub Settings** → **Notifications** → **Actions**

## 🐛 Debugging bei Fehlern

### Tests schlagen fehl, aber lokal funktionieren?

```bash
# Baue genau wie CI/CD
cd hugo-site
hugo --minify

# Starte Server & führe Tests aus
hugo server --buildDrafts &
sleep 3
python -m pytest tests/test_wcag_aaa.py -v
```

### Logs einsehen

1. **Actions** → Workflow
2. **Run** auswählen
3. Job-Step expandieren
4. Logs durchsuchen (Strg+F)

### Common Issues

| Problem | Lösung |
|---------|--------|
| "Hugo command not found" | Workflow benutzt `peaceiris/actions-hugo@v2` |
| "Tests timeout" | Erhöhe `timeout` oder verwende `--buildDrafts` |
| "Netlify deploy fails" | Prüfe `NETLIFY_SITE_ID` und `NETLIFY_AUTH_TOKEN` |
| "Links broken" | Offline-Modus in `validate.yml` ist standardmäßig aktiv |

## 🎯 Best Practices

### 1. Feature Branches
```bash
git checkout -b feat/new-page
# ... Änderungen ...
git push -u origin feat/new-page
# → Pull Request erstellen
# → Workflows laufen automatisch
```

### 2. Vor lokalem Commit
```bash
# Lokal testen
python run_tests.py

# Nur committen wenn grün
git commit -m "Fix accessibility issues"
git push
```

### 3. Regelmäßige Checks
- Validate Workflow läuft wöchentlich (Sonntag, 00:00 UTC)
- Überprüft auch externe Links
- Findet neue Probleme früh

## 🚀 Deployment Workflow

```
[Commit to main]
        ↓
[GitHub Actions triggered]
        ↓
[✓ Build Hugo]
[✓ Run WCAG Tests]
[✓ Validate HTML/Links]
        ↓
[Deploy to Netlify] (nur main branch)
        ↓
[🎉 Live!]
```

## 📝 PRs mit Workflows

**Beispiel PR-Kommentar von Workflows:**
```
## 📋 Build Status
✅ Hugo site built successfully
✅ WCAG AAA tests passed
Preview: [Build artifacts](...)
```

## 🔗 Weitere Ressourcen

- [GitHub Actions Dokumentation](https://docs.github.com/en/actions)
- [Hugo Custom Actions](https://github.com/peaceiris/actions-hugo)
- [Netlify Deployment](https://www.netlify.com/blog/2016/10/18/how-our-build-bots-build-sites/)

## ✅ Checkliste zum Aktivieren

- [ ] Secrets für Netlify hinzugefügt (wenn Deploy gewünscht)
- [ ] `.github/workflows/*.yml` Dateien sind committed
- [ ] Push zu `main` → Workflows sollten laufen
- [ ] **Actions** Tab zeigt grüne Häkchen

Das war's! Deine Dokumentation wird nun automatisch getestet und deployed! 🎉

