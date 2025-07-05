import csv
import pandas as pd
df = pd.read_csv('pokemon_data.csv')
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# df_txt = pd.read_csv('pokemon_data.txt',delimiter='\t')
print(df.head(3))
print(df.tail(1))
print(df.columns)##reading headers
print(df[['Name','Type 1','Attack']][0:2])
#Read Each row using indexes
print(df.iloc[1:3])
#Read a specific row
print(df.iloc[2,1])
#Read using Label
print(df.loc[4:6]['Name'])
print(df.loc[df['Type 1']=='Fire'][0:5])
print(df.describe())
print(df.sort_values(['Type 1','HP'],ascending=[1,0]))