from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from telegram.ext import Updater, CommandHandler

TOKEN = "Token"

def hello(update, context):
    update.message.reply_text("Hi")

def main():
    updater = Updater(TOKEN, use_context = True)

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()