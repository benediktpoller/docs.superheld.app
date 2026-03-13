---
title: "Privatsphäre & Sicherheit"
weight: 30
---

## 🔒 Die Philosophie von superheld.app

**superheld.app ist der Held für deine Privatsphäre – Datenschutz im Kern, nicht als Zusatz.**

Wir glauben, dass deine Daten *dir* gehören. Punkt. Nicht uns, nicht anderen. Darum haben wir superheld.app von Grund auf mit Datenschutz und Sicherheit gebaut.

---

## 🛡️ Wie superheld.app dich schützt

{{< callout type="info" >}}
Deine Daten gehören DIR. Nicht uns. Nicht anderen. Darum haben wir superheld.app mit Ende-zu-Ende Verschlüsselung gebaut – von Tag 1, nicht als Zusatz.
{{< /callout >}}

### 1️⃣ **Ende-zu-Ende Verschlüsselung (E2E)**

Alle deine Daten sind verschlüsselt – vom Moment, tippen bis zur Speicherung.

```
Dein Gerät
    ↓
[Daten getippt]
    ↓
🔐 AES-256 Verschlüsselung
    ↓
Nur du hast die Schlüssel
    ↓
Selbst superheld.app kann nicht lesen! ✅
    ↓
Internet-Übertragung (TLS 1.3)
    ↓
Server erhält nur verschlüsselte Daten
    ↓
Speicherung bleibt verschlüsselt
```

### 2️⃣ **Lokale Verarbeitung zuerst**

Die meisten Operationen laufen *auf deinem Gerät* – nicht auf unseren Servern.

**Was läuft lokal ab:**
- ✅ Encryption/Decryption
- ✅ Datenfilterung
- ✅ Workflow-Verarbeitung
- ✅ Offline-Funktionen

**Was synchronisiert wird:**
- 📡 Nur notwendige Metadaten (verschlüsselt)
- 📡 Backups (verschlüsselt)
- 📡 Team-Syncs (mit Permissions verschlüsselt)

### 3️⃣ **Null-Knowledge Architecture**

Das bedeutet: **Wir wissen nichts über deine Daten.**

```
Szenario: Du speicherst ein Passwort in superheld.app

Dein Passwort: "SuperSicheresPassword123!"

                 ↓
          
         [Auf deinem Gerät]
         Verschlüsselt mit DEINEM Schlüssel
         
                 ↓
         
      superheld.app Server sieht:
    "xK9mL2qP!w#vR4sT$Y%uI&oP*aS(dF)gH"
    
         (Keine Ahnung was drin ist! 🤷)
         
                 ↓
         
      Nur DU kannst mit deinem Schlüssel
      das Passwort wieder lesen
```

**Folge:** Selbst wenn Hacker in unsere Server eindringen – deine Daten bleiben sicher verschlüsselt.

### 4️⃣ **Keine Tracking, keine Werbung, keine Datenverkäufe**

| Was superheld.app NICHT tut | |
|-----|---|
| 📊 Dein Verhalten tracken | ✅ Nicht getan |
| 📢 Personalisierte Werbung zeigen | ✅ Nicht getan |
| 💰 Daten an Dritte verkaufen | ✅ Nicht getan |
| 📍 Deinen Standort weltweit verbreiten | ✅ Nicht getan |
| 👁 Deine Kamera/Mikro abhören | ✅ Nicht getan |

**Unser Business-Modell:** Du zahlst → Wir beliefern dir den Service. Das ist alles.  
Deine Daten sind kein Produkt, das verkauft werden kann.

### 5️⃣ **Open Source & Transparent**

