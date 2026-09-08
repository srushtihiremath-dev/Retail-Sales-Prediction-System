import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")

plt.plot(data["Weekly_Sales"])
plt.title("Weekly Sales Trend")
plt.xlabel("Index")
plt.ylabel("Weekly Sales")
plt.show()