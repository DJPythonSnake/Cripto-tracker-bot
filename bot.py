from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

import parsebot

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nМоя задача - отслеживать курс криптовалют.\nЧтобы узнать список команд - нажми сюда: '/help'")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Доступные команды:\n'/bitcoin'\n'/ethereum'")


@dp.message_handler(commands=['bitcoin'])
async def print_course(message: types.Message):
    await message.reply("Курс битка:\nUSD: " + parsebot.course_usd + "\nRUB: " + parsebot.course_rub)

@dp.message_handler(commands=['ethereum'])
async def print_course(message: types.Message):
    await message.reply("Курс эфира:\nUSD: " + parsebot.course1_usd + "\nRUB: " + parsebot.course1_rub)



if __name__ == '__main__':
    executor.start_polling(dp)
