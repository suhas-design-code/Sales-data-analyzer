import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data
data = pd.read_csv("sales.csv")
print("Data loaded successfully!")
print(data.head())

# Step 2: Basic analysis
print("\nSummary Statistics:")
print(data.describe())

# Step 3: Group by region
region_sales = data.groupby("Region")["Sales"].sum()
print("\nSales by Region:")
print(region_sales)

# Step 4: Visualization
region_sales.plot(kind="bar", title="Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
