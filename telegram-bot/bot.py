import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

with open('token', "r") as t:
	token = t.read().strip()

with open('../list', "r") as l:
	datenbank = l.readlines()

def wkwt(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(datenbank))


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('wkwt', wkwt))

updater.start_polling()
updater.idle()
