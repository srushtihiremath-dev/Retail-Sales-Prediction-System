import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")

data["Date"] = pd.to_datetime(data["Date"])
data["IsHoliday"] = data["IsHoliday"].astype(int)

numeric_data = data.select_dtypes(include=['number'])
corr = numeric_data.corr()

plt.figure()
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

# SAVE IMAGE (IMPORTANT)
plt.savefig("correlation_heatmap.png", dpi=300, bbox_inches='tight')

plt.show()