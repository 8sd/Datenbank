import random
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

with open('token', "r") as t:
	token = t.read().strip()

with open('../list', "r") as l:
	datenbank = l.readlines()

def wkwt(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(random.choice(datenbank))

def start(update: Update, context: CallbackContext) -> None:
    custom_keyboard = [['/wkwt']] 
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    context.bot.send_message(chat_id=update.effective_user.id, 
                 text="Was können wir tun?", 
                 reply_markup=reply_markup)

updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('wkwt', wkwt))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
