import pandas as pd
df = pd.read_csv('pokemon_data.csv')
df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def'] + df['Speed']
print(df.head(2))
df =df.drop(columns=['Total'])
print(df.head(2))
df['Total'] = df.iloc[:,4:10].sum(axis=1)
print(df.head(2))
