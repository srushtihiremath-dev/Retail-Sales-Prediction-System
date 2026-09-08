import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("train.csv")

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Create Month column
data["Month"] = data["Date"].dt.month

# Group by Month and calculate total sales
monthly_sales = data.groupby("Month")["Weekly_Sales"].sum()

# Plot graph
plt.figure()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

# Save image
plt.savefig("monthly_sales.png", dpi=300, bbox_inches='tight')

# Show graph
plt.show()