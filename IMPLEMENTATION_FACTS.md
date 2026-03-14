# IMPLEMENTATION_FACTS

> **Purpose:** This template must be filled in by the engineering/product team.
> Each answer directly unblocks one or more TODO markers across the documentation.
> Once completed, hand this file back so the docs can be updated with verified facts.

---

## 1. Voice Patterns / Anruf-Erkennung

**Docs blocker:** Multiple pages reference "Sprachmuster" / "voice patterns" without specifying the data source.

- [ ] Does the app access microphone audio during or after calls?
  - Answer:
- [ ] Does it use call metadata only (duration, caller ID, frequency, time-of-day)?
  - Answer:
- [ ] Does it use carrier-level signals (STIR/SHAKEN attestation, network reputation)?
  - Answer:
- [ ] If audio is accessed: is processing on-device only, or is any data sent to the cloud?
  - Answer:
- [ ] Recommended canonical term (pick one): `Anruf-Metadaten-Heuristik` / `Sprachmuster-Analyse` / other:
  - Answer:

**Affected pages:** scope-non-goals, detection-pipeline, core-concepts, privacy-security

---

## 2. LLM / KI-Modell Existence

**Docs blocker:** "Prompt-Manipulation" is listed as a threat category, implying an LLM exists in-product.

- [ ] Does the product contain or use an LLM (large language model) in any component?
  - Answer:
- [ ] If yes: what is it used for (classification, user-facing chat, content analysis)?
  - Answer:
- [ ] If yes: is it on-device, cloud-hosted, or hybrid?
  - Answer:
- [ ] If no LLM exists: should "Prompt-Manipulation" be replaced with "extern erzeugte KI-Betrugsinhalte" (AI-generated fraud content from external sources)?
  - Answer:

**Affected pages:** scope-non-goals, threat-model, detection-pipeline

---

## 3. Federated Learning

**Docs blocker:** Architecture page references "Modell-Updates ohne zentrale Rohdaten" but status is unclear.

- [ ] Is federated learning currently shipped in production?
  - Answer:
- [ ] If shipped: which models are trained this way?
  - Answer:
- [ ] If shipped: is participation opt-in or opt-out?
  - Answer:
- [ ] If shipped: what aggregation protocol is used (secure aggregation, DP-SGD, other)?
  - Answer:
- [ ] If not shipped: is it on the roadmap? Target timeline?
  - Answer:
- [ ] If not shipped: what is the current model update mechanism (centrally trained, manual push)?
  - Answer:

**Affected pages:** architecture, privacy-security, scope-non-goals, roadmap

---

## 4. Feature Vectors and Differential Privacy

**Docs blocker:** Architecture claims anonymized feature vectors are sent to cloud, but transforms and DP parameters are unspecified.

- [ ] What transforms are applied before a feature vector leaves the device?
  - Answer (e.g., dimensionality reduction, hashing, quantization):
- [ ] What is the dimensionality of the transmitted vector?
  - Answer:
- [ ] Is formal differential privacy (DP) applied?
  - Answer:
- [ ] If DP is applied: what are the privacy parameters?
  - ε (epsilon):
  - δ (delta):
  - Mechanism (Laplace, Gaussian, other):
- [ ] If DP is NOT applied: what privacy guarantee can be stated instead?
  - Answer:
- [ ] Can the cloud reconstruct the original input from the vector?
  - Answer (expected: no — but state the technical basis):

**Affected pages:** architecture, privacy-security, scope-non-goals, data-flows

---

## 5. Location / Geofencing

**Docs blocker:** privacy-security says "Keine Standortdaten" but configuration references geofencing in family profiles.

- [ ] Does the family "Standort-Benachrichtigung" feature exist in production?
  - Answer:
- [ ] If yes: is location processed entirely on-device?
  - Answer:
- [ ] If cloud-involved: what location data is transmitted (GPS coords, geofence zone ID, coarse region)?
  - Answer:
- [ ] What permissions are required (iOS CLLocationManager, Android ACCESS_FINE_LOCATION, etc.)?
  - Answer:
- [ ] Is location data stored? If so, for how long?
  - Answer:

**Affected pages:** privacy-security, configuration, platform-capabilities

---

## 6. Retention Periods

**Docs blocker:** Multiple pages reference data retention without specifying durations.

- [ ] Event log retention period:
  - Answer:
- [ ] Audit trail retention period:
  - Answer:
- [ ] Alert retention period:
  - Answer:
- [ ] Anonymized telemetry retention period:
  - Answer:
- [ ] User account data after deletion request:
  - Answer (e.g., "purged within 30 days"):
- [ ] Are retention periods configurable per customer/plan?
  - Answer:

**Affected pages:** telemetry, privacy-security, trust-center, configuration

---

## 7. Confidence Score Thresholds

**Docs blocker:** Detection pipeline references confidence scores but thresholds are unspecified.

- [ ] What is the confidence score range (e.g., 0.0–1.0)?
  - Answer:
- [ ] Default threshold for alert escalation:
  - Answer:
- [ ] Is the threshold configurable per policy?
  - Answer:
- [ ] Are thresholds different per threat category?
  - Answer:

**Affected pages:** detection-pipeline, core-concepts, configuration
