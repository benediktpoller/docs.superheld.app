---
title: "Apps & Plattformen"
weight: 25
---

## App-Übersicht

superheld.app ist eine **plattformspezifische Schutz-App**, die auf jedem Gerät eine konsistente Schutzschicht bereitstellt. Alle Apps teilen dieselbe Kernlogik (Proxy, VPN, Kindersicherung, Sicherheitsstatus, KI-Analyse) – die Oberfläche passt sich an das Gerät und die Nutzungsrolle an.

> Diese Seite beschreibt: **Android, iOS, Windows, macOS, Linux** sowie typische Nutzungsszenarien für **Einsteiger (DAU), versierte Nutzer, Eltern und Administratoren**.

---

## App-Architektur (Shared Core)

Die App besteht aus drei Kernbereichen:

1. **Device Guardian (MDM-Light)**
   - Geräte-Registrierung & Inventarisierung
   - Root/Jailbreak-Detektion
   - Sicherheitsstatus & Patchlevel

2. **Secure Web Proxy + VPN**
   - Filterregeln (Jugendschutz, Malware, Scam, illegale Inhalte)
   - Ausnahmen (einmalig / zeitlich / dauerhaft)
   - Optionaler VPN‑Tunnel für verschlüsselten Verkehr

3. **AI Safety Layer**
   - LLM-/Chat‑Traffic überwachen (Local-first)
   - Erkennen von Social Engineering (z.B. Fake‑Support, Phishing)
   - Warnungen und automatische Blockierung

Zusätzlich sind integriert:
- **Passkey / Biometric Lock** (Touch/Face ID, Fingerabdruck)
- **Eltern‑Dashboard** mit Nutzer-/Geräte‑Profilen
- **Trusted Apps / Untrusted Apps** (Whitelist/Paket‑Kontrolle)

---

## Android (App Store / Play Store)

![Android App](/images/screenshot-android.svg)

### Was du siehst
- Startbildschirm: **VPN**, **Webschutz**, **Geräte‑Status**, **Kindersicherung**
- Schnellzugriff: **Ein‑/Aus‑Schalter für den Proxy**, **Sicherheitsstatus (grün/gelb/rot)**
- Geführtes Setup für **Eltern‑Modus** & **Kind‑Profil**

### Kurzanleitung (DAU)
1. App aus dem Google Play Store installieren
2. Öffne superheld.app → **Konto erstellen** oder **anmelden**
3. Folge dem Setup: **Einrichtung des VPN/Proxy**
4. Tippe auf **VPN starten** → grüne Anzeige bedeutet: Schutz aktiv

### Für versierte Nutzer
- **Regelsets konfigurieren** (Malware / Adult Content / Zeitlimits)
- **Ausnahmen hinzufügen** (z.B. Bildungsdomain für Schule)
- **Logs prüfen**: Filter → Aktivität → blockierte Anfragen

---

## iOS (App Store)

![iOS App](/images/screenshot-ios.svg)

### Besonderheiten
- iOS erlaubt keinen System‑weiten Proxy, daher verwendet superheld.app eine Kombination aus **VPN + DNS‑Filter**.
- **Passkey & Face ID** werden nativ unterstützt.

### Kurzanleitung (DAU)
1. App Store öffnen, nach „superheld.app“ suchen
2. App installieren & öffnen
3. Erstelle ein Konto und aktiviere **Biometric Lock**
4. Starte den Schutz: **VPN & Webschutz aktivieren**

### Eltern‑Modus (Eltern)
- **Kinderprofile anlegen** (Telefon, iPad)
- Automatische **Regelsätze** (Jugendschutz, Schulzeiten)
- **Anfragen genehmigen**: Kind will eine blockierte Seite öffnen → Eltern erhalten Benachrichtigung

---

## Windows (Desktop)

![Windows App](/images/screenshot-windows.svg)

