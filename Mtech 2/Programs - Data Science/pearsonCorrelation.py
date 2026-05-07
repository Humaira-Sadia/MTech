import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

print(df.corr(numeric_only=True))

for s in df['species'].unique():
    sns.pairplot(df[df['species']==s])
    plt.show()
