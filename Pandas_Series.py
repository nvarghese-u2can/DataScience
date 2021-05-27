import numpy as np
import pandas as pd

my_data = [1, 2, 3]
my_data1 = {'a': 1, 'b': 2}
my_data2 = np.arange(1, 10)
# my_series = pd.Series(data=my_data1)
# my_series = pd.Series(data=my_data2])
my_series = pd.Series(data=my_data, index=['a', 'b', 'c'])
print(my_series)

my_data4 = {'a': 1, 'b': 2, 'c': 5}
my_series1 = pd.Series(my_data4)
my_data5 = {'a': 1, 'b': 2, 'd': 5}
my_series2 = pd.Series(my_data5)
print(my_series1+my_series2)

