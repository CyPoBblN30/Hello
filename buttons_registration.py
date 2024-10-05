from telebot import types

def number_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отправить номер телефона', request_contact=True)
    kb.add(but1)

    return kb

def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Отравьте локацию', request_location=True)
    kb.add(but1)

    return kb

def language_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.InlineKeyboardButton('ru', callback_data='ru')
    but2 = types.InlineKeyboardButton('uz', callback_data='uz')
    kb.add(but1, but2)

    return kb


