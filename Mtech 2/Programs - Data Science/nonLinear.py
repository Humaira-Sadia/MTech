import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10)
y = x**2

coef = np.polyfit(x,y,2)
poly = np.poly1d(coef)

plt.scatter(x,y)
plt.plot(x,poly(x))
plt.show()
