# CLAUDE.md

This file is read automatically at the start of every Claude Code session
in this repository. It exists so implementation work can pick up exactly
where product/planning discussions (done elsewhere, in chat) left off,
without needing to re-explain context each time.

## What this project is

FamilyOS's first product is built around a single, durable actor: **the
parent**. The core problem — capturing and reflecting on meaningful
parenting moments — is inherently personal, even in a mature version of
the product: each parent would keep their own library, not a shared one.
This is different from shared family-coordination tools (calendar, tasks,
finances), which are not assumed to be part of FamilyOS's scope. See
`doc/vision.md` ("Current Starting Point") for the full reasoning.

Note on language: "parent," not "father" — the capture problem itself
isn't gender-specific. "Father" belongs to (Nie)spokojny Tata's voice and
branding, not to this product.

The current build target is a **personal capture agent**: a frictionless
way to save parenting moments (via Telegram) that later become structured
raw material for a separate personal-brand storytelling project,
"(Nie)spokojny Tata" (not part of this repo).

## Where the real source of truth lives

Read these before making any product/scope decisions — don't infer scope
from code alone:

- `doc/vision.md` — long-term product vision, and the single-user starting
  point.
- `doc/roadmap.md` — the four phases (Capture → Organize → Assist →
  Anticipate), what each phase does and does not include.
- `doc/release-plan-phase1.md` — the actual delivery plan for Phase 1:
  milestones (M0–M3) and the specific versions within M0 (v0.1, v0.2,
  v0.3...), each with explicit in-scope / out-of-scope boundaries and a
  "Success means" criterion.
- `CHANGELOG.md` — what has actually shipped, version by version,
  including fixes found after the fact. Check this for current status;
  the release plan describes intent, not status.

**If a task isn't described in one of these docs, treat that as a signal
to stop and ask, not to improvise scope.**

## Current status

- Active milestone: **M0 — Telegram Capture MVP**
- Active version: **v0.1.1 — in progress.** Fixing gaps found in the
  v0.1 review: making the `voice-notes` bucket private with signed URLs,
  confirming RLS on `moments`, confirming EU region. See `CHANGELOG.md`
  for exact scope and `doc/v0.1-summary.md` for how these were found.
- **Not yet validated:** the 2-week real-usage test from v0.1's success
  criterion hasn't run yet — run it in parallel with the v0.1.1 fixes.
- Update this section (and `CHANGELOG.md`) whenever a version ships or
  the active target changes, so the next session starts accurate.

## Architecture decisions already made

- **Capture channel:** Telegram Bot API, **polling mode** (not webhook) —
  deliberately, so this can run on a local machine with no public
  IP/HTTPS endpoint, no tunnel (ngrok/Cloudflare Tunnel), no port
  forwarding.
- **Storage:** Supabase (Postgres, free tier) — chosen over Google
  Drive/Sheets because v0.2+ needs structured queries (tags), and Phase 1
  M1 will need pgvector for semantic linking. Table: `moments` (`id`,
  `created_at`, `raw_text`, `audio_url`, `source`; `transcript` and `tags`
  added in v0.2).
- **Transcription:** Whisper API (provider TBD).
- **Tagging/classification:** Claude API, single-pass call, no agentic
  complexity yet.
- **Orchestration:** a small local Python script (not n8n) for v0.1 —
  n8n's Telegram Trigger node requires a public HTTPS webhook, which
  conflicts with the "no public server" constraint. n8n may be
  reconsidered later if a tunnel is set up deliberately.
- Every version's raw input is stored even before it's processed (e.g.
  `audio_url` is saved in v0.1 even though transcription doesn't exist
  yet), so later versions can backfill older records instead of losing
  data. Any backfill script must be idempotent — safe to re-run, only
  touching records with an empty target field.

## Explicitly out of scope right now

- Multi-user / family-wide capture
- Content generation (drafting, filming, editing posts) — this repo's
  job ends at "structured moment," not "finished content"
- Mobile app, public launch, monetization — all deferred to later
  milestones (see `doc/release-plan-phase1.md`)

## Working conventions

- Product/scope decisions happen in chat/planning first, then get
  written into `doc/`. Claude Code should treat `doc/` as authoritative
  over any assumption made mid-session.
- Prefer the smallest version that proves the next thing — don't build
  ahead of the current milestone's explicit scope.