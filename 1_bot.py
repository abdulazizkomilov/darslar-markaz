import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')

API_TOKEN = '5196386075:AAEvLkyR1L3qRMlM4jEfgXXY38itn6B4vOE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):


    await message.reply("Hi!\nWelcome to wikibot!")
    await message.reply("Bu bot siz kiritgan so'zga doir malumotlarni wikipediadan topib beradi.")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga doir maqola topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)