import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")

data = pd.read_csv("train.csv")

print("Processing data...")

store_sales = data.groupby("Store")["Weekly_Sales"].sum()

top10 = store_sales.sort_values(ascending=False).head(10)

print("Plotting graph...")

top10.plot(kind="bar")

plt.title("Top 10 Stores by Sales")
plt.xlabel("Store")
plt.ylabel("Total Sales")

plt.show()