import telebot
from dotenv import load_dotenv
import requests
from os import getenv
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from telebot.formatting import escape_markdown
import database

load_dotenv()

TOKEN = getenv('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='MarkdownV2')

add_data = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    reply = r'''Hi\! This bot will help you to manage your Nintendo Switch games library\. You can:

• Add your games with purchase price\.
• Get some useful information from eShop\.
• Find buddies with same games\.

Detailed instructions are available via /help command\. Enjoy\!'''

    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['help'])
def send_help(message):
    reply = r'''Available commands:

• /add new game to your library\. We will ask you some questions about your new game\.
• /find game information from eShop by its name or code \(you can find this code on cartridge\)\.
• /list your games with information\.'''

    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['add'])
def add_game_init(message):
    bot.send_message(message.chat.id, 'Send me *game name*')
    bot.register_next_step_handler(message, add_game_name)


def add_game_name(message):
    global add_data
    add_data[message.chat.id] = {'name': message.text}
    bot.send_message(message.chat.id, 'Perfect, now send me purchase price in dollars, for example *59\.99*')
    bot.register_next_step_handler(message, add_game_price)


def add_game_price(message):
    global add_data
    add_data[message.chat.id]['price'] = float(message.text)
    bot.send_message(message.chat.id, 'Nice, now check your info')
    info_reply = f'{add_data[message.chat.id]["name"]}: {add_data[message.chat.id]["price"]}'

    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton('Yes', callback_data='gd_yes'),
        InlineKeyboardButton('No', callback_data='gd_no')
    )

    bot.send_message(message.chat.id, escape_markdown(info_reply), reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data.startswith('gd_'))
def check_new_game_info(call):
    if call.data == 'gd_yes':
        database.add_game(call.message.chat.id, add_data[call.message.chat.id])
        add_data[call.message.chat.id] = {}

        bot.answer_callback_query(call.id, 'Successfully added!')
        bot.send_message(call.message.chat.id, 'Successfully added\!')
    elif call.data == 'gd_no':
        add_data[call.message.chat.id] = {}

        bot.answer_callback_query(call.id, 'Fill the form again')
        add_game_init(call.message)


@bot.message_handler(commands=['games'])
def send_games(message):
    url = 'https://search.nintendo-europe.com/en/select?fq=type%3AGAME+AND+system_type%3Anintendoswitch*+AND+product_code_txt%3A*&q=*&sort=change_date+desc&start=0&wt=json&rows=10'
    data = requests.get(url).json()
    print(data['response']['docs'][0])
    response = '\n'.join([game['title'] for game in data['response']['docs']])
    bot.send_message(message.chat.id, escape_markdown(response))


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, 'Cannot proceed this message, try again')


bot.infinity_polling()
