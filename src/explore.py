import pandas as pd

df = pd.read_csv("data/raw/mother_jones.csv")

print(df.shape)
print(df.columns.tolist())
print(df.head())
