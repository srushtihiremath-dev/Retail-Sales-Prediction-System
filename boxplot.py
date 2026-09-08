import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("train.csv")

# Convert Date column (optional but good practice)
data["Date"] = pd.to_datetime(data["Date"])

# Remove missing values (important)
data = data.dropna()

# Create boxplot
plt.figure()
plt.boxplot(data["Weekly_Sales"])

plt.title("Boxplot of Weekly Sales")
plt.ylabel("Sales")

# Save image (VERY IMPORTANT)
plt.savefig("boxplot_sales.png", dpi=300, bbox_inches='tight')

# Show graph
plt.savefig("boxplot_sales.png", dpi=300, bbox_inches='tight')
plt.show()