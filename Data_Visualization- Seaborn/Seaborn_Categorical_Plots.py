import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_Set = sns.load_dataset('tips')

print(data_Set.head())
print(data_Set.columns)
# fig = plt.figure(figsize=(10, 8))
# axes = fig.add_axes([0.1, 0.1, 0.9, 0.9])

# bar plot
sns.barplot(x='sex', y='total_bill', data=data_Set, estimator=np.std)
plt.show()
plt.close()

# count plot
sns.countplot(x='sex', data=data_Set)
plt.show()
plt.close()

# box plot
sns.boxplot(x='day', y='total_bill', data=data_Set, hue='smoker')
plt.show()
plt.close()

# violin plot
sns.violinplot(x='day', y='total_bill', data=data_Set, hue='sex', split=True)
plt.show()

# strip plot
sns.stripplot(x='day', y='total_bill', data=data_Set, hue='sex', split=True)
plt.show()

# swarm plot
sns.violinplot(x='day', y='total_bill', data=data_Set, hue='sex', split=True)
sns.swarmplot(x='day', y='total_bill', data=data_Set, hue='sex')
plt.show()

# factor plot

sns.factorplot(x='day', y='total_bill', data=data_Set, kind='box')
plt.show()


