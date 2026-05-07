import seaborn as sns
import pandas as pd

df_iris = sns.load_dataset('iris')

spearman_corr = df_iris.corr(method='spearman', numeric_only=True)

print("Spearman Correlation Matrix:")
print(spearman_corr)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
sns.heatmap(spearman_corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Spearman Correlation Heatmap (Iris Dataset)')
plt.show()