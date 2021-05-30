import numpy as np
import pandas as pd

data1 = {'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2'], 'C': ['C0', 'C1', 'C2']}
df1 = pd.DataFrame(data=data1, index=[0, 1, 2])
print(df1)
data2 = {'A': ['A3', 'A4', 'A5'], 'B': ['B3', 'B4', 'B5'], 'C': ['C4', 'C5', 'C6']}
df2 = pd.DataFrame(data=data2, index=[4, 5, 6])
print('\n Concatenate')
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))
print('\n Merging !!!')

data3 = {'A': ['A0', 'A1', 'A2'], 'B': ['B0', 'B1', 'B2'], 'key': ['K0', 'K1', 'K2']}
df3 = pd.DataFrame(data=data3, index=[0, 1, 2])
print(df3)
data4 = {'A1': ['A3', 'A4', 'A5'], 'B1': ['B3', 'B4', 'B5'], 'key': ['K0', 'K1', 'K2']}
df4 = pd.DataFrame(data=data4, index=[0, 1, 2])
print(df4)

print(pd.merge(df3, df4, how="inner", on=['key']))

print('\n Join..')

data5 = {'A1': [1, 2, 3], 'B1': [4, 5, 6]}
data6 = {'A2': [11, 12, 13], 'B2': [14, 15, 16]}

print('\n')
df5 = pd.DataFrame(data5, index=['k0', 'k1', 'k2'])
print(df5)
print('\n')
df6 = pd.DataFrame(data6, index=['k1', 'k2', 'k3'])
print(df6)
print('\n')
print(df5.join(df6))
print('\n')
print(df6.join(df5))
print('\n')
print(df5.join(df6, how="outer"))


