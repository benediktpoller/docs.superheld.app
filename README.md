# docs.superheld.app

[![Build & Validate](https://github.com/benediktpoller/docs.superheld.app/workflows/Astro%20Docs%20Validation/badge.svg)](https://github.com/benediktpoller/docs.superheld.app/actions)
[![Accessibility](https://github.com/benediktpoller/docs.superheld.app/workflows/WCAG%20AAA%20Accessibility%20Tests/badge.svg)](https://github.com/benediktpoller/docs.superheld.app/actions)

Official documentation for **[superheld.app](https://superheld.app)** — enterprise-grade threat detection for social engineering, fraud, and digital manipulation.

**Live site:** [docs.superheld.app](https://docs.superheld.app)

## Stack

- **[Astro](https://astro.build/) 6** + **[Starlight](https://starlight.astro.build/) 0.38** — static site generator
- **[Mermaid](https://mermaid.js.org/)** — architecture and data flow diagrams
- **OpenAPI 3.1** — canonical API contract at `/openapi.yaml`

## Quick start

```bash
cd astro-site
npm install
npm run dev        # http://localhost:4321
```

Build for production:

```bash
npm run build      # output in astro-site/dist/
npm run preview    # preview production build
```

## Project structure

```
docs.superheld.app/
├── astro-site/                        # Astro project (primary)
│   ├── astro.config.mjs               # Starlight + Mermaid config
│   ├── public/
│   │   └── openapi.yaml               # OpenAPI 3.1 contract (draft)
│   └── src/content/docs/
│       ├── getting-started/           # Onboarding (7 pages)
│       ├── experts/                   # Concepts, guides, trust (32 pages)
│       │   └── spec/                  # Engineering specifications (12 pages)
│       └── index.mdx                  # Landing page
├── tests/                             # Playwright tests
├── .github/workflows/
│   ├── astro-validate.yml             # Build, lint, link check, drift gate
│   ├── accessibility.yml              # WCAG AAA tests
│   └── build-deploy.yml              # Netlify deployment
├── IMPLEMENTATION_FACTS.md            # Engineering fact sheet (unfilled)
├── API_FACTS.md                       # API fact sheet (unfilled)
└── README.md
```

## Documentation architecture

The site follows the [Diataxis](https://diataxis.fr/) framework:

| Section | Path | Intent | Pages |
|---|---|---|---:|
| Getting Started | `/getting-started/` | Tutorials + orientation | 7 |
| Experts | `/experts/` | Concepts, guides, reference, trust | 32 |
| Engineering Specs | `/experts/spec/` | Implementation specifications | 12 |
| **Total** | | | **52** |

### Engineering specifications

The `/experts/spec/` section contains implementation-facing specifications with a structured TODO-ENG backlog (48 items, 20 P1 blockers). Open questions are tracked with stable `TODO-ENG-###` IDs linked to two engineering fact sheets:

- `IMPLEMENTATION_FACTS.md` — voice/audio, feature vectors, DP parameters, scoring, retention
- `API_FACTS.md` — endpoints, schemas, auth, webhooks, pagination

See [TODO-ENG Summary](https://docs.superheld.app/experts/spec/todo-summary/) for the full backlog.

## CI pipeline

The `astro-validate.yml` workflow runs on every push to `main`:

| Step | Tool | Status |
|---|---|---|
| Build | `astro build` | Blocking |
| OpenAPI lint | Redocly CLI (`minimal`) | Blocking |
| Sitemap validation | Shell checks | Blocking |
| Page drift | Test list vs build output | Blocking |
| Internal link check | lychee (`--offline`) | Blocking |
| Endpoint drift | Docs vs OpenAPI paths | Informational |

## Enterprise-ready status

**NO** — 48 TODO-ENG items remain (20 P1 blockers). The path to "enterprise-ready" requires:

1. Engineering fills `IMPLEMENTATION_FACTS.md` and `API_FACTS.md`
2. TODO-ENG items resolved with confirmed facts
3. OpenAPI 3.1 finalized and linted at `recommended-strict`
4. RFC 9116 `security.txt` deployed at `/.well-known/security.txt`
5. Endpoint drift gate escalated to blocking

## License

MIT
