import numpy as np
import pandas as pd

data1 = {'Org': ['AA', 'AA', 'BB', 'BB', 'CC', 'CC'],
         'Share': ['AA1', 'AA2', 'BB1', 'BB2', 'CC1', 'CC2'],
         'Price': [100, 150, 250, 298, 300, 450]}

df = pd.DataFrame(data1)
print(df)
print('\n')
result = df.groupby(by='Org')
print(result.std())
print('\n')
print(df.groupby(by='Org').describe())
print('\n')
print(df.groupby(by='Org').describe().transpose())



