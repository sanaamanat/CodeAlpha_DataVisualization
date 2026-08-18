import pandas as pd

# ============================================
# 1. LOAD CLEANED DATASET
# ============================================

file_path = "dataset/cleaned_superstore.csv"

df = pd.read_csv(file_path, parse_dates=["Order Date", "Ship Date"])

print("=" * 70)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 70)


# ============================================
# 2. BASIC BUSINESS METRICS
# ============================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_products = df["Product ID"].nunique()

print("\n1. KEY BUSINESS METRICS")
print("-" * 70)

print(f"Total Sales      : ${total_sales:,.2f}")
print(f"Total Profit     : ${total_profit:,.2f}")
print(f"Total Quantity   : {total_quantity:,}")
print(f"Total Orders     : {total_orders:,}")
print(f"Total Customers  : {total_customers:,}")
print(f"Total Products   : {total_products:,}")


# ============================================
# 3. SALES BY CATEGORY
# ============================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n2. SALES BY CATEGORY")
print("-" * 70)
print(category_sales)


# ============================================
# 4. PROFIT BY CATEGORY
# ============================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n3. PROFIT BY CATEGORY")
print("-" * 70)
print(category_profit)


# ============================================
# 5. SALES BY REGION
# ============================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n4. SALES BY REGION")
print("-" * 70)
print(region_sales)


# ============================================
# 6. PROFIT BY REGION
# ============================================

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n5. PROFIT BY REGION")
print("-" * 70)
print(region_profit)


# ============================================
# 7. TOP 10 PRODUCTS BY SALES
# ============================================

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n6. TOP 10 PRODUCTS BY SALES")
print("-" * 70)

for product, sales in top_products.items():
    print(f"{product}: ${sales:,.2f}")


# ============================================
# 8. YEARLY SALES
# ============================================

yearly_sales = (
    df.groupby("Year")["Sales"]
    .sum()
    .sort_index()
)

print("\n7. YEARLY SALES")
print("-" * 70)
print(yearly_sales)


# ============================================
# 9. YEARLY PROFIT
# ============================================

yearly_profit = (
    df.groupby("Year")["Profit"]
    .sum()
    .sort_index()
)

print("\n8. YEARLY PROFIT")
print("-" * 70)
print(yearly_profit)


# ============================================
# 10. TOP 10 MOST PROFITABLE PRODUCTS
# ============================================

top_profit_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n9. TOP 10 PRODUCTS BY PROFIT")
print("-" * 70)

for product, profit in top_profit_products.items():
    print(f"{product}: ${profit:,.2f}")


# ============================================
# 11. LOSS-MAKING PRODUCTS
# ============================================

loss_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)

print("\n10. TOP 10 LOSS-MAKING PRODUCTS")
print("-" * 70)

for product, profit in loss_products.items():
    print(f"{product}: ${profit:,.2f}")


# ============================================
# 12. GENERAL PROFIT MARGIN
# ============================================

overall_profit_margin = (total_profit / total_sales) * 100

print("\n11. OVERALL PROFIT MARGIN")
print("-" * 70)
print(f"Overall Profit Margin: {overall_profit_margin:.2f}%")

print("\n" + "=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)