import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips_data = sns.load_dataset('tips')
flights_data = sns.load_dataset('flights')

print(tips_data.head())
print(tips_data.columns)

print(flights_data.head())
print(flights_data.columns)
print('\n')
print(tips_data.corr())
print('\n')

# heat map
sns.heatmap(tips_data.corr(), annot=True, cmap='coolwarm', linecolor='red', linewidths=3)

plt.show()
plt.close()

fp = flights_data.pivot_table(values='passengers', index='month',columns='year')

sns.heatmap(fp, cmap='magma', linewidths=3, linecolor='black')
plt.show()

# cluster map
sns.clustermap(fp, cmap='magma', standard_scale=1)
plt.show()
plt.close()