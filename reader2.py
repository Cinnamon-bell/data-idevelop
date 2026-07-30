import pandas as pd

df = pd.read_csv("sales.csv")

total = df["unit_price"].sum()

top3 = df.nlargest(3, "unit_price")[["order_id", "product", "unit_price"]]

df["revenue"] = df["units"] * df["unit_price"]

revenue_per_region = df.groupby("region")["revenue"].sum()

print("Total unit price:", total)

print("\nTop 3 unit prices:")
for i, (_, row) in enumerate(top3.iterrows(), start=1):
    print(f"Top {i}: {row['order_id']} {row['product']} with price: {row['unit_price']}")

print("\nRevenue per region:")
print(revenue_per_region)