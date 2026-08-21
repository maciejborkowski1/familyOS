# Changelog

All notable changes to the FamilyOS personal capture agent are recorded
here, in reverse chronological order. This is a record of what actually
shipped — for what's planned, see `doc/release-plan-phase1.md`.

Format loosely follows [Keep a Changelog](https://keepachangelog.com/):
each entry uses **Added** / **Changed** / **Fixed** / **Security** as
needed.

## v0.1.1 — fixes for v0.1 - released 21.08.2026

### Security
- Fixed: `voice-notes` Supabase Storage bucket was public
  (`get_public_url()`); switched to a private bucket with signed,
  expiring URLs.
- Confirmed/fixed: Row Level Security (RLS) enabled on the `moments`
  table.
- Confirmed: Supabase project region is EU (Frankfurt).

Found during the v0.1 technical review (`doc/v0.1-summary.md`) — see
that doc for how the gap was discovered.

## v0.1 — draft capture - released 20.08.2026

### Added
- Telegram bot (`src/bot.py`) using long-polling (no public
  webhook/tunnel needed).
- Text and voice message handlers; voice messages downloaded from
  Telegram and uploaded to Supabase Storage.
- Supabase integration (`src/storage.py`): `moments` table insert via
  the Data API (PostgREST), using the `service_role` key.
- `moments` table schema (`sql/001_create_moments_table.sql`):
  `id`, `created_at`, `raw_text`, `audio_url`, `source`.
- Local launcher (`run_bot.ps1`) with duplicate-run guard and logging.
- `.env`-based secrets, excluded from git from the first commit.

### Known gaps at release (see v0.1.1 above for fixes)
- Audio bucket was public rather than private.
- 2-week real-usage validation (the version's success criterion) not
  yet run.