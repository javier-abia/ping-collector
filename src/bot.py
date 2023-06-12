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

# Function to handle the /start command -> Starts running the ping_collector
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running_process
    if running_process is None:
        command = "./ping_collector.sh"
        wipe_data = subprocess.Popen(['bash', '-c', "min,avg,max,time,date> ping.csv"])
        running_process = subprocess.Popen(['bash', '-c', command])
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Collecting ping data")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Ping data is already being collected")



# Function to handle the /stop command -> Stops ping_collector
async def stop_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running_process
    if running_process is not None:
        running_process.terminate()
        running_process = None
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Stopped collecting")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ping data wasn't being collected")

# Function to handle the /check command -> It checks if the program is running
async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running_process
    if running_process is not None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ping data is being collected")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Ping collector is off")


def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("stop", stop_command))
    application.add_handler(CommandHandler("check", check_command))


    # Start the bot   
    application.run_polling()

if __name__ == '__main__':
    main()