import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('df1', index_col=0)
print(df1.head())

print('\n')

df2 = pd.read_csv('df2')
print(df2.head())

sns.set_style('darkgrid')
# Histogram
df1['A'].plot.hist(bins=25)
plt.show()

# Bar plot
df2.plot.bar()
plt.show()

# Bar plot with stacked option
df2.plot.bar(stacked=True)
plt.show()

# Area Plot
df2.plot.area(alpha=0.5)
plt.show()

# Box Plot
df2.plot.box()
plt.show()

# KDE Plot
df2['a'].plot.kde()
plt.show()

# Line Plot
# df2['a'].plot.line()
# plt.show()

# df1.plot.line(x=df1.index,y='B')
# plt.show()

df1.plot.scatter(x='A', y='B', c='C', cmap='magma')
plt.show()