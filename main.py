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

@bot.message_handler(commands= ['convert'])
def values(message: telebot.types.Message):
    text  = 'Выберите валюту из которой конвертировать:'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, base_handler)

def base_handler(message: telebot.types.Message):
    base = message.text.strip()
    text = 'Выберите валюту в которую конвертировать:'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, sym_handler, base)

def sym_handler(message: telebot.types.Message, base):
    sym = message.text.strip()
    text = 'Выберите количество конвертируемой валюты:'
    bot.reply_to(message, text)
    bot.register_next_step_handler(message, amount_handler, base, sym)

def amount_handler(message: telebot.types.Message, base, sym):
    amount = message.text.strip()
    try:
        new_price = Converter.get_price(base, sym, amount)
    except ApiException as e:
        bot.send_message(message, f"Ошибка в комманде: \n {e}")
    text = f"Цена {amount} {base} в {sym} : {new_price}"
    bot.reply_to(message, text)

bot.polling()



