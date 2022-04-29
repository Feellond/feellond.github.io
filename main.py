#token = 5279727352:AAFFkfirCrXNObf_Hvtoq0rzmes3w_wJH8A
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types.web_app_data import WebAppData

API_TOKEN = '5279727352:AAFFkfirCrXNObf_Hvtoq0rzmes3w_wJH8A'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

print('Я работаю :)')
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("test message",
reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="link",
web_app=WebAppInfo(url="https://feellond.github.io/student.html?a=ham&b=bam"))))

#async def recieve_message(web_app_query_id: str, result: types.InlineQueryResult):
    #bot.answer_web_app_query()

#@dp.message_handler(content_types=types.ContentTypes.WEB_APP_DATA)
#async def recieve_message(web_app_query_id: str, result: types.InlineQueryResult):
    #print("worked?")
    #bot.answer_web_app_query(web_app_query_id, result)

@dp.message_handler(content_types=types.ContentTypes.WEB_APP_DATA)
async def recieve_message(message: str):
    print(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)