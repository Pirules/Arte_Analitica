file = '../DATASETS/spotify/data.csv'

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans

df = pd.read_csv(file)

# columnas_tempo = df["tempo"]
# columnas_duration = df["duration_ms"]

df = df[["tempo","duration_ms"]]
df = df[df.duration_ms<450000]
df = df.dropna(axis = 0, how = 'any')

kmeans = KMeans(n_clusters=10).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

cla = kmeans.predict(df)

plt.scatter(df["tempo"],df["duration_ms"],c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0],centroids[i][1],marker="*",c="red")
plt.show()