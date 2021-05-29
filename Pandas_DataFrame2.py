import numpy as np
import pandas as pd

df = pd.DataFrame(data=np.random.randn(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
print(df)
print(df > 0)
print('\n')
print(df[df > 0])
print('\n')
print(df[(df > 0) & (df < 2)])
print((df['A'] > 0))
print('\n')
print(df[df['A'] > 0]['E'])

df1 = pd.DataFrame(data=np.random.randn(3, 3), index=['a', 'b', 'c'], columns=['A', 'B', 'C'])
print(df1)
print(df1.loc['a'])
print(df1.reset_index())
print('\n')
df1['states'] = ['AB', 'BC', 'CD']
print(df1.set_index('states'))
df2=df1.set_index('states', inplace=True)
print(df2)

df3 = pd.DataFrame(data=np.random.randn(3, 3), columns=['A', 'B', 'C'])
print(df3.loc[[1, 2]])
print(df3.loc[2][['B', 'C']])







