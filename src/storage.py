import uuid

from supabase import Client, create_client

import config

_client: Client = create_client(config.SUPABASE_URL, config.SUPABASE_SERVICE_KEY)

VOICE_BUCKET = "voice-notes"


def save_moment(raw_text: str | None, audio_url: str | None, source: str) -> dict:
    result = (
        _client.table("moments")
        .insert({"raw_text": raw_text, "audio_url": audio_url, "source": source})
        .execute()
    )
    return result.data[0]


def upload_audio(file_bytes: bytes, extension: str) -> str:
    path = f"{uuid.uuid4()}.{extension}"
    _client.storage.from_(VOICE_BUCKET).upload(
        path, file_bytes, {"content-type": "audio/ogg"}
    )
    return _client.storage.from_(VOICE_BUCKET).get_public_url(path)
