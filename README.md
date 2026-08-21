# FamilyOS

FamilyOS is a personal "operating system" for family life — currently
being built and validated as a single-user product for the author, as a
parent.

## What it does today

The current build is a **personal capture agent**: a frictionless way to
save meaningful parenting moments — via a Telegram bot, as text or voice
notes — without needing to organize them first. Captured moments become
the raw material for later reflection and storytelling, structured
around a simple schema (situation → emotions → dilemma → decision →
outcome → reflection).

This is Phase 1 (**Capture**) of a longer-term roadmap: Capture →
Organize → Assist → Anticipate.

## Status

**v0.1.1** — draft capture is live: a locally-run Telegram bot (polling
mode, no public server required) stores text and voice moments in
Supabase. See `CHANGELOG.md` for exact version history.

## Tech stack

- **Capture:** Telegram Bot API (long-polling)
- **Storage:** Supabase (Postgres + Storage), EU region
- **Orchestration:** a local Python script — no cloud hosting required
  for this stage

## Documentation

| File | What it answers |
|---|---|
| `doc/vision.md` | Why this exists, and who it's for |
| `doc/roadmap.md` | The four phases and what each one does/doesn't cover |
| `doc/release-plan-phase1.md` | What's planned for Phase 1, version by version |
| `CHANGELOG.md` | What actually shipped, and when |
| `doc/v0.1-summary.md` | Technical deep-dive on the v0.1 implementation |
| `CLAUDE.md` | Current status and context for AI-assisted development |

## Explicitly out of scope (for now)

- Multi-user / shared-family use
- Content generation (this repo stops at "structured moment," not
  "finished post")
- Mobile app, public availability, monetization