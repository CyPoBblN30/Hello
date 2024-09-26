from fnmatch import translate

import telebot
import buttons

bot = telebot.TeleBot('7619773623:AAGst8VOD6UQg2D2q0XmXYQPXtJBxBQQ9Go')

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Здраствуйте', reply_markup=buttons.choice_buttons())
    bot.register_next_step_handler(message, text)

@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'usd':
        bot.send_message(user_id, 'Курс доллара 12700 сум')
    elif message.text.lower() == 'eur':
        bot.send_message(user_id, 'Курс евра 14200 сум')

bot.polling(non_stop=True)