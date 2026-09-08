import pandas as pd
import matplotlib.pyplot as plt

print("Loading data...")

data = pd.read_csv("train.csv")

print("Processing data...")

holiday_sales = data.groupby("IsHoliday")["Weekly_Sales"].mean()

holiday_sales.plot(kind="bar")

plt.title("Holiday vs Non-Holiday Sales")
plt.xlabel("Is Holiday (True/False)")
plt.ylabel("Average Weekly Sales")

plt.show()


