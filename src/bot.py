import logging

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

import config
import storage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    storage.save_moment(raw_text=update.message.text, audio_url=None, source="telegram")
    await update.message.reply_text("Zapisano.")


async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    voice = update.message.voice
    file = await context.bot.get_file(voice.file_id)
    file_bytes = bytes(await file.download_as_bytearray())
    audio_path = storage.upload_audio(file_bytes, extension="ogg")
    storage.save_moment(raw_text=None, audio_url=audio_path, source="telegram")
    await update.message.reply_text("Zapisano.")


def main() -> None:
    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    logger.info("Bot starting (polling)...")
    app.run_polling()


if __name__ == "__main__":
    main()
