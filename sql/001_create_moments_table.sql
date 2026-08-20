create table if not exists moments (
    id bigint generated always as identity primary key,
    created_at timestamptz not null default now(),
    raw_text text,
    audio_url text,
    source text not null
);
