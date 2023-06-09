import os
import time
import subprocess
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from graph import plot

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
        wipe_data = subprocess.Popen(['bash', '-c', "echo 'min,avg,max,time,date' > ping.csv"])
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

# Function to handle the /plot command -> Sends plotted data
async def plot_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running_process

    # Remove old photo
    subprocess.Popen(['bash', '-c', "rm ./plot.png"])
    time.sleep(1)
    if running_process is not None:

        try:
            # Execute pyhton script to plot and send photo
            plot()

            # This loop gives time to make the plot
            while True:
                try:
                    await context.bot.send_photo(chat_id=update.effective_chat.id, photo="./plot.png", caption="Ping is being collected, here is the progress")
                    break
                except:
                    False
        except:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="There is no data to plot")

    else:

        try:
            # Execute pyhton script to plot and send photo
            plot()

            # This loop gives time to make the plot
            while True:
                try:
                    await context.bot.send_photo(chat_id=update.effective_chat.id, photo="./plot.png", caption="Last data collection")
                    break
                except:
                    False
        except:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="There is no data to plot")

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register the command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("stop", stop_command))
    application.add_handler(CommandHandler("check", check_command))
    application.add_handler(CommandHandler("plot", plot_command))


    # Start the bot   
    application.run_polling()

if __name__ == '__main__':
    main()