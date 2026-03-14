---
title: "Use Cases & Szenarien"
weight: 35
aliases:
  - /docs/use-cases
---

## superheld.app für verschiedene Szenarien

Entdecke, wie superheld.app in deinem spezifischen Fall hilft.

---

## Szenario 1: Startup-Gründer

<div class="sh-gallery">
  <div class="sh-gallery-phone">
    <div class="sh-screenshot">
      <img src="/images/screenshot-api-vault.svg" alt="superheld.app API Vault — verschlüsselte API-Keys mit Audit Trail" loading="lazy">
    </div>
  </div>
</div>

### Das Problem

- Wie halte ich Finanzpläne geheim?
- Wie teile ich Code sicher mit dem Team?
- Wie schütze ich Investor-Gespräche?
- Wie speichere ich API-Keys sicher?

### Superheld-Lösung

{{< details title="Dokumente & Investor-Updates" >}}

**Finanzierungsrunde-Daten**
- Direkt zur superheld-Gruppe "Investors"
- Automatisch E2E-verschlüsselt
- Nur autorisierte Gründer und Partner können zugreifen

**Pitch-Decks**
- Upload zu superheld
- Teilbar mit Ablaufdatum
- Nachverfolgung, wer das Dokument gelesen hat

**Verträge & Legal-Dokumente**
- Sichere Speicherung
- Versionierung aller Änderungen
- Signatur-Integration

{{< /details >}}

{{< details title="Team-Kommunikation mit API-Keys" >}}

**Herausforderung:** Das DevOps-Team benötigt AWS-Credentials.

**Herkömmlicher Weg (unsicher):**
- API-Key per E-Mail versenden
- Key wird überall kopiert und ist ungeschützt

**superheld.app Weg (sicher):**
1. Settings → API Vault öffnen
2. Neuen Key anlegen: "AWS Production"
3. Credential eingeben
4. superheld verschlüsselt und speichert den Key
5. Team-Mitglieder sehen den Key nie im Klartext
6. Key ist nur in Workflows nutzbar
7. Jeder Zugriff wird im Audit Trail protokolliert

{{< /details >}}

{{< details title="Skalierung ohne Sicherheitsrisiko" >}}

**Situation:** Alle 3 Monate kommen 5 neue Team-Mitglieder hinzu.

superheld.app stellt sicher:
- Neue Accounts werden mit 2FA angelegt
- Granulare Berechtigungen nach Rolle:
  - **Founders:** Vollzugriff
  - **Engineers:** Code & Infrastruktur
  - **Marketing:** Kampagnen
  - **Finance:** Budgets
- Audit Trail dokumentiert, wer was getan hat
- Automatische Prüfung der Logs auf Sicherheitsvorfälle

{{< /details >}}

---

## Szenario 2: Investigativer Journalist

<div class="sh-gallery">
  <div class="sh-gallery-phone">
    <div class="sh-screenshot">
      <img src="/images/screenshot-secure-chat.svg" alt="superheld.app Sichere Quelle — E2E-verschlüsselter Chat mit Auto-Delete" loading="lazy">
    </div>
  </div>
</div>

### Das Problem

- Quellen müssen anonym bleiben
- Regierungen versuchen, Zugang zu blockieren
- Daten könnten gelöscht werden
- Metadaten sind fast so wichtig wie Inhalte

### Superheld-Lösung

{{< details title="Sichere Quellen-Verwaltung" >}}

**1. Kontaktaufnahme der Quelle**
- Quelle kontaktiert dich über einen superheld-Link
- Der Link enthält kein Tracking
- Quelle muss lediglich einen kostenlosen Account erstellen

**2. Sichere Konversation**
- Vollständig E2E-verschlüsselt
- Nur du und die Quelle sehen die Chats
- Vollständige Plausible Deniability – die Quelle kann die Kommunikation abstreiten

**3. Sensible Dokumente**
- Upload zur Gruppe "Research"
- Nur freigegebene Journalisten haben Zugriff
- Automatisierte Löschung nach einer festgelegten Frist

{{< callout type="info" >}}
**Auto-Delete Feature:** Nachrichten und Dokumente werden nach 30 Tagen unwiderruflich gelöscht. Nicht wiederherstellbar. Ideal für sensible Recherchen.
{{< /callout >}}

{{< /details >}}

{{< details title="Investigative Tools Integration" >}}

superheld verbindet spezialisierte Tools sicher miteinander:

- **Signal (Encrypted Messaging):** Export und Backup zu superheld
- **ProPublica Secure Drop:** Dokumente importieren
- **Off-the-Record Chats:** Transkripte E2E-verschlüsselt speichern
- **FOIA Requests:** Alle Antworten zentral und verschlüsselt ablegen

Alles an einem Ort. Alles privat. Alles nachverfolgbar.

