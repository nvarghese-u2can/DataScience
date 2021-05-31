import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_set = sns.load_dataset('tips')
print(data_set.head())
print(data_set.columns)


# distribution plots
sns.distplot(data_set['total_bill'], kde=False, bins=30)
plt.show()
plt.close()

# joint plots

sns.jointplot(x='total_bill', y='tip', data=data_set, kind='hex')
sns.jointplot(x='total_bill', y='tip', data=data_set, kind='reg')
sns.jointplot(x='total_bill', y='tip', data=data_set, kind='kde')

plt.show()
plt.close()

# pair plots
sns.pairplot(data=data_set, hue='sex', palette='coolwarm')
plt.show()

# rug plot
sns.rugplot(data_set['total_bill'])
plt.show()
plt.close()

# kde plot
sns.kdeplot(data_set['total_bill'])
plt.show()
plt.close()
