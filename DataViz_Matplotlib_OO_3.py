import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1, 25, 50)
y = x**2
y1 = x**3
fig = plt.figure(figsize=(8, 8))
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, label='First')
axes.plot(x, y1, label='Second')
axes.set_xlabel('X')
axes.set_ylabel('Y')

axes.legend(loc=0)
plt.tight_layout()
plt.show()

