from telebot import types

def choice_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but_usd = types.KeyboardButton('USD')
    but_eur = types.KeyboardButton('EUR')
    kb.add(but_usd, but_eur)

    return kb