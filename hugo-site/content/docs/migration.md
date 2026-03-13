+++
title = "Migration Guide"
weight = 40
+++

## 🔄 Von anderen Tools zu superheld.app

Du nutzt bereits Slack, Google Drive, LastPass oder ähnliches? Hier zeigen wir dir, wie du einfach umsteigst – ohne Daten zu verlieren.

---

## 📱 Von Slack zu superheld.app

### Warum wechseln?

```
Slack                          superheld.app
-----------                    ---------------
Google-Konzern sammelt Daten   Du besitzt deine Daten
Alle Nachrichten durchsuchbar  Nur du kannst lesen
Teuer ($12.50/User/Monat)      Günstiger ($9)
Keine Offline-Funktion        Offline-Zugriff
```

### Migration in 3 Schritten

{{% expand title="Schritt 1: Export aus Slack" %}}

```
1. Gehe zu Slack → Admin Panel
2. "Imports" → "Export"
3. Wähle Zeitraum (z.B. letzte 90 Tage)
4. Warte auf ZIP mit:
   - Alle Nachrichten (JSON)
   - Alle Dateien
   - Alle Benutzer + Kanäle
5. ZIP herunterladen
```

**Hinweis:** Slack Free hat begrenzte Exports (10.000 Nachrichten)

{{% /expand %}}

{{% expand title="Schritt 2: Import zu superheld.app" %}}

```
1. Öffne superheld.app
2. Gehe zu Settings → Workspace → Import
3. Wähle "From Slack"
4. ZIP hochladen
5. superheld.app konvertiert:
   ✅ Kanäle → Gruppen
   ✅ Nachrichten → verschlüsselt gespeichert
   ✅ Dateien → verschlüsselt gespeichert
   ✅ Benutzer → Einladungen gesendet
6. Warte ~5 Minuten auf Abschluss
```
{{% notice title="Wichtige Hinweise" color="info" %}}
- Import verschlüsselt alles automatisch
- Alte Slack-Metadaten werden nicht übertragen (absichtlich!)
- Alle Benutzer müssen neue Passwörter setzen
{{% /notice %}}

{{% /expand %}}

{{% expand title="Schritt 3: Team einladen & migrieren" %}}

```
1. superheld.app erstellt Einladungs-Email
2. Team-Mitglieder klicken Link
3. Erstelle Passwort + aktiviere 2FA
4. Alles neu konfigurieren:
   - Profile anpassen
   - Notification-Einstellungen
   - Zwei-Faktor-Auth
5. Beginne Kommunikation in superheld.app

Timeline:
- Tag 1: Import + Einladungen
- Tag 2-3: Team schafft sich ein
- Tag 4: Erste Gespräche
- Tag 7: Slack komplett aus
```

{{% /expand %}}

### Häufige Fragen beim Slack-Wechsel

{{% expand title="Was passiert mit meinen Slack-Archives?" %}}

Slack speichert alte Nachrichten:

```
Option 1: Alles mitnehmen
- Import kompletter History zu superheld
- Nimmt Zeit in Anspruch
- Alles verschlüsselt ab sofort

Option 2: Nur neue Nachrichten  
- Lasse alte auf Slack
- Starte frisch mit superheld
- Weniger Migration-Aufwand

Option 3: Hybrid
- Exportiere nur wichtige Kanäle
- Lasse Rest auf Slack
- Schrittweise Migration
```

{{% /expand %}}

{{% expand title="Kosten beim Wechsel?" %}}

```
Slack kostet: ~$12.50/User/Monat
superheld kostet: ~$9/User/Monat

Ersparnisse pro 10-er Team:
Slack: $125/Monat × 12 = $1.500/Jahr
superheld: $90/Monat × 12 = $1.080/Jahr
Ersparnisse: $420/Jahr

+ Extra Vorteile:
✅ Keine Google-Überwachung
✅ DSGVO konform
✅ Open Source
```

{{% /expand %}}

---

## 💾 Von Google Drive zu superheld.app

### Was mitnehmen?

```
Google Drive:
- Dokumente (.docs)
- Tabellen (.sheets)
- Präsentationen
- Fotos
- Videos
- Beliebige Dateien

superheld.app unterstützt:
✅ PDF (konvertierung)
✅ Office Open XML (.docx, .xlsx)
✅ Bilder (jedes Format)
✅ Videos (jedes Format)
✅ Archive (ZIP, RAR, etc.)
```

### Migration

{{% expand title="Einfache Migration" %}}

```
1. Google Drive öffnen
2. Selektiere alle Ordner/Dateien
3. Herunterladen als ZIP
4. superheld.app → "Upload Folder"
5. ZIP hochladen
6. superheld.app verschlüsselt alles ✅

Time: 5-30 Min (je nach Dateigröße)
```

{{% /expand %}}

{{% expand title="Dokumente konvertieren" %}}

Wenn du Google Docs benutzt:

