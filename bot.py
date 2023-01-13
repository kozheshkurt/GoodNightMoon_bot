import telebot
import moon
import config
import sys

# telegram bot API
bot = telebot.TeleBot(config.TOKEN)


# says hello to user isung their name and last name if exists
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name == None:
        mess = f'Hello, <b>{message.from_user.first_name}</b>'
    else:
        mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['good_night'])
def good_night(message):
    mess = moon.get_goodnight(0)
    bot.send_message(message.chat.id, mess)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    mess = moon.get_goodnight(0)
    # +' '+mess[-1])
    # bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, message.text + mess[-1])


bot.polling(none_stop=True)