### Desktop‑Funktionen
- Vollständiger **Proxy-Filter** für Browser und Apps
- **VPN‑Tunnel** (+Split‑Tunneling)
- **Geräte‑Dashboard** (installierte Apps, Risiken, Updates)

### Kurzanleitung (DAU)
1. Installiere die App über den Installer (EXE)
2. Starte superheld.app und melde dich an
3. Klicke auf **Webfilter aktivieren** und **VPN starten**

### Für Administratoren
- **Policy‑Vorlagen** (z.B. Schulnetz, Familien‑PC)
- **Gruppenverwaltung** (mehrere PCs verwalten)
- **Remote Insights**: Zeigt an, welche Geräte aktuell offline sind

---

## macOS

![macOS App](/images/screenshot-macos.svg)

### Besonderheiten
- Nutzt macOS‑Systemproxies + System‑VPN (NEPacketTunnel)
- **Audit‑Logs** für Netzwerk‑Ereignisse (Datenschutzkonform)

### Kurzanleitung (DAU)
1. DMG herunterladen, App in den Applications‑Ordner ziehen
2. Starte superheld.app und melde dich an
3. Aktiviere **Proxy‑Regeln** und **VPN**

### Versierter Modus
- Erstelle **spezielle Regeln** für bestimmte Apps (z.B. Dev-Tools, Terminal)
- Nutze **Script‑Hooks** (CLI) für Automatisierung

---

## Linux (Debian/Ubuntu, Fedora, Arch)

![Linux App](/images/screenshot-linux.svg)

### Funktionen
- CLI‑Tool + optionales GUI
- **System‑Proxy** + **WireGuard‑VPN**
- Paketverwaltung für Updates

### Kurzanleitung (DAU)
1. Lade das passende Paket (DEB/RPM/AppImage) herunter
2. Installiere (z.B. `sudo dpkg -i superheld-app.deb`)
3. Starte `superheld-app` oder `superheld-app --gui`
4. Aktiviere Schutz und richte Profile ein

### Admins / Power User
- Automatisiere mit `superheld-app config set ...`
- Nutze **Agent‑Modus** im Headless‑Server
- Exportiere Logs für Audit / Compliance

---

## Rollen & typische Workflows

### 1. Einsteiger / DAU (Easy Mode)
- Einfache Setup‑Abfolge
- Ein großer **Ein‑/Aus‑Button** (Schutz aktivieren)
- Visuelle Warnungen (rot/gelb/grün)
- Automatische Empfehlungen („Aktiviere Kindersicherung“, „Aktualisiere Firmware“)

### 2. Versierte Nutzer
- Feine Einstellungen (Proxy-Filter, Ausnahme‑Regeln, Zeitlimits)
- **Raw‑Log‑View** + Filter
- **Export / Import** von Regeln und Sicherungspaketen

### 3. Eltern
- Kindersicherung mit Profilen (Schule, Freizeit, Schlaf)
- Genehmigungs‑Workflow für blockierte Seiten
- Übersicht über Aktivität: **Was wurde geblockt?**

### 4. Administratoren
- Geräteliste + Status (online/offline)
- Remote‑Lock, Remote‑Wipe (optional)
- Richtlinien‑Vorlagen (z.B. „Eltern“, „Schule“, „Home‑Office“)

---

## Woher kommen die Inhalte?
Die Funktionen basieren auf dem **superheld.app‑Design**:
- Proxy + VPN + Filterregeln (Jugendschutz, Malware, Hochrisiko)
- Lokaler AI‑Layer (LLM‑Traffic überwachen)
- Eltern‑Workflow mit Genehmigungen
- Geräte‑Management wie bei Intune/Jamf – aber für Privatnutzer

---

## Nächste Schritte (Ausblick)
- **Passkeys & biometrische Anmeldung** (iOS & Android) sind im Beta‑Modus.
- **VPN‑Device‑Liste**: Alle verbundenen Geräte sichtbar, ähnlich Tailscale.
- **Trusted Apps / Untrusted Apps**: App‑Rating & Blocklisten.

---

