import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.tail(1))
print(df.columns)
print(df[['Name','Type 1','Attack']][0:2])
print(df.iloc[1:3])
print(df.loc[df['Type 1']=='Fire'])
print(df.describe())
print(df.sort_values(['Type 1','HP'],ascending=[1,0]))