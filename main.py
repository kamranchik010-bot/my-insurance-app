import asyncio
import json
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7732206074:AAF86ThCYVR5nGXe5eQlBSKwG6JcEwkSq6c"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
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
    text = "<b>SQB INSURANCE</b> - ishonchli sug'urta hamkoringiz."
    await message.answer(text, parse_mode="HTML")

@dp.message(F.web_app_data)
async def handle_webapp_data(message: types.Message):
    try:
        data = json.loads(message.web_app_data.data)
        turi = data.get('type', '')
        text = f"✅ <b>Yangi ariza!</b>\n\n📋 <b>Turi:</b> {turi}\n👤 <b>Mijoz:</b> {data.get('name')}\n"
        text += f"📞 <b>Tel:</b> {data.get('phone')}\n"
        if turi == "KASKO":
            text += f"📅 <b>Yili:</b> {data.get('car_year')}\n"
            text += f"🚗 <b>Modeli:</b> {data.get('car_model')}\n"
            text += f"🆔 <b>VIN:</b> {data.get('vin')}\n"
        elif "hodisa" in turi.lower() or "sport" in turi.lower():
            text += f"🎂 <b>Sana:</b> {data.get('birth_date')}\n"
            if data.get('sport'): text += f"🏆 <b>Sport:</b> {data.get('sport')}\n"
        elif "OSGO" in turi:
            text += f"🔢 <b>Raqam:</b> {data.get('car_number')}\n"
        elif "Travel" in turi:
            text += f"🌍 <b>Davlat:</b> {data.get('country')}\n"
            text += f"🛂 <b>Pasport:</b> {data.get('passport')}\n"

        await message.answer(text, parse_mode="HTML")
    except Exception as e:
        await message.answer(f"Xato: {e}")

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())