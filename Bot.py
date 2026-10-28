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