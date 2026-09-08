import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "store": [1, 2, 3, 4, 5],
    "feature": [50, 60, 70, 80, 90],
    "sales": [200, 230, 260, 290, 320]
}

df = pd.DataFrame(data)

X = df[["store", "feature"]]
y = df["sales"]

model = LinearRegression()
model.fit(X, y)

def predict_sales(store, feature):
    return model.predict([[store, feature]])[0]