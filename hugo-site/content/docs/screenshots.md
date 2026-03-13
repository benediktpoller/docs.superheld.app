---
title: "Screenshots & Use Cases"
weight: 50
---

## 📸 Visuelle Übersicht

Entdecke die Hauptfunktionen von superheld.app an realen Beispielen.

---

## Use Case 1: Erste Inbetriebnahme

### 🎯 Szenario
Du öffnest superheld.app zum ersten Mal und möchtest die App in wenigen Minuten einrichten.

### 📱 Willkommens-Screen
```
┌─────────────────────────────────────────┐
│                                         │
│        🦸 superheld.app                │
│                                         │
│    Willkommen zurück!                  │
│                                         │
│  ┌──────────────────────────┐          │
│  │ 🔧 Konfigurieren        │          │
│  │    (5 Minuten)          │          │
│  └──────────────────────────┘          │
│                                         │
│  ┌──────────────────────────┐          │
│  │ 📚 Anleitung anzeigen   │          │
│  │    (optional)           │          │
│  └──────────────────────────┘          │
│                                         │
│  ┌──────────────────────────┐          │
│  │ ⚙️ Einstellungen          │          │
│  │    (Advanced)           │          │
│  └──────────────────────────┘          │
│                                         │
└─────────────────────────────────────────┘
```

### 💡 Ablauf
1. **Setup Wizard** führt dich durch 5 Schritte
2. **Visuelle Feedback** zeigt Fortschritt (50%, 100%)
3. **Bestätigung** wenn fertig → Ready to use!

**Ergebnis:** Nach 5 Minuten ist deine erste Konfiguration done ✅

---

## Use Case 2: Tägliche Nutzung

### 🎯 Szenario  
Du nutzt superheld.app jeden Tag für deine Workflow-Automation.

### 📊 Dashboard
```
┌──────────────────────────────────────────────────┐
│ superheld.app Dashboard                 🌙 ⚙️    │
├──────────────────────────────────────────────────┤
│                                                  │
│  📈 Heute                                        │
│  ┌──────────────────────────────────────────┐   │
│  │ 42 Automatisierungen ausgelöst            │   │
│  │ 2.3 MB Daten verarbeitet                  │   │
│  │ 📊 ▂▄▆██▆▄▂ (Performance gut)            │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│  🔔 Aktive Aufgaben                             │
│  ┌──────────────────────────────────────────┐   │
│  │ [✓] Backup erstellt      14:23           │   │
│  │ [⏳] Sync läuft...        5 Minuten       │   │
│  │ [⏸] Warte auf Trigger    Pause          │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│  🚨 Benachrichtigungen                          │
│  ┌──────────────────────────────────────────┐   │
│  │ Status: ✅ Alles normal                   │   │
│  │ Letzte Fehler: Keine                     │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
└──────────────────────────────────────────────────┘
```

### ⚡ Quick Actions
- **Schnelle Buttons** zum Starten/Pausieren von Tasks
- **Live Updates** zeigen aktuelle Status
- **Ein-Klick Pause/Resume** ohne zu verlassen

**Ergebnis:** Volle Kontrolle mit minimalem Aufwand ⚡

---

## Use Case 3: Erweiterte Konfiguration

### 🎯 Szenario
Du möchtest komplexe Workflows mit bedingten Regeln aufbauen.

### 🛠 Configuration Mode
```
┌───────────────────────────────────────────────────┐
│ Workflow-Editor - Erweiterte Konfiguration       │
├───────────────────────────────────────────────────┤
│                                                   │
│ Workflow: "Tägliche Datensicherung"             │
│                                                   │
│ 📋 Schritte:                                     │
│                                                   │
│  1. [Trigger] IF Uhrzeit = 02:00 THEN           │
│  2. [Action]  Backup starten                     │
│  3. [Wait]    Warte bis Backup fertig           │
│  4. [If]      IF Status = "success" THEN        │
│  5. [Action]  E-Mail Bestätigung senden         │
│  6. [Else]    IF Status = "error" THEN          │
│  7. [Action]  Admin benachrichtigen             │
│  8. [Log]     Ergebnis protokollieren            │
│                                                   │
│  ✅ ✏️ 🔄 🗑                                      │
│                                                   │
│ [Test] [Speichern] [Veröffentlichen]           │
│                                                   │
└───────────────────────────────────────────────────┘
```

### 🧠 Workflow Features
- **Visuelle Workflow-Builder** - Keine Code-Syntax nötig
- **Bedingte Logik** - IF/THEN/ELSE Regeln
- **Fehlerbehandlung** - Was wenn etwas schiefgeht?
- **Test-Mode** - Vor dem Veröffentlichen testen

