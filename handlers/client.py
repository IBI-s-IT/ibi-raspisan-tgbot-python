from aiogram import types, Dispatcher
from create_bot import dp, bot

from keyboards import keyboard_menu

async def command_start(message : types.Message):
    id = message.from_user.id
    await sqlite_db.sql_score_add(id)
    await bot.send_message(id, 'Привет! Готов начать игру?', reply_markup=keyboard_menu)

async def command_new_request(message : types.Message):
    await message.answer('Здесь я буду создавать новое обращение', reply_markup=keyboard_menu)

async def command_my_requests(message : types.Message):
    await message.answer('Здесь я буду просматривать все мои обращения', reply_markup=keyboard_menu)

#Ответ на любые сообщения, которые не обрабатываются ботом
async def werid_message(message : types.Message):
    await message.answer('Я не понимаю. Воспользуйся встроенными кнопочками.', reply_markup=keyboard_menu)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(command_new_request, commands='new_request')
    dp.register_message_handler(command_my_requests, commands='my_requests')
    dp.register_message_handler(werid_message)