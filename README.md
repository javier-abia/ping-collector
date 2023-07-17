# Ping-collector: Network Ping Data Gathering and Plotting

This Python program collects ping data from the network at regular intervals, calculates the average and maximum values every minute, and provides an option to plot the data using a telegram bot.
The program, once executed, is entirely controlled by commands send to your telegram bot.

The bot is currently limited to displaying just the hours. Therefore, collecting ping data for a long period of time can make the plot unreadable.


## Installation

1. Clone the repository or download the source code files to your local machine.

```
git clone https://github.com/javier-abia/ping-collector.git
```

2. Install the required Python libraries using pip.

```
pip install -r requirements.txt
```

## Configuration

1. Create a new bot on Telegram by contacting the @BotFather bot and following the instructions to obtain a bot token.

2. Replace the placeholder `BOT_TOKEN` variable in bot.py with your actual bot token.

   
## Usage

1. Open a terminal or command prompt and navigate to the project directory (src/).

2. Run the program using the following command:

```
python bot.py
```

3. The program will start the telegram bot. After this, you will have 4 different commands to execute in your telegram bot, sending as a message the following command:
   - `/start` to start collecting data
   - `/stop` to stop collecting data
   - `/check` to check if data is being collected
   - `/plot` to plot the collected (or ongoing collecting) data

## Customization

- If you want to adjust the ping interval or the time window for calculating averages and maximums, you can modify the respective variables in the `graph.py` file.

- You can also customize the plot appearance, labels, and other settings in the `graph.py` file using the seaborn library.

## Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch, make your changes, and submit a pull request