**Ergebnis:** Komplexe Automatisierungen ohne Code-Kenntnisse 🎯

---

## Use Case 4: Monitoring & Fehlerbehandlung

### 🎯 Szenario
Eine wichtige Automatisierung ist fehlgeschlagen. Wie finde ich das Problem?

### 📊 Activity Log / Historien
```
┌──────────────────────────────────────────────────┐
│ Aktivitäts-Log & Fehlersuche                    │
├──────────────────────────────────────────────────┤
│                                                  │
│ Filter: [Alles] [Erfolg] [Fehler] [Warnung]    │
│                                                  │
│ 🔍 Suche: ________________ [🔎]                │
│                                                  │
│ Datum | Status | Task | Details      | Aktion   │
│────────────────────────────────────────────────│
│ 14:23 │  ✅   │ Sync │ 2.3 MB ✓      │ 📋      │
│ 14:15 │  ❌   │ Mail │ SMTP Error... │ 🔍 Mehr │
│ 14:10 │  ⚠️   │ Data │ Timeout 60s   │ 🔄      │
│ 14:05 │  ⏹   │ Wait │ Abgebrochen   │ 🗑      │
│ 13:50 │  ✅   │ Back │ OK            │ 📋      │
│                                                  │
│ [Mehr laden]                                    │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 🔍 Fehlerdetails
```
┌──────────────────────────────────────────────────┐
│ Fehler-Details                                  │
├──────────────────────────────────────────────────┤
│                                                  │
│ Task: "E-Mail-Versand"                          │
│ Zeit: 14:15 Uhr                                 │
│ Status: ❌ FEHLER                                │
│                                                  │
│ Error Message:                                  │
│ "SMTP Authentication failed (Code: 535)"       │
│                                                  │
│ Mögliche Ursachen:                              │
│ → Passwort abgelaufen?                          │
│ → SMTP-Server nicht erreichbar?                │
│ → Firewall blockiert Port 587?                 │
│                                                  │
│ 💡 Schnelle Lösungen:                           │
│ [🔧 Einstellungen] [🔄 Erneut versuchen]      │
│                                                  │
│ 📚 [Fehler-Dokumentation anzeigen]             │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 📋 Debugging Tools
- **Detaillierte Error Messages** - Was ist passiert?
- **Intelligente Vorschläge** - Mögliche Ursachen anzeigen
- **Quick-Fix Links** - Direkt zur Lösung
- **Automatische Logs** - Vollständige Historie

**Ergebnis:** Fehler in Minuten identifiziert & behoben 🔧

---

## Use Case 5: Team Collaboration

### 🎯 Szenario
Mehrere Team-Mitglieder nutzen superheld.app und müssen Workflows teilen.

### 👥 Sharing & Permissions
```
┌──────────────────────────────────────────────────┐
│ Workflow freigeben                              │
├──────────────────────────────────────────────────┤
│                                                  │
│ Workflow: "Tägliche Datensicherung"             │
│                                                  │
│ 👥 Zugriffsrechte:                              │
│                                                  │
│ ┌─ Benutzer ─────── Rolle ────── Aktion ──┐   │
│ │ du@example.com    👑 Admin     ⛔        │   │
│ │ anna@example.com  ✏️  Editor    🔄       │   │
│ │ bob@example.com   👁️  Viewer    🔄       │   │
│ │ team@..           👥 Gruppe    ➕       │   │
│ └──────────────────────────────────────────┘   │
│                                                  │
│ 🔗 Link: https://superheld.app/s/abc123       │
│    [📋 Kopieren] [🚫 Deaktivieren]            │
│                                                  │
│ 🔐 Berechtigungen:                              │
│ ☑️ Ausführung erlaubt                          │
│ ☑️ History anschauen                           │
│ ☐ Bearbeitung erlaubt                         │
│                                                  │
│ [Speichern]                                    │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 📝 Audit Trail
```
┌──────────────────────────────────────────────────┐
│ Änderungsverlauf (Wer hat was geändert?)       │
├──────────────────────────────────────────────────┤
│                                                  │
│ 13:45 | anna@example.com | ✏️ Modified Step 5  │
│       | "Retry-Count erhöht von 3 auf 5"       │
│                                                  │
│ 12:30 | bob@example.com   | 🏃 Executed        │
│       | "Workflow erfolgreich ausgelöst"       │
│                                                  │
│ 11:15 | du@example.com    | ✏️ Created Workflow│
│       | "Neue Automation erstellt"             │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 🎯 Collaboration Benefits
- **Role-based Access Control** - Admin, Editor, Viewer
- **Shareable Links** - Einfach zum Teilen
- **Audit Trail** - Wer hat was geändert?
- **Notifications** - Team bleibt informiert

