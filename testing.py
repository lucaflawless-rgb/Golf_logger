import pandas as pd

df = pd.read_csv("Data_centric_programming.csv")
print(df.head())
print(len(df))
df.info()