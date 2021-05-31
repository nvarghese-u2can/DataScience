import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(1, 10, 100)
y = x**2

# Functional Method
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('sample diagram')
plt.show()
# subplots

plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')

plt.subplot(1, 2, 2)
plt.plot(x, y, 'b')
plt.show()

plt.close()






