from pathlib import Path
import logging
import os
import sqlite3

from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ChatType
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

if not BOT_TOKEN or not OWNER_ID:
    raise RuntimeError("BOT_TOKEN or OWNER_ID are not set.")

OWNER_ID = int(OWNER_ID)


DATA_AIR = Path(os.getenv("DATA_AIR", str(Path(__file__).parent)))
DATA_AIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_AIR / "messages.db"


logging.basicConfig(
    format = "%(asctime)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                owner_message_id INTEGER PRIMARY KEY,
                sender_chat_id INTEGER NOT NULL
            )
        """)


def save_messages(owner_message_id: int, sender_chat_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO messages
            (owner_message_id, sender_chat_id)
            VALUES (?, ?)
            """,
            (owner_message_id, sender_chat_id),
        )


def get_sender(owner_message_id: int):
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT sender_chat_id FROM messages "
            "WHERE owner_message_id = ?",
            (owner_message_id,),
        ).fetchone()
    return row[0] if row else None


async def start(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE, 
):
    chat_id = update.effective_chat.id
    if chat_id == OWNER_ID:
        text = (
            "Anon box message is active.\n"
            "Reply to any messages to answer the messager."
        )
    else:
        text = (
            "Welcome to my envoy bot. 🙋🏻‍♀️ \n"
            "Your message will be sent anonymously.\n"
            "Please enter your message: (text, file or picture)"
        )
    await update.effective_message.reply_text(text)



async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    message = update.effective_message
    chat = update.effective_chat

    if message is None or chat is None:
        return

    if chat.type != ChatType.PRIVATE:
        return

    if chat.id == OWNER_ID:
        replied = message.reply_to_message
        if replied is None:
            return

        sender_id = get_sender(replied.message_id)
        if sender_id is None:
            await message.reply_text("Couldn't find the sender.")
            return

        try:
            await context.bot.copy_message(
                chat_id=sender_id,
                from_chat_id=OWNER_ID,
                message_id=message.message_id,
            )
            await message.reply_text("Message sent.")

        except Exception:
            logging.exception("Could not deliver the reply.")
            await message.reply_text("Couldn't deliver the reply.")
        return

    supported = (
        message.text is not None
        or bool(message.photo)
        or message.document is not None
    )

    if not supported:
        await message.reply_text("Only text, pictures, or files are acceptable.")
        return

    try:
        copied = await context.bot.copy_message(
            chat_id=OWNER_ID,
            from_chat_id=chat.id,
            message_id=message.message_id,
        )

        save_messages(copied.message_id, chat.id)

        await message.reply_text(
            "Message sent.\n"
            "If I reply to your message, you'll receive it here. 💁🏻‍♀️")

    except Exception:
        logging.exception("Could not deliver message.")
        await message.reply_text("Couldn't deliver your message. Please try again in a few minutes.")


def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

    logging.info("Bot is starting.")
    app.run_polling()


if __name__ == "__main__":
    main()