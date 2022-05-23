import logging

from aiogram import Bot, Dispatcher, executor, types

from googletrans import Translator
translator = Translator()

API_TOKEN = '5196386075:AAEvLkyR1L3qRMlM4jEfgXXY38itn6B4vOE'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushuring"),
            types.BotCommand("help", "Yordam"),
        ]
    )

async def on_startup(dispatcher):
    await set_default_commands(dispatcher)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply("Tarjimon Botga Xush Kelibsiz!")

@dp.message_handler(commands=['help'])
async def send_helper(message: types.Message):

    await message.reply("Foydalanish uchun tarjima qilmoqchi bo`lgan so`zni yoki gapni kiriting. \nSiz uz-en yoki en-uz da foydalanishingiz mumkin.")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    dest = 'uz' if lang == 'en' else 'en'
    await message.reply(translator.translate(message.text, dest).text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)