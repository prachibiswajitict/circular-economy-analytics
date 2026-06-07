import pandas as pd

df = pd.read_csv("data/raw/mismanaged-plastic-waste-per-capita.csv")

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("data/cleaned_mismanaged_plastic_waste.csv", index=False)

print("Cleaned dataset saved successfully!")
print(df.head())