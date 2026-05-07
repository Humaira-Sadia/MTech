from sklearn.linear_model import LinearRegression

X = df[['sepal_length']]
y = df['petal_length']

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_)
print("Intercept:", model.intercept_)
