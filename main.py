from mybot import *
from decorator import * 
import sys

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token='YOUR TOKEN HERE')
dispatcher = updater.dispatcher

@log
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me! ")

def stop(bot, updater):
    updater.stop()
    sys.exit()

def unknown(bot, update):
     bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
weather_handler = CommandHandler('method1', method1)
dispatcher.add_handler(weather_handler)
stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)
unknown_handler = MessageHandler([Filters.command], unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
