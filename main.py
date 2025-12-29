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
    # Asosiy menyu tugmalari
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
    await message.answer("Sug'urta rasmiylashtirish uchun quyidagi menyuga bosing 👇", reply_markup=kb)

@dp.message(F.text == "🏢 Kompaniya haqida")
async def about_company(message: types.Message):
    oferta_text = (
        "<b>OMMAVIY OFERTA</b>\n\n"
        "Ushbu ommaviy oferta (bundan buyon matnda – oferta) <b>«SQB INSURANCE» SUG‘URTA KOMPANIYASI» AKSIYADORLIK JAMIYATI</b> "
        "(bundan buyon matnda – sug‘urtalovchi) va sug‘urtalanuvchi o‘rtasida transport vositalari egalarining fuqarolik javobgarligini "
        "majburiy sug‘urta qilish (bundan buyon matnda – TVEAFJMSQ) bo‘yicha E-polisni (elektron polisni) onlayn rasmiylashtirish "
        "(shartnomani tuzish va bekor qilish) tartibini hamda sug‘urta shartlarini belgilaydi.\n\n"
        "Mazkur oferta O‘zbekiston Respublikasining Fuqarolik kodeksi, O‘zbekiston Respublikasining «Elektron tijorat to‘g‘risida»gi, "
        "«Elektron hujjat aylanishi to‘g‘risida»gi, «Sug‘urta faoliyati to‘g‘risida»gi Qonunlari, Vazirlar Mahkamasining 2020-yil 14-dekabrdagi "
        "780-sonli qarori bilan tasdiqlangan E-polisni sotish, rasmiylashtirish va ularning haqiqiyligini tekshirish qoidalari hamda "
        "Vazirlar Mahkamasining 2008-yil 24-iyundagi 141-sonli qarori bilan tasdiqlangan Transport vositalari egalarining fuqarolik "
        "javobgarligini majburiy sug‘urta qilish qoidalari asosida ishlab chiqilgan."
    )
    await message.answer(oferta_text, parse_mode="HTML")

@dp.message(F.web_app_data)
async def handle_webapp_data(message: types.Message):
    result = json.loads(message.web_app_data.data)
    
    # Ma'lumotlarni chiroyli formatda yig'amiz
    text = f"📩 <b>Yangi sug'urta arizasi!</b>\n\n"
    text += f"📋 <b>Turi:</b> {result.get('type')}\n"
    text += f"👤 <b>Mijoz:</b> {result.get('name')}\n"
    text += f"📞 <b>Tel:</b> {result.get('phone')}\n"
    
    # Agar OSAGO yoki boshqa avto sug'urta bo'lsa, qo'shimcha ma'lumotlarni qo'shish
    if result.get('car_number'):
        text += f"🔢 <b>Davlat raqami:</b> {result.get('car_number')}\n"
        text += f"📄 <b>Tex-pasport:</b> {result.get('tex_passport')}\n"
        text += f"🚗 <b>Avto turi:</b> {result.get('car_type')}\n"
    
    await message.answer(text, parse_mode="HTML")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())