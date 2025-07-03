import pandas as pd
import re
df = pd.read_csv('pokemon_data.csv')
print(df.loc[df['Type 1'].str.contains('Fire|Grass',flags = re.I,regex=True)])
print(df.loc[df['Name'].str.contains('^pi[a-z]*',flags = re.I,regex=True)])

