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
DB_PATH = DATA_AIR / "massages.db"


logging.basicConfig(
    format = "%(asctime)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
logging.getLogger("httpsx").setLevel(logging.WARNING)


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
            "Welcome to Nazanin(Leonika)s bot.\n"
            "Your message will be sent anonymously.\n"
            "Please enter your message: (text, file, picture)"
        )
    await update.effective_message.reply_text(text)
