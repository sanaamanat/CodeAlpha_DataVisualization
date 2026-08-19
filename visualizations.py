import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================
# LOAD CLEANED DATASET
# ============================================

file_path = "dataset/cleaned_superstore.csv"

df = pd.read_csv(
    file_path,
    parse_dates=["Order Date", "Ship Date"]
)

# ============================================
# CREATE IMAGES FOLDER
# ============================================

os.makedirs("images", exist_ok=True)

# ============================================
# MONTHLY SALES TREND
# ============================================

monthly_sales = (
    df.groupby("Year-Month")["Sales"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["Year-Month"],
    monthly_sales["Sales"],
    marker="o",
    linewidth=2
)

plt.title(
    "Monthly Sales Trend",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Month", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

# Save chart
output_file = "images/monthly_sales_trend.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Monthly Sales Trend created successfully!")
print("Saved to:", output_file)


# ============================================
# SALES BY CATEGORY
# ============================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title(
    "Sales by Product Category",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Category", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)

plt.xticks(rotation=0)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

output_file = "images/sales_by_category.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Sales by Category chart created successfully!")
print("Saved to:", output_file)

# ============================================
# PROFIT BY CATEGORY
# ============================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

plt.bar(
    category_profit.index,
    category_profit.values
)

plt.title(
    "Profit by Product Category",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Category", fontsize=12)
plt.ylabel("Profit ($)", fontsize=12)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

output_file = "images/profit_by_category.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Profit by Category chart created successfully!")
print("Saved to:", output_file)

# ============================================
# SALES BY REGION
# ============================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9, 6))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title(
    "Sales by Region",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Region", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

output_file = "images/sales_by_region.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Sales by Region chart created successfully!")
print("Saved to:", output_file)

# ============================================
# TOP 10 PRODUCTS BY SALES
# ============================================

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .sort_values()
)

plt.figure(figsize=(12, 7))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title(
    "Top 10 Products by Sales",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel("Sales ($)", fontsize=12)
plt.ylabel("Product", fontsize=12)

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

output_file = "images/top_10_products.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Top 10 Products chart created successfully!")
print("Saved to:", output_file)