```
1. Google Docs → Download → PDF/DOCX
2. Speichere alle Dokumente lokal
3. superheld.app → Upload
4. Oder nutze superheld's native Editor
   (ähnlich wie Google Docs, aber verschlüsselt)

Hinweis: Google Docs hat keine 1:1 Äquivalent,
aber superheld hat einen Web-Editor für
Zusammenarbeit (auch E2E verschlüsselt)
```

{{% /expand %}}

---

## 🔐 Von LastPass zu superheld.app

### Passwörter mitnehmen

{{% expand title="Export aus LastPass" %}}

```
1. LastPass → Account Settings
2. "Show Advanced" 
3. "Export" → "Database to CSV"
4. Speichern (unverschlüsselt, nur lokal!)
5. CSV hat Format:
   url,username,password,extra,name,folder
```

{{% notice title="⚠️ Achtung" color="warning" %}}
LastPass CSV ist unverschlüsselt! Speichern sofort nach Download, nicht versenden!
{{% /notice %}}

{{% /expand %}}

{{% expand title="Import zu superheld.app" %}}

```
1. Öffne superheld.app
2. Settings → Password Manager
3. "Import" → "From CSV"
4. LastPass CSV hochladen
5. superheld.app konvertiert:
   ✅ Alle Passwörter
   ✅ Zugriffsdetails
   ✅ Notizen
   ✅ Ordnerstruktur

   UND verschlüsselt alles mit AES-256
```

{{< button href="https://docs.superheld.app/password-manager/import" >}}Detaillierter Import-Guide{{< /button >}}

{{% /expand %}}

### Warum superheld ist besser für Passwörter

```
LastPass:
- Zentrale Kontrolle (LastPass hat Zugriff)
- Bekannt für Hacks
- Bezahlt, aber nicht sicher genug

superheld.app:
- Dezentralisiert (nur du hast Zugriff)
- Zero-Knowledge (wir sehen nichts)
- Encryption auch für API-Keys
- Offline-Zugriff
- Team-Sharing mit Zugriffsschutz
```

---

## 🔗 Von Zapier zu superheld.app

### Workflows migrieren

Zapier-Zaps → superheld Workflows:

{{% expand title="Schritt-für-Schritt Anleitung" %}}

**Beispiel:** GitHub Push → Slack Notification

```
Bei Zapier:
1. GitHub Trigger: "Push created"
2. Action: Slack "Send message"
3. Mapping von GitHub-Daten zu Slack

Bei superheld:
1. GitHub Webhook empfangen
2. Condition: "branch == main"?
3. Action: Slack message senden
4. Datenfluss bleibt lokal + verschlüsselt
```

**Key Difference:**
- Zapier: Dein GitHub-Token ist auf Zapier-Servern
- superheld: Dein GitHub-Token bleibt auf deinem Server ✅

{{% /expand %}}

{{% expand title="API-Keys sicherer lagern" %}}

```
superheld.app hat sichere Vault für API-Keys:

1. Settings → API Management
2. "Add New Key"
3. GitHub Token:
   - Eingeben
   - AES-256 verschlüsselt
   - Nur in Workflows nutzbar
   - Niemals sichtbar nach Speicherung
   - Nur auf deinem Server

Resultat: GitHub kann nicht sehen,
dass du Zapier nutzst!
```

{{% /expand %}}

---

## 📊 Migration Checkliste

{{% notice title="Vor der Migration" color="info" %}}

- [ ] Backup von aktuellen Tools (sicher lokal speichern)
- [ ] Alle wichtigen Daten exportieren
- [ ] Team informieren + Terminieren
- [ ] Downtime planen (meist 1-2 Tage)
- [ ] Test-Umgebung vorbereiten

{{% /notice %}}

{{% notice title="Während der Migration" color="info" %}}

- [ ] Daten hochladen zu superheld
- [ ] Verschlüsselung verifizieren  
- [ ] Team-Zugriffe einrichten
- [ ] Notifications + Integrationen testen
- [ ] Dokumentation aktualisieren

{{% /notice %}}

{{% notice title="Nach der Migration" %}}

- [ ] Alle Benutzer haben Zugriff?
- [ ] Alle Daten sind da? (stichprobenartig checken)
- [ ] 2FA aktiviert?
- [ ] Alte Accounts löschen (nach 30 Tagen)
- [ ] Team-Training (optional)
- [ ] Support-Kontakt dokumentieren

{{% /notice %}}

---

## 💬 Support bei Migration

Brauchst du Hilfe beim Umstieg?

{{< button href="mailto:migration@superheld.app" >}}Migration-Support kontaktieren{{< /button >}}

Wir bieten:
- ✅ Kostenlose Migrations-Beratung
- ✅ Technischer Support während Umstieg
- ✅ Team-Training
- ✅ Daten-Validierung

---

**Bereit?** [Installation starten →](/docs/einführung/installation-v2)
