import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randn(3, 2), index=['A', 'B', 'C'], columns=['a', 'b'])
print(df)
print(df['a'])
print(df.loc['A'])
print(df[['a', 'b']])
print(df.shape)
df['c'] = df['a']**2
print(df)
print(df.drop('c', axis=1, inplace=True))
df.drop('C', axis=0, inplace=True)
print(df)
print('\n')
print(df.loc['A'])
print('\n')
print(df.iloc[0])

df1 = pd.DataFrame(data=np.arange(0,25).reshape(5, 5), index=['A', 'B', 'C', 'D', 'E'], columns=['a', 'b', 'c', 'd', 'e'])
print(df1)
print('\n')
print(df1.loc['B', 'c'])
print('\n')
print(df1.loc[['A', 'B'], ['c', 'd', 'e']])





