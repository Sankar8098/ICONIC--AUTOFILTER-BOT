import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your filter function
def filter_message(update: Update, context: CallbackContext) -> None:
    message = update.message
    # Implement your filtering logic here
    if 'bad_word' in message.text:
        # Delete the message if it contains a bad word
        message.delete()

# Define the command handler for /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the AutoFilterBot! This bot will automatically filter messages containing certain keywords.')

# Define the private message handler
def private_message(update: Update, context: CallbackContext) -> None:
    message = update.message
    # Handle private messages here
    message.reply_text("I'm sorry, I can only process messages in group chats.")

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("6668839691:AAE-uUmSpfSz1LQYbENoGUr4nQo7vRncJCA")
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, filter_message))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.private, private_message))

    # Start the Bot
    updater.start_polling()
    logger.info("Bot started")
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
