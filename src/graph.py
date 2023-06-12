import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn theme
sns.set_theme(style="whitegrid")

# Loading the csv file as a pandas DataFrame
df =  pd.read_csv("ping.csv")

# Calculate the desired number of ticks based on the data length
desired_tick_interval = 4
num_ticks = int(len(df["time"]) / desired_tick_interval)

# Create the seaborn plot
g = sns.relplot(
    data = df, 
    x=range(len(df["time"])), y="avg", hue = "max"
)



### Config plot ###

# Set the tick locations
plt.xticks(range(0, len(df["time"]), num_ticks))


# Set the tick labels to correspond to specific values in your data
tick_labels = [df["time"][i] for i in range(0, len(df["time"]), num_ticks)]
g.set_xticklabels(tick_labels)


# Set axis and legend labels
g.set_axis_labels("Local time", "average (ms)", labelpad=10)
g.legend.set_title("Max ping (ms)")
g.figure.set_size_inches(10.5, 4.5)
g.ax.margins(.1)

plt.savefig("plot.png")
