import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/mismanaged-plastic-waste-per-capita.csv")

top10 = df.sort_values(
    by="Mismanaged plastic waste per capita",
    ascending=False
).head(10)

plt.figure(figsize=(10,6))
plt.bar(
    top10["Entity"],
    top10["Mismanaged plastic waste per capita"]
)

plt.xticks(rotation=45)
plt.title("Top 10 Countries by Mismanaged Plastic Waste Per Capita")
plt.tight_layout()

plt.show()