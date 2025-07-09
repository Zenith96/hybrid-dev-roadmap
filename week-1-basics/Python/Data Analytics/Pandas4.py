import pandas as pd
df = pd.read_csv('pokemon_data.csv',)
#df[condition , 'column_name'] = new_name
df.loc[df['Type 1'] == 'Fire','Type 1'] = 'Flamer'
print(df)
df.loc[df['HP'] > 80 ,['Generation','Legendary']] = [1,2]
print(df.loc[df['HP'] > 80, ['Generation', 'Legendary']])