{{< /details >}}

{{< details title="Sichere Team-Redaktion" >}}

**Workflow für gemeinsame Recherchen:**

1. Edit-Gruppe mit ausschließlich autorisierten Personen
2. Draft-Versionierung – wer hat was geändert?
3. Fact-Check-Checkliste
4. Legal-Review-Prozess
5. Redaction-Tools zum Schwärzen sensibler Informationen
6. Veröffentlichung mit Zeitstempel

**Regulatorische Anforderungen:**
- Audit Trail aller Änderungen
- DSGVO-konform
- Erfüllt Newsroom-Standards

{{< /details >}}

---

## Szenario 3: Medizinische Praxis

<div class="sh-gallery">
  <div class="sh-gallery-wide">
    <div class="sh-screenshot">
      <img src="/images/screenshot-patientenakte.svg" alt="superheld.app Patientenakte — Zugriffssteuerung und Diagnosen" loading="lazy">
    </div>
  </div>
</div>

### Das Problem

- Patientendaten müssen HIPAA-konform gespeichert werden
- Zweitmeinungen sollen vertraulich bleiben
- Telemedizin erfordert Verschlüsselung
- Team-Kommunikation muss über Schichten hinweg funktionieren

### Superheld-Lösung

{{< details title="Patientendaten sicher verwalten" >}}

Jeder Patient erhält einen eigenen Ordner in superheld mit folgender Struktur:

- Krankengeschichte (E2E-verschlüsselt)
- Laborergebnisse (mit Scan-Datum)
- Rezepte (Link mit Code statt PDF)
- Behandlungen und Notizen
- Nachsorge-Checklisten
- Versicherungsdokumentation

**Zugriffssteuerung (Beispiel):**

| Rolle | Zugriff |
|---|---|
| Hausarzt | Vollzugriff |
| Fachärzte (falls relevant) | Vollzugriff |
| Rezeptionistin | Kein Zugriff auf Diagnosen |
| Reinigungspersonal | Kein Zugriff |
| Praktikanten | Kein Zugriff |

{{< callout type="info" >}}
superheld erfüllt alle relevanten Anforderungen: Access Control, Audit Logs, 256-Bit Encryption, Disaster Recovery und Business Associate Agreements.
{{< /callout >}}

{{< /details >}}

{{< details title="Sichere Zweitmeinungen" >}}

**Ablauf für eine Zweitmeinung:**

1. **Share-Link erstellen:** Dr. Schmidt erstellt einen Link mit allen relevanten Daten, einer Gültigkeit von 7 Tagen und Passwortschutz.
2. **Link weiterleiten:** Der Patient sendet den Link an den zweiten Arzt. Dieser erhält ausschließlich Lesezugriff, kann keine Daten verändern und muss ein Passwort eingeben.
3. **Antwort in superheld:** Der zweite Arzt antwortet direkt in superheld. Die Zweitmeinung wird gespeichert und ist für Patient sowie Originalarzt einsehbar – ohne ungesicherte E-Mails.

{{< /details >}}

{{< details title="Telemedizin & Follow-ups" >}}

**superheld Video-Integration:**

1. Integriertes Video (E2E-verschlüsselt)
2. Automatische Aufzeichnung und Transkription
3. Digitale Signatur von Patient und Arzt
4. Automatische Dokumentation
5. Follow-up-Termine werden automatisch geplant

**Sicherheitsgarantien:**
- Kein unbefugter Zugriff auf Videocalls
- Aufnahmen werden nicht weitergeleitet
- Nur Arzt und Patient können zugreifen
- HIPAA-konform

{{< /details >}}

---

## Szenario 4: Internationale NGO

<div class="sh-gallery">
  <div class="sh-gallery-wide">
    <div class="sh-screenshot">
      <img src="/images/screenshot-ngo-teams.svg" alt="superheld.app Team-Übersicht — 4 globale Standorte mit Zeitzonen" loading="lazy">
    </div>
  </div>
</div>

### Das Problem

- Teams in Ländern mit staatlicher Überwachung
- Spenderdaten müssen vertraulich bleiben
- Kampagnen sind sensibel
- Internationales Team mit verschiedenen Sprachen

### Superheld-Lösung

{{< details title="Globale Team-Kommunikation" >}}

**Beispiel: Netzwerk gegen Menschenhandel**

Teams verteilt auf mehrere Standorte:
- **Indien** – Advocacy
- **Philippinen** – Field Operations
- **Bangladesch** – Dokumentation
- **USA** – Policy & Fundraising

**superheld.app Setup:**
- Alle Teams in einem Workspace
- Lokale Gruppen (z. B. "India Team")
- Globale Gruppen (z. B. "All Leads")
- Campaign Management
- Zeitzonen-bewusstes Scheduling
- Multi-Language Support

