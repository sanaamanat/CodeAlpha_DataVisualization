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