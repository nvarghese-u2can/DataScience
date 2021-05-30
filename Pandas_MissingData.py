import numpy as np
import pandas as pd

sample = {'a': [1, 2, np.nan], 'b': [1, 2, 3], 'c': [1, np.nan, np.nan]}
df = pd.DataFrame(data=sample)
print(df)
print('\n')
print(df.dropna())
print('\n')
print(df.dropna(axis=1))
print('\n')
print(df.dropna(axis=1, thresh=2))
print('\n')
print(df)
print('\n')
print(df['a'].fillna(value='TEST'))
print('\n')
print(df['c'].fillna(value=df['a'].sum(), inplace=True))
print('\n')
print(df)
