#

#
# print(data['response']['docs'][0]['title'])
# print(data['response']['docs'][1]['title'])

import telebot
from dotenv import load_dotenv
import requests
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['games'])
def send_games(message):
    url = 'https://search.nintendo-europe.com/en/select?fq=type%3AGAME+AND+system_type%3Anintendoswitch*+AND+product_code_txt%3A*&q=*&sort=change_date+desc&start=0&wt=json&rows=10'
    data = requests.get(url).json()
    response = '\n'.join([game['title'] for game in data['response']['docs']])
    bot.send_message(message.chat.id, response)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
