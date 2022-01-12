file = '../DATASETS/spotify/data.csv'

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv(file)

# columnas_tempo = df["tempo"]
# columnas_duration = df["duration_ms"]

df = df[["tempo","duration_ms"]]

#Histogramas
print(df.max())
print(df.min())

df.hist( grid=False, color = "c")
plt.show()


#Boxplots
df.boxplot(column="tempo", color = "red", showmeans=True )
plt.show()
df.boxplot(column="duration_ms", color = "red", showmeans=True )
plt.show()


#HeatMap
print(df.corr())
sns.heatmap(df.corr())
plt.show()

# Observar una sola variable
# plt.figure(figsize=(15, 5))
# column = df.corr()[['tempo']].sort_values(by='tempo', ascending=False)
# sns.heatmap(column, vmin=-1, vmax=1, annot=True, cmap='GnBu')
# 
# plt.show()