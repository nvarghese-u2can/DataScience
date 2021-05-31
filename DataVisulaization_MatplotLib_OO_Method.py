import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1, 25, 50)
y = x**2

fig = plt.figure()

# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y)
# axes.set_xlabel('X')
# axes.set_ylabel('Y')
# axes.set_title('OO Figure1')
# plt.show()

axes1 = fig.add_axes([0.2, 0.2, 0.7, 0.7])
axes2 = fig.add_axes([0.3, 0.3, 0.4, 0.4])

axes1.plot(x, y, 'r')
axes2.plot(y, x, 'b')

plt.show()
plt.close()
