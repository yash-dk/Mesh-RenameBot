# pip install python-telegram-bot==12.0.0
from telegram.ext import Updater
from telegram.ext import CommandHandler
updater = Updater(BOT_TOKEN)

def start(bot, update):
    # print('json file update : ' ,update)
    # print("json file bot : ', bot)
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    print("chat_id : {} and firstname : {} lastname : {}  username {}". format(chat_id, first_name, last_name , username))
    bot.sendMessage(chat_id, 'text')

start_command = CommandHandler('start',start)
updater.dispatcher.add_handler(start_command)
updater.start_polling()
updater.idle()
