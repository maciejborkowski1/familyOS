# Phase 1 — Personal Capture Agent: Release Plan

## Purpose

This document translates **Phase 1 (Capture)** of `roadmap.md` into a concrete,
sequenced delivery plan for the initial single-user validation described in
`vision.md` ("Current Starting Point"). Where `roadmap.md` defines the *why*
and *what* of Capture at the product level, this document defines *what ships,
in what order, and how we know each step is done* — scoped to a single user
(the author, as a parent) capturing personal parenting moments.

Two different things are tracked separately here, deliberately:

- **Milestones** — named, strategic checkpoints. Each has its own definition
  of done and can absorb as many versions as it actually needs.
- **Versions** — sequential build increments *within* a milestone, numbered
  as they actually ship, not pre-assigned to a fixed roadmap of dates or
  features.

---

## Milestones

| Milestone | Objective | Status |
|---|---|---|
| **M0 — Telegram Capture MVP** | Prove frictionless capture works as a sustained personal habit | In progress |
| **M1 — Story Bank Structure** | Build a 50-moment library, structured and ready as raw material for [(Nie)spokojny Tata] storytelling | Not started |
| **M2 — Mobile Migration** | Move the capture experience off Telegram into a dedicated app, without losing capture ease | Not started |
| **M3 — Public Launch** | Open the capture agent (or a derived product) to other users | Not started |

Monetization is intentionally **not** listed as a milestone here — it is a
separate business decision to be made once M3 is reached, not a synonym
for "feature complete."

---

## M0 — Telegram Capture MVP

### v0.1 — Draft capture

**Scope**
- Telegram bot receives a text or voice message.
- Message (raw text, or audio file reference) + timestamp is written to
  storage. Zero classification, zero structure.

**Explicitly out of scope**: tagging, transcription, follow-up questions.

**Tech**
- Capture channel: Telegram Bot API (webhook).
- Storage: Supabase (Postgres) table `moments`:
  `id, created_at, raw_text, audio_url, source`.

**Success means**
> Every message sent to the bot over a 2-week test period is durably
> stored and retrievable, with zero data loss.

### v0.2 — Transcription + light tagging

**Scope**
- Voice messages are automatically transcribed.
- 1–2 tags (e.g. "granice", "złość", "szkoła") are assigned automatically
  per moment. No follow-up questions yet.

**Explicitly out of scope**: deep structure, linking between moments.

**Tech additions**
- Transcription: Whisper API (provider TBD).
- Tagging: Claude API, single-pass classification call.

**Success means**
> 100% of captured moments receive automatic tags with no manual input;
> transcriptions are usable without correction in the large majority of
> cases.

### v0.3 — Deep questioning + structure

**Scope**
- After a raw capture, the bot asks 1–2 follow-up questions (in the same
  chat thread, at the user's own pace) to fill out the schema:
  **Situation → Emotions → Dilemma → Decision → Outcome → Reflection.**

**Explicitly out of scope**: connecting moments to books/podcasts,
suggesting frameworks, hooks, or content formats.

**Success means**
> A majority of captured moments reach "complete" structure (all six
> fields filled) within a few days of capture.

### v0.4+ — TBD within M0

Reserved for whatever M0 turns out to actually need — e.g. a simple
browsing/retrieval view, or export to a plain-text format for drafting.
Not planned in advance; assigned only once a real gap shows up in use.

---

## M1 — Story Bank Structure (deferred, not detailed yet)

Will include: linking captured moments to book/podcast notes (semantic
search via pgvector), surfacing possible frameworks, and reaching the
50-moment library target. Deliberately left undetailed until M0 is done —
detailing it now would be planning fiction.

**Worked example to keep in mind for later (not current scope):** if a
moment captured a week ago touches on a problem, and a podcast episode
consumed since then addresses that same problem, the system proactively
surfaces the link between them — e.g. "this episode covers what you
wrote about last week." This is the kind of proactive matching this
milestone is aiming at; it depends on M0 being solid first (nothing to
match against otherwise).

## M2 — Mobile Migration (deferred, not detailed yet)

Migration from Telegram to a native/mobile capture experience. Sized
independently once M0/M1 usage patterns are known — this is a much bigger
jump than any single M0 version and shouldn't be pre-numbered as if it
were one.

## M3 — Public Launch (deferred, not detailed yet)

Opening the tool to other users. Monetization is a separate decision made
after this milestone, not part of its definition of done.

---

## Security (applies from v0.1 onward)

These were decided in planning discussion but need to live here, not just
in conversation history, so they're visible to anyone (including Claude
Code) working on this repo:

- `.env` in `.gitignore` from the first commit — Supabase/Telegram keys
  never enter git history, especially since this repo is public.
- Row Level Security (RLS) enabled on the `moments` table, even for a
  single user — defense in depth if a key is ever exposed.
- `service_role` key used only in the local script, never in anything
  that could reach a client or a public repo; `anon` key is the only one
  ever safe to expose.
- Supabase project region set to EU (Frankfurt) — no cost difference,
  keeps family data in the EU.
- **Audio in Supabase Storage: private bucket, signed/expiring URLs —
  not `get_public_url()`.** A public bucket means anyone who obtains a
  stored URL can listen to the recording.

---

## Tech Stack Decision (effective as of v0.1)

| Concern | Choice | Why |
|---|---|---|
| Capture channel | Telegram Bot API | Zero-friction, native voice message support, no app to build yet |
| Storage | Supabase (Postgres, free tier) | Structured querying needed from v0.2; pgvector available for M1 semantic linking; matches the stated goal of learning cloud/API integration; avoids a migration off Google Drive/Sheets later |
| Transcription | Whisper API | Provider TBD |
| Tagging/classification | Claude API | Single-pass classification, no agentic complexity yet |

**Rejected for now:** Google Drive / Sheets as primary storage — fast to
start, but wouldn't support v0.2 tagging queries or M1 semantic linking
without a migration. Could still be used as a one-off, throwaway spike if
v0.1 needs to be validated in under 30 minutes before any setup — but not
as the foundation v0.2+ builds on.

---

## Out of Scope for all of Phase 1

- Multi-user / family-wide capture (deferred to a later roadmap phase per
  `vision.md`).
- Content generation — the capture agent's job ends at "structured
  moment," not "finished post." Drafting, filming, and editing content
  happens outside this tool.