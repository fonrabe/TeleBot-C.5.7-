import telebot

exchange = {
    'доллар' : 'USD',
    'евро' : 'EURO',
    'рубль' : 'RUB',
}

TOKEN = "6244157845:AAHx0agwgu9sc5a77M0cECWJShwHVc2Bifo"

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

bot.polling()



