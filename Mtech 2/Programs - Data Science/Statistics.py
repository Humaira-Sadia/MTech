import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.randint(1, 101, 100)

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", pd.Series(data).mode()[0])
print("IQR:", np.percentile(data,75)-np.percentile(data,25))

plt.hist(data)
plt.show()