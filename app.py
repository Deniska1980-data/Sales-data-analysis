import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Load dataset
# ===============================
df = pd.read_csv("Sales.csv", sep=";")

print("=== Dataset Preview ===")
print(df.head(), "\n")

print("=== Columns ===")
print(df.columns.tolist(), "\n")

# ===============================
# Data Filtering Examples
# ===============================
print("=== Orders with quantity > 5 ===")
print(df[df["Order Quantity"] > 5][["Product Name", "Order Quantity"]], "\n")

print("=== Products with price < 800 ===")
print(df[df["Product Price"] < 800][["Product Name", "Product Price"]], "\n")

print("=== Paid by Credit Card AND price < 5000 ===")
filtered = df[(df["Payment Method"] == "Credit Card") & (df["Product Price"] < 5000)]
print(filtered[["Product Name", "Product Price", "Payment Method"]], "\n")

print("=== Unique product categories ===")
print(df["Product Category"].unique(), "\n")

# ===============================
# Business Metrics
# ===============================
top_revenue = df.loc[df["Order Total"].idxmax()]
low_revenue = df.loc[df["Order Total"].idxmin()]
top_sales = df.loc[df["Order Quantity"].idxmax()]
low_sales = df.loc[df["Order Quantity"].idxmin()]

print("=== Business Metrics ===")
print(f"Highest revenue: {top_revenue['Product Name']} → {top_revenue['Order Total']} CZK")
print(f"Lowest revenue: {low_revenue['Product Name']} → {low_revenue['Order Total']} CZK")
print(f"Top sales volume: {top_sales['Product Name']} → {top_sales['Order Quantity']} units")
print(f"Lowest sales volume: {low_sales['Product Name']} → {low_sales['Order Quantity']} units\n")

# ===============================
# Visualization - Revenue
# ===============================
products = [top_revenue["Product Name"], low_revenue["Product Name"]]
values = [top_revenue["Order Total"], low_revenue["Order Total"]]
colors = ["seagreen", "salmon"]

plt.bar(products, values, color=colors)
plt.title("Nejvyšší vs. Nejnižší tržby")
for i, v in enumerate(values):
    plt.text(i, v + 100, str(v), ha="center", fontsize=10, fontweight="bold")
plt.savefig("img/top_vs_low_revenue.png")
plt.show()

# ===============================
# Visualization - Sales Volume
# ===============================
products = [top_sales["Product Name"], low_sales["Product Name"]]
values = [top_sales["Order Quantity"], low_sales["Order Quantity"]]
colors = ["royalblue", "orange"]

plt.bar(products, values, color=colors)
plt.title("Nejvyšší vs. Nejnižší prodeje (kusy)")
for i, v in enumerate(values):
    plt.text(i, v + 0.1, str(v), ha="center", fontsize=10, fontweight="bold")
plt.savefig("img/top_vs_low_sales.png")
plt.show()