**Ergebnis:** Nahtlose Team-Zusammenarbeit 👥

---

## Use Case 6: Mobile App

### 🎯 Szenario
Du bist unterwegs und möchtest deine Workflows schnell kontrollieren.

### 📱 Mobile Dashboard
```
┌──────────────────────┐
│  superheld.app       │ 
│  12:34 📶 ▔▔▔ 🔋    │
├──────────────────────┤
│                      │
│  📊 Status           │
│  ──────────────────  │
│  ✅ 5 aktiv          │
│  ⏳ 2 läuft          │
│  ❌ 1 Fehler         │
│                      │
│  🔔 Aktuelle Aufgabe │
│  ──────────────────  │
│  Backup Sync         │
│  ████████░░ 80%      │
│  Fertig in ~2min     │
│                      │
│  ⚡ Quick Actions    │
│  [▶] [⏸] [🔄]       │
│                      │
│  🚨 Alerts           │
│  ──────────────────  │
│  Mail-Error 14:15    │
│  Tap für Details     │
│                      │
├──────────────────────┤
│ [Dashboard] [Log] ⚙️ │
└──────────────────────┘
```

### ✨ Mobile Features
- **Minimales Design** - Schnell erfassen, was los ist
- **Touch-optimiert** - Große Buttons, einfach zu tappen
- **Push Notifications** - Bleib benachrichtigt
- **Offline-Ready** - Funktioniert auch ohne Internet

**Ergebnis:** Kontrolle von überall 📱

---

## Use Case 7: Integration & API

### 🎯 Szenario
Du möchtest superheld.app mit anderen Tools verbinden (Slack, GitHub, etc.).

### 🔌 Integrationen
```
┌──────────────────────────────────────────────────┐
│ Verfügbare Integrationen                        │
├──────────────────────────────────────────────────┤
│                                                  │
│ 💬 Slack              [✅ Verbunden]            │
│    Sende Alerts zu Slack-Channels               │
│    [⚙️ Einstellungen] [🔄 Neu verbinden]      │
│                                                  │
│ 🐙 GitHub             [➕ Verbinden]            │
│    Triggere Workflows bei GitHub Events         │
│    [Verbinden mit OAuth]                        │
│                                                  │
│ 📧 Gmail              [❌ Nicht verbunden]      │
│    Sende / Empfange E-Mails                     │
│    [Aktivieren]                                 │
│                                                  │
│ ☁️ Dropbox            [✅ Verbunden]            │
│    Automatische Backups zu Dropbox              │
│    [⚙️ Einstellungen]                           │
│                                                  │
│ 🔗 Webhook Support                              │
│    [+ Neuen Webhook hinzufügen]                │
│                                                  │
├──────────────────────────────────────────────────┤
│ 📚 [API Dokumentation lesen]                    │
│                                                  │
└──────────────────────────────────────────────────┘
```

### 🔗 Beispiel-Workflow mit Integrations
```
Event eintritt (GitHub Push)
    ↓
superheld.app erkennt Event
    ↓
Webhook triggert Workflow
    ↓
Führe Aktionen durch
    ├→ Build starten
    ├→ Tests ausführen
    └→ Slack benachrichtigen
    ↓
Status zu GitHub zurück
    ↓
✅ Pipeline vollständig automatisiert
```

### 🌐 Integration Benefits
- **30+ vordefinierte Integrationen**
- **Custom Webhooks** - Verbinde mit allem
- **OAuth 2.0** - Sichere Authentifizierung
- **Real-time Sync** - Daten immer aktuell

**Ergebnis:** Alles ist verbunden, alles ist automatisiert 🔗

---

## Feature-Übersicht

| Feature | Use Case | Status |
|---------|----------|--------|
| **Willkommens-Wizard** | Schnelle Einrichtung | ✅ |
| **Dashboard** | Tägliche Überwachung | ✅ |
| **Workflow-Editor** | Komplexe Automatisierung | ✅ |
| **Activity Log** | Fehlersuche | ✅ |
| **Team Sharing** | Zusammenarbeit | ✅ |
| **Mobile App** | Unterwegs | ✅ |
| **Integrationen** | Drittanbieter-Tools | ✅ |
| **API Access** | Custom Automation | ✅ |

---

## 🎓 Welche Seite passt zu mir?

- **Anfänger?** → [Installation](/docs/einführung/installation) & [Setup](/docs/einführung/setup)
- **Täglich nutzen?** → [Nutzung](/docs/nutzung)
- **Profi-Workflows?** → [Konfiguration](/docs/konfiguration)
- **Fragen?** → [FAQ](/docs/faq)

---

**Bereit zu starten?** [Jetzt Installation durchgehen →](/docs/einführung/installation)
