---
title: "Privatsphäre & Sicherheit"
weight: 15
aliases:
  - /docs/privacy-sicherheit
---

## Die Philosophie von superheld.app

**superheld.app ist der Held für deine Privatsphäre – Datenschutz im Kern, nicht als Zusatz.**

Wir glauben, dass deine Daten *dir* gehören. Punkt. Nicht uns, nicht anderen. Darum haben wir superheld.app von Grund auf mit Datenschutz und Sicherheit gebaut.

---

## Wie superheld.app dich schützt

{{< callout type="info" >}}
Deine Daten gehören DIR. Nicht uns. Nicht anderen. Darum haben wir superheld.app mit Ende-zu-Ende Verschlüsselung gebaut – von Tag 1, nicht als Zusatz.
{{< /callout >}}

### 1. Ende-zu-Ende Verschlüsselung (E2E)

Alle deine Daten sind verschlüsselt – vom Moment des Tippens bis zur Speicherung.

{{% steps %}}

#### Daten eingeben

Du tippst deine Daten auf deinem Gerät ein.

#### AES-256 Verschlüsselung

Die Daten werden lokal mit AES-256 verschlüsselt. Nur du hast die Schlüssel – selbst superheld.app kann sie nicht lesen.

#### Sichere Übertragung

Die verschlüsselten Daten werden über TLS 1.3 übertragen.

#### Verschlüsselte Speicherung

Der Server erhält und speichert ausschließlich verschlüsselte Daten.

{{% /steps %}}

### 2. Lokale Verarbeitung zuerst

Die meisten Operationen laufen *auf deinem Gerät* – nicht auf unseren Servern.

**Was lokal verarbeitet wird:**
- **Encryption/Decryption** – Verschlüsselung findet auf deinem Gerät statt
- **Datenfilterung** – Filterung und Suche laufen lokal
- **Workflow-Verarbeitung** – Workflows werden geräteseitig ausgeführt
- **Offline-Funktionen** – Voller Funktionsumfang auch ohne Internet

**Was synchronisiert wird:**
- **Metadaten** – Nur notwendige Metadaten (verschlüsselt)
- **Backups** – Automatische Sicherungen (verschlüsselt)
- **Team-Syncs** – Teamdaten mit Berechtigungssteuerung (verschlüsselt)

### 3. Null-Knowledge Architecture

Das bedeutet: **Wir wissen nichts über deine Daten.**

{{% steps %}}

#### Du speicherst ein Passwort

Beispiel: Du speicherst `SuperSicheresPassword123!` in superheld.app.

#### Verschlüsselung auf deinem Gerät

Das Passwort wird lokal mit deinem persönlichen Schlüssel verschlüsselt.

#### Server sieht nur Kauderwelsch

superheld.app Server speichert lediglich: `xK9mL2qP!w#vR4sT$Y%uI&oP*aS(dF)gH` – ohne jegliche Möglichkeit, den Inhalt zu entschlüsseln.

#### Nur du kannst entschlüsseln

Mit deinem persönlichen Schlüssel kannst nur du das Passwort wieder lesbar machen.

{{% /steps %}}

**Folge:** Selbst wenn Angreifer in unsere Server eindringen, bleiben deine Daten sicher verschlüsselt.

### 4. Kein Tracking, keine Werbung, keine Datenverkäufe

| Was superheld.app NICHT tut | Status |
|-----|---|
| Dein Verhalten tracken | Nicht getan |
| Personalisierte Werbung zeigen | Nicht getan |
| Daten an Dritte verkaufen | Nicht getan |
| Deinen Standort verbreiten | Nicht getan |
| Deine Kamera/Mikrofon abhören | Nicht getan |

**Unser Business-Modell:** Du zahlst – wir liefern dir den Service. Das ist alles.
Deine Daten sind kein Produkt, das verkauft werden kann.

### 5. Open Source und Transparent

