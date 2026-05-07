import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Load Data
df = pd.read_csv('/content/sample_data/california_housing_train.csv')
X = df[['housing_median_age', 'total_rooms', 'population']]
y = df['median_house_value']
# Model
model = LinearRegression().fit(X, y)
y_pred = model.predict(X)
# Results
print(f"R^2 Score: {model.score(X, y):.4f}")

# Visualize
plt.figure(figsize=(8, 5))
plt.scatter(y, y_pred, alpha=0.3, s=10, color='teal', label='Predictions')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2, label='Perfect Fit')
plt.title('Multiple Regression: Actual vs Predicted')
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
