import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randn(4, 4), columns=['A', 'B', 'C', 'D'])
print(df)
print('\n')
print(df.head())
print('\n')
print(df.nunique())
print('\n')
print(df['A'].unique())
print('\n')
print(df['A'].value_counts())
print('\n')

print(df['A'].apply(lambda x: x**25))

df1 = pd.DataFrame(data=np.ones([4, 4]), columns=['A', 'B', 'C', 'D'])
print(df1.apply(lambda x: x*4))

print('\n')
print(df.values)

