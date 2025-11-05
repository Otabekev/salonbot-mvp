import asyncio, threading, pytz
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime, timedelta
from dateutil import tz

from app.core.config import BOT_TOKEN, DEFAULT_TZ, PORT
from app.core.db import init_db, SessionLocal
from app.models.user import User
from app.models.salon import Salon
from app.models.service import Service

# --- FastAPI server in background (for /health and future OAuth) ---
def run_api():
    import uvicorn
    from app.web.main import app
    uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="info")

def start_api_thread():
    t = threading.Thread(target=run_api, daemon=True)
    t.start()

# --- Bot setup ---
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

LANGS = ["🇺🇿 O‘zbek", "🇷🇺 Русский", "🇬🇧 English"]

@dp.message(F.text == "/start")
async def start(m: Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for l in LANGS: kb.add(KeyboardButton(l))
    await m.answer("Tilni tanlang / Выберите язык / Choose language:", reply_markup=kb)

@dp.message(F.contact)
async def got_contact(m: Message):
    with SessionLocal() as s:
        u = s.query(User).filter_by(tg_id=str(m.from_user.id)).first()
        if not u:
            u = User(tg_id=str(m.from_user.id), name=m.from_user.full_name, phone=m.contact.phone_number)
            s.add(u); s.commit()
    await m.answer("✅ Kontakt qabul qilindi. Endi xizmatni tanlang / Выберите услугу / Choose service:\n1) Haircut (30m)\n2) Beard Trim (20m)\n3) Combo (45m)")

@dp.message()
async def any_message(m: Message):
    # minimal flow: ask for contact if not saved
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("📱 Share phone / Поделиться номером / Raqamni ulashish", request_contact=True))
    await m.answer("Please share your phone to book. / Пожалуйста, поделитесь номером. / Iltimos, raqamingizni ulashing.", reply_markup=kb)

async def main():
    # init DB & seed a default salon + services on first run
    init_db()
    with SessionLocal() as s:
        if not s.query(Salon).first():
            s.add(Salon(name="Demo Salon", tz=DEFAULT_TZ))
        if not s.query(Service).first():
            s.add_all([
                Service(salon_id=1, name="Haircut", duration_min=30, buffer_min=0, price=0),
                Service(salon_id=1, name="Beard Trim", duration_min=20, buffer_min=0, price=0),
                Service(salon_id=1, name="Combo", duration_min=45, buffer_min=0, price=0),
            ])
        s.commit()

    start_api_thread()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
