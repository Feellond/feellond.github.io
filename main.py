#token = 5279727352:AAFFkfirCrXNObf_Hvtoq0rzmes3w_wJH8A
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

API_TOKEN = '5279727352:AAFFkfirCrXNObf_Hvtoq0rzmes3w_wJH8A'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

print('Я работаю :)')
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("test",
reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="test",
web_app=WebAppInfo(url="https://bit.ly/3MkVmIj"))))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)