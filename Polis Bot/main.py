import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "7732206074:AAF86ThCYVR5nGXe5eQlBSKwG6JcEwkSq6c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    # Asosiy menyu tugmalari
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                # WebAppInfo ichiga web-sahifangiz manzilini yozasiz
                KeyboardButton(text="➕ Yangi polis rasmiylashtirish", 
                              # Kodingizdagi ushbu qatorni o'zgartiring:
web_app=WebAppInfo(url="https://kamranchik010-bot.github.io/my-insurance-app/")),
                KeyboardButton(text="🏢 Kompaniya haqida")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Sug'urta rasmiylashtirish uchun quyidagi menyuga bosing 👇", reply_markup=kb)

@dp.message(F.text == "🏢 Kompaniya haqida")
async def about_company(message: types.Message):
    # O'zingiz xohlagan matnni shu yerga yozasiz
    await message.answer("O'zim yozaman")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())