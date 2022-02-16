import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = np.linspace(-5, 5, 21)
y1 = 3 * x + 5
y2 = 2 * x + 4
y3 = 9 * x + 2
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
