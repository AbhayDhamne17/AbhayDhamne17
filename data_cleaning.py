import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
print(df)

for i in df.index:
    if df.loc[i, 'Duration'] > 60:
        df.loc[i, 'Duration'] = 60
df.dropna(subset=['Date'], inplace=True)
df.Date = pd.to_datetime(df.Date, format='mixed')
x = df.Calories.mean()
df.Calories.fillna(x, inplace=True)
df.Calories = df.Calories.round(2)
print(df)

df['Day'] = pd.DatetimeIndex(blackrock.Date).day_name()
df['Range'] = pd.cut(df['Duration'], bins=[10, 20, 30, 40, 50, 60], labels=['0-12', '13-24', '25-36', '37-48', '49-60'])
print(df)
