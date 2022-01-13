file = '../DATASETS/spotify/data.csv'

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv(file)

# columnas_tempo = df["tempo"]
# columnas_duration = df["duration_ms"]

df = df[["tempo","duration_ms"]]

