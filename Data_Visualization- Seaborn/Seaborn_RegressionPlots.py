import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

tips_data = sns.load_dataset('tips')
print(tips_data.head())
print(tips_data.columns)

sns.set_style(style='whitegrid')
sns.lmplot(x='total_bill', y='tip', data=tips_data, hue='sex')
plt.show()
