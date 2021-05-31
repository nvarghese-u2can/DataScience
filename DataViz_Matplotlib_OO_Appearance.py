import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1, 25, 100)
y = x**2

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, color='red', lw=3, ls='--', marker='+', label='TEST')

axes.set_xlim([1, 25])
axes.set_ylim([1, 250])

axes.legend(loc=0)
#plt.tight_layout()
plt.show()

plt.scatter(x, y)
plt.show()

plt.hist(x)
plt.show()


