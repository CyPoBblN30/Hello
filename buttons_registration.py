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

