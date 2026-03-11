# GitHub Actions Workflows

Automatisierte Tests und Deployment für superheld.app Dokumentation

## 📋 Übersicht

| Workflow | Trigger | Ziel |
|----------|---------|------|
| **accessibility.yml** | Push/PR auf main/develop/master | WCAG AAA Tests durchführen |
| **build-deploy.yml** | Push/PR auf main/master | Hugo bauen & zu Netlify deployen |
| **validate.yml** | Push/PR + wöchentlich | Links & HTML validieren |

## 🔧 Workflows

### accessibility.yml
```yaml
- Branches: main, develop, master
- Trigger: Push, Pull Request
- Dauer: ~2-3 Minuten

Steps:
1. Python 3.11 installieren
2. Test-Dependencies laden
3. Hugo Server starten
4. WCAG AAA Tests laufen
5. Ergebnisse hochladen
6. PR kommentieren (falls PR)
```

### build-deploy.yml
```yaml
- Branches: main, master
- Trigger: Push, Pull Request
- Deploy: Nur bei Push zu main

Steps:
1. Hugo bauen (--minify)
2. WCAG Tests
3. Zu Netlify deployen (bei main)
4. PR mit Status kommentieren
```

### validate.yml
```yaml
- Branches: main, develop, master
- Trigger: Push, PR + wöchentlich (Sonntag 00:00 UTC)
- Dauer: ~5 Minuten

Steps:
1. Hugo bauen
2. Broken links prüfen (offline)
3. HTML validieren
4. MarkdownChecken
5. Duplikate suchen
```

## 🚀 Start

1. **Secrets hinzufügen** (falls Netlify Deploy gewünscht):
   - `NETLIFY_SITE_ID`
   - `NETLIFY_AUTH_TOKEN`

2. **Commit & Push zu main**:
   ```bash
   git add .github/
   git commit -m "Add GitHub Actions CI/CD"
   git push origin main
   ```

3. **Actions Tab** öffnen → Workflows sollten laufen ✅

## 📊 Status-Badges

Füge diese zu `README.md` hinzu:

```markdown
## CI/CD Status

[![WCAG AAA Tests](https://github.com/<!-- USER -->/docs.superheld.app/workflows/WCAG%20AAA%20Accessibility%20Tests/badge.svg)](https://github.com/<!-- USER -->/docs.superheld.app/actions)
[![Build & Deploy](https://github.com/<!-- USER -->/docs.superheld.app/workflows/Build%20%26%20Deploy%20Hugo%20Site/badge.svg)](https://github.com/<!-- USER -->/docs.superheld.app/actions)
[![Link Validation](https://github.com/<!-- USER -->/docs.superheld.app/workflows/Link%20%26%20Content%20Validation/badge.svg)](https://github.com/<!-- USER -->/docs.superheld.app/actions)
```

## 🔍 Logs ansehen

1. **GitHub** → **Actions** 
2. Workflow auswählen
3. Run auswählen
4. Job expandieren → Logs sehen

## ❌ Fehlerbehebung

**Tests schlagen fehl?**
- Logs im Actions Tab prüfen
- Lokal mit `python run_tests.py` testen
- Fixes committen → Workflow läuft automatisch neu

**Deploy zu Netlify funktioniert nicht?**
- `NETLIFY_SITE_ID` und `NETLIFY_AUTH_TOKEN` prüfen
- Aus `build-deploy.yml` den Netlify-Step temporär kommentieren zum Debuggen

## 📖 Weitere Infos

Siehe [CI_CD_SETUP.md](CI_CD_SETUP.md) für detaillierte Anleitung
