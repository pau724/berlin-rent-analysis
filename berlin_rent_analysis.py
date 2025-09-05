import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/berlin_rent.csv")

print("First rows of the dataset:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

avg_price = df.groupby("district")["price"].mean().sort_values(ascending=False)
print("\nAverage rent price by district:")
print(avg_price)

plt.figure(figsize=(8,6))
sns.histplot(df["price"], bins=20, kde=True)
plt.title("Distribution of Rent Prices in Berlin")
plt.xlabel("Rent Price (€)")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x=avg_price.values, y=avg_price.index, palette="viridis")
plt.title("Average Rent Price by District in Berlin")
plt.xlabel("Average Rent Price (€)")
plt.ylabel("District")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x="sqm", y="price", data=df, hue="district", alpha=0.7)
plt.title("Relationship between Size (sqm) and Rent Price")
plt.xlabel("Size (sqm)")
plt.ylabel("Rent Price (€)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