Code ist öffentlich [auf GitHub](https://github.com/benediktpoller/superheld-app) einsehbar.

```
Du kannst sehen:
✅ Wie deine Daten verschlüsselt werden
✅ Was der Server speichert
✅ Welche Berechtigungen nötig sind
✅ Wo die Schwachstellen sind (ja, ehrlich!)
```

**Sicherheit durch Transparenz:** 10.000+ Security-Profis können Code reviewen. Wenn ein Bug existiert, wissen wir schnell davon.

### 6️⃣ **DSGVO-konform von Tag 1**

Wir halten sich an die strengsten Datenschutzgesetze der Welt (DSGVO, CCPA, LGPD, etc.):

- ✅ **Datenminimierung** – Wir speichern nur das Nötigste
- ✅ **Dein Recht auf Vergessenheit** – Löschen auf Knopfdruck
- ✅ **Datenportabilität** – Exportiere deine Daten jederzeit
- ✅ **Transparenz** – Datenschutzerklärung in Mensch-Sprache
- ✅ **Sichere Löschung** – Daten sind nach Löschung **wirklich weg**, nicht nur "versteckt"

---

## 🚀 So funktioniert superheld.app im Detail

### Workflow: "Sichere Nachricht verschicken"

```
SCHRITT 1: Nachricht tippen
┌─────────────────────────────┐
│ Meine Nachricht:            │
│ "Hey, Treffpunkt morgen?"  │
└─────────────────────────────┘
                ↓
        [Auf DEINEM Gerät]
SCHRITT 2: Verschlüsseln
        
        Message + DEIN_GEHEIMSCHLÜSSEL
            ↓ (AES-256)
        
        🔐 xK9mL2qPvR4sT5Y6uI7oP8aS9dF0gH
                ↓
SCHRITT 3: Senden über TLS 1.3 (sichere Leitung)
        (Netzwerk kann nicht abhört werden)
                ↓
SCHRITT 4: Server speichert (VERSCHLÜSSELT!)
        
    Datenbank Entry:
    ┌─────────────────────────────────┐
    │ user_id: 🔐 (verschlüsselt)    │
    │ message: 🔐 xK9mL2qPvR4sT5Y... │
    │ timestamp: 🔐 (verschlüsselt)  │
    │ recipient: 🔐 (verschlüsselt)  │
    └─────────────────────────────────┘
    
    SuperHeld-Server: "🤷 Keine Ahnung was drin ist"
                ↓
SCHRITT 5: Empfänger will lesen
        
        Bekommt: 🔐 xK9mL2qP...
             + SEIN_GEHEIMSCHLÜSSEL
            ↓ (Entschlüsselung)
        
        Sieht: "Hey, Treffpunkt morgen?"
                ↓
SCHRITT 6: Nachricht lesen & antworten
        (Gleicher Prozess umgekehrt)
```

**Fazit:** Niemand – auch nicht superheld.app – kann deine Nachricht lesen. Nur du und der Empfänger!

---

{{< details title="Klick für Details: Risiken & Schutzmaßnahmen" >}}

|  Szenario | Risiko | superheld.app Lösung |
|---|---|---|
| 🚗 Im Auto mit öffentlichem WLAN | WLAN kann abgehört werden | TLS 1.3 verschlüsselt alles |
| ☕ Im Café, Hacker im gleichen Netz | Man-in-the-Middle Attacke möglich | E2E Encryption schützt |
| 🏪 Bahn mit schlechtem Signal | Daten könnten unterwegs abgefangen werden | Lokal verschlüsselt, dann gesendet |
| 📱 Handy gestohlen | Dieb könnte Apps öffnen | Biometrische Locks & Passcode |
| 🏨 Hotel mit Spionage-WLAN | Intentionaler Daten-Dieben | E2E: Hacker sieht nur Kauderwelsch |

{{< /details >}}
| ☕ Im Café, Hacker im gleichen Netz | Man-in-the-Middle Attacke möglich | E2E Encryption schützt |
| 🏪 Bahn mit schlechtem Signal | Daten könnten unterwegs abgefangen werden | Lokal verschlüsselt, dann gesendet |
| 📱 Handy gestohlen | Dieb könnte Apps öffnen | Biometrische Locks & Passcode |
| 🏨 Hotel mit Spionage-WLAN | Intentionaler Daten-Dieben | E2E: Hacker sieht nur Kauderwelsch |

### 🛡️ 5 Regeln für sichere unterwegs Arbeit

#### 1️⃣ **Verwende SuperHeld's Offline-Mode**

```
Szenario: Du bist in einem Tunnel, Internet weg

Deine Arbeit:
✅ Nachrichten schreiben (lokal verschlüsselt)
✅ Dokumente bearbeiten (lokal gespeichert)
✅ Adressen aktualisieren (lokal verschlüsselt)

Das passiert im Hintergrund:
💤 Nichts wird gesendet
🔐 Alles bleibt lokal verschlüsselt

Wenn du wieder Online bist:
🔄 Automatische Sync
🔒 Mit E2E Verschlüsselung
✅ Alles ist sicher!
```

#### 2️⃣ **Aktiviere Biometrische Locks**

```
┌──────────────────────────────────────┐
│  superheld.app Lock-Optionen:        │
├──────────────────────────────────────┤
│                                      │
│ Sicherheitsstufe: Hoch ⭐⭐⭐⭐⭐ │
│                                      │
│ Methoden (aktiviert):                │
│ ☑️ Face ID / TouchID               │
│ ☑️ Fingerabdruck                   │
│ ☑️ Passcode (6-stellig)            │
│ ☑️ Auto-Lock nach 2 Minuten        │
│ ☑️ Benachrichtigung bei Eindringen  │
│                                      │
│ Wenn jemand dein Handy stiehlt:     │
│                                      │
│ 1. App sperrt sich auto              │
│ 2. Remote-Block möglich (Website)   │
│ 3. Daten können komplett gelöscht   │
│    werden (Wipe-on-Unlock)          │
│                                      │
└──────────────────────────────────────┘
```

#### 3️⃣ **Nutze VPN nur, wenn du ihm traust**

❌ **Problem mit Standard-VPNs:**
```
Dein Standard-Fluss:
Dein Daten → VPN-Server → Internet

Der VPN-Betreiber sieht:
- Wohin du gehst (Websites)
- Was du sendest (could be decrypted)
- Dein echte IP-Adresse (oft)
```

✅ **superheld.app mit VPN:**
```
Dein Fluss:
Dein Daten → [E2E VERSCHLÜSSELT] 
    → VPN → Internet

Was VPN-Betreiber sieht:
- NICHTS verständliches (E2E!)
- Nur: Du sendest Datenpakete
- Nicht: Was drin ist
```

**Empfehlung:** Verwende nur vertrauenswürdige VPN-Services (z.B. ProtonVPN, Mullvad). Besser noch: OG ohne VPN, da E2E das meiste schützt!

#### 4️⃣ **Aktiviere Zwei-Faktor-Authentifizierung (2FA)**

```
Login ohne 2FA (unsicher):
Passwort eingeben → Zack, du bist rein ❌

Login mit 2FA (sicher):
1. Passwort eingeben
   ↓
2. SuperHeld sendet Code an dein Handy
   (SMS, Authenticator-App, oder Hardware-Key)
   ↓
3. Du gibst Code ein
   ↓
4. ERST DANN: Du bist rein ✅

Warum sicherer?
Selbst wenn Passwort gehackt:
Hacker braucht AUCH dein Handy/Code
(Wahrscheinlichkeit sinkt drastisch)
```

**Optionen in superheld.app:**
- 📱 Authenticator App (bewährt)
- 🔑 Hardware Security Key (Pentagon-Level!)
- 📧 E-Mail Codes (schnell, okay)
- ❌ SMS (Letzte Option, nicht ideal)

#### 5️⃣ **Regelmäßig Aktivitäten protokollieren**

```
In SuperHeld go to:
Settings → Security → Activity Log
        ↓

Du siehst:
┌──────────────────────────────────────┐
│ 📋 Aktivitäts-Protokoll             │
├──────────────────────────────────────┤
│                                      │
│ Wann | Was | Von wo | Gerät         │
│─────────────────────────────────────│
│ 14:23│Login|Berlin|iPhone 14       │
│ 14:22│Downloaded|Berlin|Chrome     │
│ 13:15│Login|Tokyo(?) |Android      │  ⚠️
│ 13:14│File edited|Tokyo|iPad       │  ⚠️
│                                      │
│ ⚠️ = Ungewöhnlich!                  │
│                                      │
│ [Aktivität blockieren]              │
│ [Passwort jetzt ändern]             │
│ [Support kontaktieren]              │
│                                      │
└──────────────────────────────────────┘
```

**Checkliste wöchentlich:**
- ✅ Unbekannte Logins? Nein = Gut!
- ✅ Unerwartete Änderungen? Nein = Gut!
- ✅ Neue Geräte? Nein = Gut!

Falls JA → Sofort Passwort ändern + Support kontaktieren!

---

## 🔐 Technische Sicherheitsmaßnahmen

### Verschlüsselungs-Standards

| Standard | Was schützt | Stärke |
|----------|-----------|--------|
| **AES-256** | Ruhende Daten | 🟢 Militär-Klasse |
| **TLS 1.3** | Übertragung | 🟢 Bank-Standard |
| **RSA-4096** | Schlüsselaustausch | 🟢 Quantum-resistent |
| **HMAC-SHA256** | Integrität | 🟢 Kann nicht gefälscht werden |

### Infrastruktur-Sicherheit

####🏗️ Server-Isolation
```
Deine Daten sind komplett isoliert:

[Server-Cluster]
  ├─ [Isolation Zone 1] → Nur Daten User#1
  ├─ [Isolation Zone 2] → Nur Daten User#2
  ├─ [Isolation Zone 3] → Nur Daten User#3
  └─ [Isolation Zone N] → Nur Daten UserN

Selbst wenn Hacker Zone 2 angreift:
Zone 1, 3, N sind nicht betroffen!
```

#### 🔥 Firewall & DDoS-Schutz
- 🟢 Enterprise Firewall (Cloudflare Enterprise)
- 🟢 DDoS-Schutz (99,99% Verfügbarkeit)
- 🟢 Intrusion Detection (AI-basiert)
- 🟢 24/7 Monitoring

#### 🔍 Regelmäßige Sicherheits-Audits
```
Zeitplan:
- Wöchentlich: Automatische Scans
- Monatlich: Penetration Tests (ethische Hacker)
- Quarterly: Externe Security-Audits
- Jährlich: Full SOC 2 Type II Zertifizierung
```

---

## 📚 Deine Rechte & Kontrolle

### 1️⃣ **Recht auf Vergessenheit (DSGVO Art. 17)**

```
Du möchtest deine Daten löschen?

Gehe zu: Settings → Privacy → Delete Account

┌─────────────────────────────────────┐
│ Permanente Löschung                 │
├─────────────────────────────────────┤
│                                     │
│ Folgende Daten werden gelöscht:     │
│ ☑️ Profil & Einstellungen          │
│ ☑️ Nachrichten & Dateien           │
│ ☑️ Aktivitäts-Logs                 │
│ ☑️ Backups (nach 30 Tagen)        │
│ ☑️ Alle verschlüsselten Daten      │
│                                     │
│ Zeitrahmen: Innerhalb 24 Stunden   │
│                                     │
│ [Löschen bestätigen]               │
│ (Eingabe: "Ich verstehe, das ist   │
│  permanent und kann nicht rückgängig│
│  gemacht werden")                  │
│                                     │
└─────────────────────────────────────┘
```

**Was passiert nach Löschung:**
- ✅ Diche Accout ist weg
- ✅ Nachrichten an andere sind noch lesbar (sie gehören ihnen!)
- ✅ Server-Backups werden nach 30 Tagen überschrieben
- ✅ Keine Wiederherstellung möglich

### 2️⃣ **Datenexport (DSGVO Art. 20)**

```
Du willst deine Daten in einer anderen App nutzen?

Gehe zu: Settings → Privacy → Export Data

superheld.app gibt dir alles in Standard-Formaten:
✅ JSON (für Apps & APIs)
✅ CSV (für Spreadsheets)
✅ PDF (zum Drucken/Archivieren)

Deine Daten gehören DIR!
```

### 3️⃣ **Transparenz-Reports**

Wir veröffentlichen transparent:
- 📊 Wie viele Daten-Anfragen Regierungen stellen
- 🚨 Wie viele wir ablehnen
- 💾 Wie viel Speicherplatz du nutzt
- 🔓 Wie viele Benutzer 2FA nutzen

[Aktuelle Reports](https://superheld.app/transparency)

---

## ⚡ Checkliste: Du bist sicher, wenn...

- ✅ Face ID / Fingerabdruck aktiviert (Handy-Lock)
- ✅ Passcode 6-stellig oder länger
- ✅ 2FA aktiviert (Authenticator App, nicht SMS)
- ✅ Activity Log wöchentlich gecheckt
- ✅ App immer auf neuster Version
- ✅ Handy-Betriebssystem aktuell
- ✅ Du NIEMALS dein Passwort teilst (nicht mal Support!)
- ✅ Du weißt: superheld.app kann nicht in deine Daten schauen

**Wenn alle Häkchen grün sind: Du bist maximalist geschützt!** 🎉

---

## 🆘 Was tun, wenn etwas verdächtig ist?

### Notfall-Prozess

**Schritt 1: Sofort handeln (unter 5 Minuten)**

```
Verdacht auf Hack? (Z.B. unbekannter Login im Activity Log)

1. Passwort ändern
   → Settings → Security → Change Password
   
2. Alle Sessions beenden
   → Settings → Security → Logout All Devices
   
3. 2FA überprüfen
   → Ist deine Nummer noch korrekt?
   → Ist Authenticator App noch da?
```

**Schritt 2: Uns informieren (nächste 30 Minuten)**

```
Support → "Sicherheits-Incident"

Beschreibe:
- Wann hast du es gemerkt?
- Was ist verdächtig?
- Wo warst du online?
- Welche Geräte nutzt du?

Unser Team:
🔴 Pauses alle deine Sessions
🔴 Überprüft Logs
🔴 Benachrichtigt dich von verdächtigen Aktivitäten
```

**Schritt 3: Verhärtung (nächste 24 Stunden)**

```
- 🔑 Alle Passwörter ändern (auch andere Apps!)
- 🔑 2FA auf anderen Servies überprüfen
- 💾 Virenscan auf deinem Gerät
- 📱 Handy-Sicherheit updaten
- 🚩 Kreditkarten überwachen (falls Zahlungsdaten betroffen)
```

---

## 📞 Kontakt & Weitere Hilfe

**Sicherheits-Fragen:** support@superheld.app  
**Notfall / Bug Report:** security@superheld.app  
**Transparenz Reports:** https://superheld.app/transparency

---

## 🎓 Weitere Ressourcen

- [Installation & Grundlagen](/docs/einführung/installation)
- [Sichere Nutzung unterwegs](/docs/nutzung)
- [Erweiterte Sicherheits-Konfiguration](/docs/konfiguration)
- [FAQ: Häufige Sicherheits-Fragen](/docs/faq)

---

**Deine Privatsphäre ist nicht verhandelbar.**  
**SuperHeld schützt sie, damit du dich auf das konzentrieren kannst, das dir wichtig ist.**

🛡️ Stay safe! 🛡️
