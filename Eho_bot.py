import telebot

bot = telebot.TeleBot('7717349107:AAFnOOYTwQ7IY04PI5UcHv6wubpYIUI0cHY')
@bot.message_handler(content_types=['text'])
def eho(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()