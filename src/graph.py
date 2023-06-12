import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn theme
sns.set_theme(style="whitegrid")

# Loading the csv file as a pandas DataFrame
df = pd.read_csv("ping.csv")

# Plot data
g = sns.relplot(
    data=df,
    x="time", y="avg", hue="max"
)

# Config plot
g.set_axis_labels("Local time", "average (ms)", labelpad=10)
g.set_xticklabels(rotation = 45)

plt.show()