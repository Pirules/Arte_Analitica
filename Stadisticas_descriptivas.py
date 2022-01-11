file = './DATASETS/spotify/data.csv'
import pandas as pd

df = pd.read_csv(file)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print("Numero de registros y de variables:")
print(df.shape,"\n")
print("Nombres de las columnas:")
print(df.columns,"\n")
print("Tipo de datos de cada columna:")
print(df.dtypes,"\n")

columnas_tempo = df["tempo"]
columnas_duration = df["duration_ms"]

print("Valores unicos en de tempo:")
print(columnas_tempo.unique(),"\n")

print("Valores unicos en de duracion:")
print(columnas_duration.unique(),"\n")

print("Valores maximos y minimos tempo:")
print(columnas_tempo.max())
print(columnas_tempo.min(),"\n")

print("Valores maximos y minimos duracion:")
print(columnas_duration.max())
print(columnas_duration.min(),"\n")

print("Valores media, mediana y desviacion de tempo:")
print(columnas_tempo.mean())
print(columnas_tempo.median())
print(columnas_tempo.std(),"\n")

print("Valores media, mediana y desviacion de duracion:")
print(columnas_duration.mean())
print(columnas_duration.median())
print(columnas_duration.std())

