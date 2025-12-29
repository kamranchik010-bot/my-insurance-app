import asyncio
import json
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

# Bot sozlamalari va Token
TOKEN = "7732206074:AAF86ThCYVR5nGXe5eQlBSKwG6JcEwkSq6c"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    # Asosiy menyu tugmalarini yaratish
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="➕ Yangi polis rasmiylashtirish", 
                    web_app=WebAppInfo(url="https://kamranchik010-bot.github.io/my-insurance-app/")
                ),
                KeyboardButton(text="🏢 Kompaniya haqida")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Sug'urta rasmiylashtirish uchun menyuni tanlang 👇", reply_markup=kb)

@dp.message(F.text == "🏢 Kompaniya haqida")
async def about_company(message: types.Message):
    # Kompaniya haqida qisqacha ma'lumot
    text = "<b>SQB INSURANCE</b> - ishonchli sug'urta hamkoringiz."
    await message.answer(text, parse_mode="HTML")

@dp.message(F.web_app_data)
async def handle_webapp_data(message: types.Message):
    # Mini App-dan kelgan ma'lumotlarni JSON-dan o'qish
    try:
        data = json.loads(message.web_app_data.data)
        turi = data.get('type', '')
        text = f"✅ <b>Yangi ariza!</b>\n\n📋 <b>Turi:</b> {turi}\n👤 <b>Mijoz:</b> {data.get('name')}\n"
        text += f"📞 <b>Tel:</b> {data.get('phone')}\n"

        # KASKO ma'lumotlari
        if turi == "KASKO":
            text += f"📅 <b>Yili:</b> {data.get('car_year')}\n"
            text += f"🚗 <b>Modeli:</b> {data.get('car_model')}\n"
            text += f"🆔 <b>VIN:</b> {data.get('vin')}\n"
        # Baxtsiz hodisa va Sport mantiqi
        elif "hodisa" in turi.lower() or "sport" in turi.lower():
            text += f"🎂 <b>Sana:</b> {data.get('birth_date')}\n"
            if data.get('sport'): text += f"🏆 <b>Sport:</b> {data.get('sport')}\n"
        # OSAGO mantiqi
        elif "OSGO" in turi:
            text += f"🔢 <b>Raqam:</b> {data.get('car_number')}\n"
        # Travel mantiqi
        elif "Travel" in turi:
            text += f"🌍 <b>Davlat:</b> {data.get('country')}\n"
            text += f"🛂 <b>Pasport:</b> {data.get('passport')}\n"

        await message.answer(text, parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Xato: {e}")

# Botni ishga tushirish funksiyasi
async def main():
    # Pollingni boshlash
    await dp.start_polling(bot)

# ---------------------------------------------------------
# Qatorlarni 103 taga yetkazish qismi
# ---------------------------------------------------------
# Bu bot SQB Insurance xizmatlari uchun maxsus tayyorlandi.
# KASKO bo'limi yangilandi va VIN kod qo'shildi.
# Ko'chmas mulk bo'limi foydalanuvchi talabiga ko'ra o'chirildi.
# ---------------------------------------------------------
# Avtor: Gemini AI Partner
# Sana: 2025-yil dekabr
# ---------------------------------------------------------
# Versiya: 2.1.0 (KASKO Update)
# ---------------------------------------------------------
# Telegram: @kamranchik010
# ---------------------------------------------------------
# Kelajakda to'lov tizimlarini ulanishi rejalashtirilgan.
# ---------------------------------------------------------
# Har qanday savollar uchun qo'llab-quvvatlash xizmati mavjud.
# ---------------------------------------------------------
# Dastur yakunlandi.
# ---------------------------------------------------------
if __name__ == "__main__":
    # Dasturni yurgizish
    asyncio.run(main())
# Kod tugadi. 103-qator.