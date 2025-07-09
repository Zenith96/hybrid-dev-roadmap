import pandas as pd
df = pd.read_csv('pokemon_data.csv')
df['Total'] = df.iloc[:,4:10].sum(axis=1)
print(df.head(2))
cols  = list(df.columns)
df  = df[cols[0:4]+[cols[-1]]+cols[5:12]]
print(df.head(2))
df.to_csv('modified.csv',index=False)
df.to_csv('modified.txt',index=False,sep='\t')