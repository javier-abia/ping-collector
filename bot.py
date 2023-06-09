import os
import subprocess
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

# We load the bot token from the .env file
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Global variable to store the process running the command
running_process = None

# Function to handle the /execute command
async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running_process
    if running_process is None:
        command = "./ping_collector.sh"  # Replace with your command to execute
        running_process = subprocess.Popen(['bash', '-c', command])
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Collecting ping data")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Ping data is already being collected")



# Function to handle the /terminate command
async def terminate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running_process
    if running_process is not None:
        running_process.terminate()
        running_process = None
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Collecting terminated")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ping data wasn't being collected")


async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running_process
    if running_process is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ping data is being collected")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ping collector is off")


def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the command handlers
    application.add_handler(CommandHandler("execute", execute_command))
    application.add_handler(CommandHandler("terminate", terminate_command))
    application.add_handler(CommandHandler("check", check))


    # Start the bot   
    application.run_polling()

if __name__ == '__main__':
    main()
d