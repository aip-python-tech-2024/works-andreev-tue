import telebot
from dotenv import load_dotenv
import requests
from os import getenv

load_dotenv()

TOKEN = getenv('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='MarkdownV2')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    reply = r'''Hi\! This bot will help you to manage your Nintendo Switch games library\. You can:

• Add your games with purchase price\.
• Get some useful information from eShop\.
• Find buddies with same games\.

Detailed instructions are available via /help command\. Enjoy\!'''

    bot.reply_to(message, reply)


@bot.message_handler(commands=['help'])
def send_help(message):
    reply = r'''Available commands:

• /add new game to your library\. We will ask you some questions about your new game\.
• /find game information from eShop by its name or code \(you can find this code on cartridge\)\.
• /list your games with information\.'''

    bot.reply_to(message, reply)


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
