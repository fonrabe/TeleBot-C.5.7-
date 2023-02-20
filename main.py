import telebot

from config import *
from utils import Converter, ApiException


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Приветствие!'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands= ['values'])
def values(message: telebot.types.Message):
    text  = 'Доступные валюты:'
    for i in exchange.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        base_key, sym_key, amount = message.text.split()
    except ValueError as e:
        bot.reply_to(message, 'Неверное количество параметров!')

    try:
        new_price = Converter.get_price(base_key, sym_key, amount)
        bot.reply_to(message, f"Цена {amount} {base_key} в {sym_key} : {new_price}")
    except ApiException as e:
        bot.reply_to(message, f"Ошибка в команде: \n{e}")

bot.polling()



