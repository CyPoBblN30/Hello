from gc import callbacks

import telebot
import database_registration as db
import buttons_registration as bt

bot = telebot.TeleBot('7859920137:AAGXfWDvZJrVakrdvCQwmjxPLc6a3EVvj4M')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if db.check_user(user_id):
        bot.send_message(user_id, f'Здраствуйте!', reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Здраствуйте! Давайте начнём регистрацию!\nВвидете ваше имя!', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, get_language)

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Команда /start запускает бот\nБот регистрируей пользователей',  reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, start)

def get_language(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Выбирете язык', reply_markup=bt.language_buttons())
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! Теперь отправьте свой номер через кнопку!', reply_markup=bt.number_button())
    bot.register_next_step_handler(message, get_number, user_name)

def get_number(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        db.register(user_id, user_name, user_number)
        bot.send_message(user_id, 'Вы успешно отправили номер телефона!\nТеперь отправьте свою локацию через кнопку ниже', reply_markup=bt.location_button())
        bot.register_next_step_handler(message, get_c)
    else:
        bot.send_message(user_id, 'Отправьте номер через кнопку ниже!')
        bot.register_next_step_handler(message, get_number, user_name)

def get_c(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Вы успешно зарегистрировались!', reply_markup=telebot.types.ReplyKeyboardRemove())

bot.polling()




