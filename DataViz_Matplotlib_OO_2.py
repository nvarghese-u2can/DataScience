import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1, 25, 50)
y = x**2

fig, axes = plt.subplots(1, 2)
print(axes)
print('\n')
# print(axes[0].plot(x, y))
# print(axes[1].plot(y, x))
# axes[0].plot(x, y)
axes[0].set_title('SUB1')
axes[0].set_xlabel('SUB1X')
axes[0].set_ylabel('SUB1Y')
axes[0].plot(x, y)
axes[1].set_title('SUB2')
axes[1].set_xlabel('SUB2X')
axes[1].set_ylabel('SUB2Y')
axes[1].plot(y, x)

plt.tight_layout()

plt.show()

plt.close()

