import pandas as pd

# Read the dataset
df = pd.read_csv("data/raw/mismanaged-plastic-waste-per-capita.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Top 10 countries
top10 = df.sort_values(
    by="Mismanaged plastic waste per capita",
    ascending=False
).head(10)

print("\nTop 10 Countries:")
print(top10[["Entity", "Mismanaged plastic waste per capita"]])