Jeder kann in seiner Sprache arbeiten. Alles bleibt E2E-verschlüsselt.

{{< /details >}}

{{< details title="Spender & Transparenz" >}}

**Berechtigungen für Spender:**

| Zugriff gewährt | Kein Zugriff |
|---|---|
| Impact Reports (verschlüsselt) | Sensible Operationen |
| Budget Tracking | Team-Mitglieder-Daten |
| Field Reports | Strategie und Planung |

**Audit Trail dokumentiert:**
- Wann wurde ein Report gelesen?
- Wer hat Fragen gestellt?
- Wie wurde geantwortet?

{{< /details >}}

---

## Szenario 5: Compliance Officer

<div class="sh-gallery">
  <div class="sh-gallery-wide">
    <div class="sh-screenshot">
      <img src="/images/screenshot-compliance.svg" alt="superheld.app Compliance Dashboard — KPIs, Alerts und Audit Logs" loading="lazy">
    </div>
  </div>
</div>

### Das Problem

- GDPR-, HIPAA- und CCPA-Compliance sicherstellen
- Audit Trails für Regulierungsbehörden vorhalten
- Data Retention Policies umsetzen
- Breach Notification Plans bereithalten

### Superheld-Lösung

{{< details title="Built-in Compliance" >}}

superheld.app bringt umfassende Compliance-Funktionen mit:

**GDPR:**
- Right to be Forgotten (Account-Löschung)
- Data Portability (vollständiger Datenexport)
- Consent Management
- Data Processing Agreements

**HIPAA:**
- Access Controls
- Audit & Accounting of Disclosures
- Encryption at Rest und in Transit
- Business Associate Agreements

**CCPA:**
- Consumer Rights (Datenzugriff und -löschung)
- Opt-Out Tracking
- Disclosure Requirements

{{< /details >}}

{{< details title="Audit Logs & Monitoring" >}}

**Compliance-Dashboard (Beispiel, letzte 90 Tage):**

- 1.234 Login-Events
- 45 Zugriffsänderungen
- 0 unautorisierte Zugriffsversuche
- 12 Datenexporte
- Durchschnittlich 3 Passwortänderungen pro Nutzer

**Automatische Alerts:**
- Mehrere fehlgeschlagene Logins
- Unerwartete Zugriffe
- Bulk-Downloads

**Exportierbare Reports:**
- Nach Nutzer
- Nach Zeitraum
- Nach Aktionstyp

{{< /details >}}

---

## Szenario 6: Freelancer und Consultant

<div class="sh-gallery">
  <div class="sh-gallery-phone">
    <div class="sh-screenshot">
      <img src="/images/screenshot-workspaces.svg" alt="superheld.app Workspaces — isolierte Kunden-Workspaces" loading="lazy">
    </div>
  </div>
</div>

### Das Problem

- Jeder Kunde hat sensible Daten
- Kundendaten müssen voneinander isoliert sein
- Verträge und Rechnungen sicher verwalten
- Einfache Abrechnung gewährleisten

### Superheld-Lösung

{{< details title="Kunden-Workspaces" >}}

**Workspace-Struktur für Consultants:**

1. **Main Workspace (privat)**
   - Eigene Rechnungen
   - Eigene Verträge
   - Eigene Notizen

2. **Client A Workspace**
   - Nur du und das Team von Client A haben Zugriff
   - 100 % getrennt von Client B

3. **Client B Workspace**
   - Nur du und das Team von Client B haben Zugriff
   - 100 % getrennt von Client A

**Sicherheit:**
- Daten sind streng voneinander isoliert
- Client A kann den Workspace von Client B nicht sehen
- Ein Login für alle Workspaces (mit 2FA)
- Automatische Abrechnung pro Workspace

{{< /details >}}

{{< details title="Sichere Vertragsarbeit" >}}

**superheld.app Workflow:**

1. Client sendet eine Anfrage über superheld
2. Du erstellst ein Proposal im integrierten Editor
3. Client prüft und kommentiert
4. Gemeinsame Verfeinerung – alle Versionen werden gespeichert
5. Digitale Signatur mit authentischem Zeitstempel
6. Automatische Rechnungsstellung nach vereinbarter Frist
7. Payment-Tracking
8. Projektabschluss und Archivierung

{{< /details >}}

---

## Welche Seite passt zu meinem Szenario?

{{< callout type="info" >}}
- [Installation](/docs/einführung/installation-v2) – Schnell starten
- [Konfiguration](/docs/experten/konfiguration) – Alles anpassen
- [Sicherheit](/docs/experten/privacy-sicherheit) – Technische Details
- [FAQ](/docs/einführung/faq) – Häufige Fragen
{{< /callout >}}

---

**Bereit?** [Installation →](/docs/einführung/installation-v2)
