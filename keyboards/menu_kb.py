from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Клавиатура в основном меню игры
button_newgame = KeyboardButton('/new_request',)
button_score = KeyboardButton('/my_requests')

keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(button_newgame, button_score)