# API_FACTS

> **Purpose:** This template must be filled in by the engineering team.
> Each answer unblocks TODO markers in the OpenAPI spec and API documentation pages.
> Once completed, hand this file back so `openapi.yaml` and docs can be updated.

---

## 1. API Version and Environments

- [ ] Current production API version:
  - Answer:
- [ ] Base URL (confirm or correct): `https://api.superheld.app/api/v1/`
  - Answer:
- [ ] Are there staging/sandbox environments?
  - Answer:
- [ ] Staging base URL (if applicable):
  - Answer:

---

## 2. Authentication

- [ ] Token format: JWT, opaque, or other?
  - Answer:
- [ ] API key prefixes (confirm): `sh_live_*` (production), `sh_test_*` (test)?
  - Answer:
- [ ] Is OAuth2 supported in production?
  - Answer:
- [ ] If OAuth2: authorization URL:
  - Answer:
- [ ] If OAuth2: token URL:
  - Answer:
- [ ] If OAuth2: supported grant types (authorization_code, client_credentials, etc.):
  - Answer:
- [ ] Available OAuth2 scopes (list all):
  - Answer:
- [ ] Token expiry duration:
  - Answer:
- [ ] Refresh token support?
  - Answer:

---

## 3. Endpoint Confirmation

For each endpoint below, confirm: **exists (Y/N)**, **correct method**, **correct path**, **auth required**.

| # | Method | Path | Exists? | Correct path? | Auth? | Notes |
|---|--------|------|---------|---------------|-------|-------|
| 1 | GET | `/devices` | | | | |
| 2 | GET | `/devices/{id}` | | | | |
| 3 | GET | `/threats` | | | | |
| 4 | GET | `/threats/{id}` | | | | |
| 5 | GET | `/events` | | | | |
| 6 | GET | `/events/{id}` | | | | |
| 7 | POST | `/events/{id}/acknowledge` | | | | |
| 8 | GET | `/policies` | | | | |
| 9 | PUT | `/policies/{id}` | | | | |
| 10 | GET | `/alerts` | | | | |

**Additional endpoints not listed above:**
- (add any missing endpoints here)

### Canonical integration model: `/events` vs `/threats`

The docs currently use both `/events` and `/threats` as integration endpoints. Clarify the relationship:

- [ ] Is `/events` the canonical append-only event stream (powering SIEM, webhooks, polling)?
  - Answer:
- [ ] Is `/threats` a derived entity view (latest state per threat, deduplicated)?
  - Answer:
- [ ] Or is the relationship different? Describe:
  - Answer:
- [ ] Which endpoint should integrators poll as their primary feed?
  - Answer:

---

## 4. Request/Response Details

### Pagination
- [ ] Pagination style: cursor-based, offset-based, or page-based?
  - Answer:
- [ ] Default page size:
  - Answer:
- [ ] Maximum page size:
  - Answer:
- [ ] Pagination parameters (e.g., `cursor`, `offset`, `limit`, `page`):
  - Answer:

### Rate Limiting
- [ ] Rate limit per API key:
  - Answer (e.g., "100 req/min"):
- [ ] Rate limit headers returned (e.g., `X-RateLimit-Remaining`):
  - Answer:
- [ ] HTTP status code when rate limited:
  - Answer (expected: 429):

### Error Format
- [ ] Error response schema (confirm or provide):
  ```json
  {
    "error": {
      "code": "string",
      "message": "string"
    }
  }
  ```
  - Correct? Adjustments:

---

## 5. Webhook Contract

- [ ] Webhook signature header name (confirm): `X-Superheld-Signature`?
  - Answer:
- [ ] Signing algorithm (confirm): HMAC-SHA256?
  - Answer:
- [ ] Replay protection header (confirm): `X-Superheld-Timestamp`?
  - Answer:
- [ ] Replay window (e.g., "reject if timestamp > 5 min old"):
  - Answer:
- [ ] Idempotency key header: `X-Superheld-Event-Id`?
  - Answer:
- [ ] Retry policy (how many retries, backoff strategy):
  - Answer:
- [ ] DLQ (dead letter queue) available?
  - Answer:
- [ ] Supported event types (list all):
  - Answer:

---

## 6. Schema Confirmation

### Device object — confirm fields:
| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `device_id` | string (UUID) | | |
| `name` | string | | |
| `platform` | enum (android, ios, windows, macos, linux) | | |
| `os_version` | string | | |
| `agent_version` | string | | |
| `status` | enum (active, inactive, compromised) | | |
| `last_seen` | datetime (ISO 8601) | | |
| (additional fields?) | | | |

### Event object — confirm fields:
| Field | Type | Required? | Notes |
|-------|------|-----------|-------|
| `event_id` | string (UUID) | | |
| `timestamp` | datetime (ISO 8601) | | |
| `device_id` | string (UUID) | | |
| `threat_category` | enum | | |
| `confidence` | number (0.0–1.0) | | |
| `action_taken` | enum | | |
| `policy_id` | string | | |
| `severity` | enum (critical, high, medium, low, info) | | |
| `description` | string | | |
| `indicators` | object | | |
| `metadata` | object | | |
| (additional fields?) | | | |

### Threat categories — confirm enum values:
- [ ] `phone_scam`
- [ ] `social_engineering`
- [ ] `malicious_app`
- [ ] `phishing`
- [ ] `remote_control`
- [ ] `deepfake`
- [ ] (additional categories?)

---

## 7. Versioning and Deprecation

- [ ] API versioning strategy: URL path (`/v1/`), header, query param?
  - Answer:
- [ ] Deprecation notice mechanism (header, changelog, email)?
  - Answer:
- [ ] Current deprecation timeline (e.g., "6 months notice"):
  - Answer:
