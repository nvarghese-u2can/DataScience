import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris_data = sns.load_dataset('iris')
print(iris_data.head())
print('\n')
print(iris_data.columns)

# sns.pairplot(iris_data)
# plt.show()

# Grid plot
print('\n')
iris_grid = sns.PairGrid(iris_data)
iris_grid.map_diag(sns.distplot)
iris_grid.map_lower(sns.kdeplot)
iris_grid.map_upper(plt.scatter)
plt.show()
print('\n')

# Faucet Plot

tips_data = sns.load_dataset('tips')
tips_data.head()

tips_grid = sns.FacetGrid(tips_data, row='smoker', col='time')
tips_grid.map(sns.distplot, 'total_bill', kde=False)

plt.show()



