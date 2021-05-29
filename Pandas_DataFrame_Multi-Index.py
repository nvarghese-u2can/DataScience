import numpy as np
import pandas as pd

out_index = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
in_index = ['1', '2', '3', '1', '2', '3']
df_index = list(zip(out_index,in_index))
print(df_index)
df_data_index = pd.MultiIndex.from_tuples(df_index)
print('\n')
print(df_data_index)

df = pd.DataFrame(data=np.random.randn(6, 2), index=df_data_index, columns=['A', 'B'])
print('\n')
print(df)
print('\n')
print(df.loc['G1'].loc['1']['B'])


