import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
DEFAULT_TZ = os.getenv("DEFAULT_TZ", "Asia/Tashkent")
REMINDER_HOUR = int(os.getenv("REMINDER_HOUR", "11"))
CONFIRM_DEADLINE_HOUR = int(os.getenv("CONFIRM_DEADLINE_HOUR", "20"))
PROFILE = os.getenv("PROFILE", "MVP")
GOOGLE_OAUTH_CLIENT_JSON = os.getenv("GOOGLE_OAUTH_CLIENT_JSON", "")
PORT = int(os.getenv("PORT", "8000"))