Der Code ist öffentlich [auf GitHub](https://github.com/benediktpoller/superheld-app) einsehbar.

- **Verschlüsselung** – Du kannst nachvollziehen, wie deine Daten verschlüsselt werden
- **Serverspeicherung** – Einsicht in alles, was der Server speichert
- **Berechtigungen** – Transparenz über alle benötigten Berechtigungen
- **Schwachstellen** – Offener Umgang mit bekannten Schwachstellen

**Sicherheit durch Transparenz:** Tausende Security-Fachleute können den Code reviewen. Wenn ein Bug existiert, erfahren wir schnell davon.

### 6. DSGVO-konform von Tag 1

Wir halten uns an die strengsten Datenschutzgesetze der Welt (DSGVO, CCPA, LGPD u. a.):

- **Datenminimierung** – Wir speichern nur das Nötigste
- **Recht auf Vergessenheit** – Löschung auf Knopfdruck
- **Datenportabilität** – Exportiere deine Daten jederzeit
- **Transparenz** – Datenschutzerklärung in verständlicher Sprache
- **Sichere Löschung** – Daten sind nach Löschung **wirklich weg**, nicht nur ausgeblendet

---

## So funktioniert superheld.app im Detail

### Workflow: Sichere Nachricht verschicken

{{% steps %}}

#### Nachricht tippen

Du verfasst deine Nachricht, z. B. „Hey, Treffpunkt morgen?"

#### Verschlüsseln

Auf deinem Gerät wird die Nachricht mit deinem geheimen Schlüssel per AES-256 verschlüsselt.

#### Senden über TLS 1.3

Die verschlüsselte Nachricht wird über eine sichere TLS-1.3-Verbindung übertragen. Das Netzwerk kann nicht abgehört werden.

#### Server speichert verschlüsselt

Der Server speichert alle Felder ausschließlich verschlüsselt: User-ID, Nachricht, Zeitstempel und Empfänger. Der Server hat keine Möglichkeit, die Inhalte zu lesen.

#### Empfänger entschlüsselt

Der Empfänger erhält die verschlüsselte Nachricht und entschlüsselt sie mit seinem eigenen Schlüssel.

#### Nachricht lesen und antworten

Der Empfänger sieht die Nachricht im Klartext und kann über denselben sicheren Prozess antworten.

{{% /steps %}}

**Fazit:** Niemand – auch nicht superheld.app – kann deine Nachricht lesen. Nur du und der Empfänger.

---

{{< details title="Klick für Details: Risiken und Schutzmaßnahmen" >}}

| Szenario | Risiko | superheld.app Lösung |
|---|---|---|
| Im Auto mit öffentlichem WLAN | WLAN kann abgehört werden | TLS 1.3 verschlüsselt alles |
| Im Café, Hacker im gleichen Netz | Man-in-the-Middle Attacke möglich | E2E Encryption schützt |
| Bahn mit schlechtem Signal | Daten könnten unterwegs abgefangen werden | Lokal verschlüsselt, dann gesendet |
| Handy gestohlen | Dieb könnte Apps öffnen | Biometrische Locks und Passcode |
| Hotel mit Spionage-WLAN | Intentionaler Datendiebstahl | E2E: Angreifer sieht nur Kauderwelsch |

{{< /details >}}

### 5 Regeln für sicheres Arbeiten unterwegs

#### 1. Verwende den Offline-Modus von superheld.app

Im Offline-Modus (z. B. in einem Tunnel ohne Internet) kannst du weiterhin produktiv arbeiten:

- **Nachrichten schreiben** – lokal verschlüsselt gespeichert
- **Dokumente bearbeiten** – lokal gespeichert
- **Adressen aktualisieren** – lokal verschlüsselt

Sobald du wieder online bist, erfolgt automatisch eine verschlüsselte Synchronisation per E2E.

#### 2. Aktiviere biometrische Locks

superheld.app bietet mehrere Sicherheitsstufen für den Gerätezugriff:

- **Face ID / Touch ID** – Biometrische Entsperrung
- **Fingerabdruck** – Alternative biometrische Methode
- **Passcode (6-stellig)** – Numerischer Zugangscode
- **Auto-Lock nach 2 Minuten** – Automatische Sperrung bei Inaktivität
- **Benachrichtigung bei Eindringversuch** – Alarmierung bei unberechtigten Zugriffen

{{< callout type="warning" >}}
**Bei Diebstahl:** Die App sperrt sich automatisch. Über die Website kannst du eine Remote-Sperrung auslösen und bei Bedarf eine vollständige Datenlöschung (Wipe-on-Unlock) durchführen.
{{< /callout >}}

#### 3. Nutze VPN nur, wenn du ihm vertraust

**Problem mit Standard-VPNs:** Der VPN-Betreiber kann potenziell sehen, welche Websites du aufrufst, welche Daten du sendest und deine echte IP-Adresse.

**superheld.app mit VPN:** Dank E2E-Verschlüsselung sieht der VPN-Betreiber lediglich, dass du Datenpakete sendest – nicht, was darin enthalten ist.

**Empfehlung:** Verwende nur vertrauenswürdige VPN-Services (z. B. ProtonVPN, Mullvad). Da die E2E-Verschlüsselung bereits den Großteil schützt, ist ein VPN nicht zwingend erforderlich.

#### 4. Aktiviere Zwei-Faktor-Authentifizierung (2FA)

{{% steps %}}

#### Passwort eingeben

Gib dein Passwort wie gewohnt ein.

#### Code empfangen

superheld.app sendet einen Code an dein Handy (per Authenticator-App, SMS oder Hardware-Key).

#### Code eingeben

Gib den empfangenen Code ein.

#### Zugang erhalten

Erst nach erfolgreicher Verifizierung beider Faktoren erhältst du Zugang.

{{% /steps %}}

{{< callout type="info" >}}
Selbst wenn dein Passwort kompromittiert wird, benötigt ein Angreifer zusätzlich Zugriff auf deinen zweiten Faktor. Das reduziert das Risiko drastisch.
{{< /callout >}}

**Verfügbare 2FA-Methoden in superheld.app:**
- **Authenticator App** – Empfohlen (z. B. Google Authenticator, Authy)
- **Hardware Security Key** – Höchste Sicherheitsstufe (z. B. YubiKey)
- **E-Mail Codes** – Schnell eingerichtet, akzeptable Sicherheit
- **SMS** – Letzte Option, nicht ideal

#### 5. Regelmäßig Aktivitäten prüfen

Unter **Settings > Security > Activity Log** findest du eine Übersicht aller Zugriffe auf deinen Account, inklusive Zeitpunkt, Aktion, Standort und Gerät.

{{< callout type="warning" >}}
Achte auf ungewöhnliche Einträge, z. B. Logins von unbekannten Standorten oder Geräten. Bei verdächtigen Aktivitäten solltest du sofort dein Passwort ändern und den Support kontaktieren.
{{< /callout >}}

**Wöchentliche Checkliste:**
- **Unbekannte Logins?** – Falls nein: alles in Ordnung
- **Unerwartete Änderungen?** – Falls nein: alles in Ordnung
- **Neue Geräte?** – Falls nein: alles in Ordnung

Falls ja: Sofort Passwort ändern und Support kontaktieren.

---

## Technische Sicherheitsmaßnahmen

### Verschlüsselungs-Standards

| Standard | Was schützt | Stärke |
|----------|-----------|--------|
| **AES-256** | Ruhende Daten | Militär-Klasse |
| **TLS 1.3** | Übertragung | Bank-Standard |
| **RSA-4096** | Schlüsselaustausch | Quantum-resistent |
| **HMAC-SHA256** | Integrität | Fälschungssicher |

### Infrastruktur-Sicherheit

#### Server-Isolation

Deine Daten sind vollständig isoliert. Jeder Benutzer erhält eine eigene Isolation Zone innerhalb des Server-Clusters. Selbst wenn ein Angreifer Zugriff auf eine Zone erlangt, bleiben alle anderen Zonen unberührt.

#### Firewall und DDoS-Schutz

- **Enterprise Firewall** – Cloudflare Enterprise
- **DDoS-Schutz** – 99,99 % Verfügbarkeit
- **Intrusion Detection** – KI-basierte Erkennung
- **24/7 Monitoring** – Rund-um-die-Uhr-Überwachung

#### Regelmäßige Sicherheits-Audits

- **Wöchentlich:** Automatische Sicherheitsscans
- **Monatlich:** Penetration Tests durch ethische Hacker
- **Quartalsweise:** Externe Security-Audits
- **Jährlich:** Vollständige SOC 2 Type II Zertifizierung

---

## Deine Rechte und Kontrolle

### 1. Recht auf Vergessenheit (DSGVO Art. 17)

Du möchtest deine Daten löschen? Gehe zu **Settings > Privacy > Delete Account**.

Folgende Daten werden permanent gelöscht:
- Profil und Einstellungen
- Nachrichten und Dateien
- Aktivitäts-Logs
- Backups (nach 30 Tagen)
- Alle verschlüsselten Daten

{{< callout type="warning" >}}
Die Löschung erfolgt innerhalb von 24 Stunden und ist **nicht rückgängig zu machen**. Du musst die Löschung durch Eingabe einer Bestätigung autorisieren.
{{< /callout >}}

**Was passiert nach der Löschung:**
- **Dein Account ist gelöscht** – Vollständig und unwiderruflich
- **Nachrichten an andere bleiben erhalten** – Sie gehören den jeweiligen Empfängern
- **Server-Backups werden nach 30 Tagen überschrieben**
- **Keine Wiederherstellung möglich**

### 2. Datenexport (DSGVO Art. 20)

Du willst deine Daten in einer anderen App nutzen? Gehe zu **Settings > Privacy > Export Data**.

superheld.app stellt dir deine Daten in Standard-Formaten bereit:
- **JSON** – Für Apps und APIs
- **CSV** – Für Tabellenkalkulationen
- **PDF** – Zum Drucken und Archivieren

Deine Daten gehören dir.

### 3. Transparenz-Reports

Wir veröffentlichen regelmäßig Berichte zu folgenden Themen:
- **Behördenanfragen** – Anzahl der Datenanfragen von Regierungen
- **Ablehnungen** – Anzahl der abgelehnten Anfragen
- **Speichernutzung** – Dein genutzter Speicherplatz
- **2FA-Nutzung** – Anteil der Benutzer mit aktivierter Zwei-Faktor-Authentifizierung

[Aktuelle Reports](https://superheld.app/transparency)

---

## Checkliste: Du bist sicher, wenn...

- Face ID / Fingerabdruck aktiviert (Handy-Lock)
- Passcode 6-stellig oder länger
- 2FA aktiviert (Authenticator App, nicht SMS)
- Activity Log wöchentlich geprüft
- App immer auf neuester Version
- Handy-Betriebssystem aktuell
- Du NIEMALS dein Passwort teilst (nicht einmal mit dem Support)
- Du weißt: superheld.app kann nicht in deine Daten schauen

{{< callout type="info" >}}
Wenn alle Punkte erfüllt sind, bist du bestmöglich geschützt.
{{< /callout >}}

---

## Was tun, wenn etwas verdächtig ist?

### Notfall-Prozess

**Schritt 1: Sofort handeln (unter 5 Minuten)**

{{% steps %}}

#### Passwort ändern

Gehe zu **Settings > Security > Change Password** und setze ein neues, starkes Passwort.

#### Alle Sessions beenden

Gehe zu **Settings > Security > Logout All Devices**, um alle aktiven Sitzungen zu beenden.

#### 2FA überprüfen

Stelle sicher, dass deine hinterlegte Telefonnummer korrekt ist und deine Authenticator App noch funktioniert.

{{% /steps %}}

**Schritt 2: Uns informieren (nächste 30 Minuten)**

Kontaktiere den Support unter der Kategorie „Sicherheits-Incident" und beschreibe:
- Wann du die verdächtige Aktivität bemerkt hast
- Was genau verdächtig ist
- Wo du zuletzt online warst
- Welche Geräte du nutzt

Unser Team wird umgehend alle deine Sessions pausieren, die Logs überprüfen und dich über verdächtige Aktivitäten benachrichtigen.

**Schritt 3: Absicherung (nächste 24 Stunden)**

- **Passwörter ändern** – Auch bei anderen Apps und Diensten
- **2FA prüfen** – Zwei-Faktor-Authentifizierung bei allen relevanten Services überprüfen
- **Virenscan durchführen** – Gerät auf Schadsoftware untersuchen
- **System aktualisieren** – Handy-Sicherheitsupdates installieren
- **Zahlungsmittel überwachen** – Kreditkarten prüfen, falls Zahlungsdaten betroffen sein könnten

---

## Kontakt und weitere Hilfe

**Sicherheits-Fragen:** support@superheld.app
**Notfall / Bug Report:** security@superheld.app
**Transparenz Reports:** https://superheld.app/transparency

---

## Weitere Ressourcen

- [Installation und Grundlagen](/docs/einführung/installation-v2)
- [Sichere Nutzung unterwegs](/docs/einführung/nutzung)
- [Erweiterte Sicherheits-Konfiguration](/docs/experten/konfiguration)
- [FAQ: Häufige Sicherheits-Fragen](/docs/einführung/faq)

---

**Deine Privatsphäre ist nicht verhandelbar.**
**superheld.app schützt sie, damit du dich auf das konzentrieren kannst, was dir wichtig ist.**
