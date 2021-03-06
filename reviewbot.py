import constants as keys
from telegram.ext import *
import responses as r

print("bot started")

def start_command(update, context):
    update.message.reply_text("How's it going Ol' Sport? \n\n Staying frosty, are we? \n\n You want to look up a movie, maybe...? \n\n TRY ME")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    #dp.add_handler(CommandHandler("start", help))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
