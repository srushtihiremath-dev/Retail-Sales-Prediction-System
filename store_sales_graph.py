import pandas as pd
import matplotlib.pyplot as plt
plt.figure()
data = pd.read_csv("train.csv")

store_sales = data.groupby("Store")["Weekly_Sales"].sum()

top_stores = store_sales.sort_values(ascending=False).head(10)

top_stores.plot(kind="bar")

plt.title("Top 10 Stores by Total Sales")
plt.xlabel("Store")
plt.ylabel("Total Weekly Sales")
plt.show();

