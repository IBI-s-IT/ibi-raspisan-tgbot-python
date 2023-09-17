from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

env = dotenv_values('.env')

TOKEN = env['TOKEN']

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, skip_updates=True)
