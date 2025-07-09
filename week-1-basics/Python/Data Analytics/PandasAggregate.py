import pandas as pd
df = pd.read_csv('pokemon_data.csv')
#df = df.groupby(['Type 1']).mean(numeric_only=True).sort_values('HP',ascending=False)
#print(df)
# .sum , .mean , .count
df['count']=1
df = df.groupby(['Type 1']).count()['count']
print(df)