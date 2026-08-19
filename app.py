import pandas as pd
import streamlit as st
import plotly.express as px

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="E-Commerce Sales Analytics",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    file_path = "dataset/cleaned_superstore.csv"

    data = pd.read_csv(
        file_path,
        parse_dates=["Order Date", "Ship Date"]
    )

    return data


df = load_data()

# ============================================================
# TITLE
# ============================================================

st.title("📊 E-Commerce Sales Analytics Dashboard")

st.markdown(
    """
    This interactive dashboard provides an overview of sales,
    profitability, product performance, and regional performance.
    """
)

# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("Dashboard Filters")

# Year filter
years = sorted(df["Year"].dropna().unique())

selected_years = st.sidebar.multiselect(
    "Select Year",
    options=years,
    default=years
)

# Region filter
regions = sorted(df["Region"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=regions,
    default=regions
)

# Category filter
categories = sorted(df["Category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=categories,
    default=categories
)

# Segment filter
segments = sorted(df["Segment"].dropna().unique())

selected_segments = st.sidebar.multiselect(
    "Select Customer Segment",
    options=segments,
    default=segments
)

# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    df["Year"].isin(selected_years)
    & df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
    & df["Segment"].isin(selected_segments)
]

# ============================================================
# KPI CALCULATIONS
# ============================================================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
total_customers = filtered_df["Customer ID"].nunique()

# ============================================================
# KPI CARDS
# ============================================================

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Total Orders",
    f"{total_orders:,}"
)

col4.metric(
    "Total Customers",
    f"{total_customers:,}"
)

# ============================================================
# CHECK EMPTY FILTER RESULT
# ============================================================

if filtered_df.empty:

    st.warning(
        "No data available for the selected filters. "
        "Please select different filter values."
    )

    st.stop()

# ============================================================
# SALES TREND
# ============================================================

st.subheader("📈 Sales Trend Over Time")

monthly_sales = (
    filtered_df
    .groupby("Year-Month", as_index=False)["Sales"]
    .sum()
)

fig_sales = px.line(
    monthly_sales,
    x="Year-Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

fig_sales.update_layout(
    xaxis_title="Month",
    yaxis_title="Sales ($)"
)

st.plotly_chart(
    fig_sales,
    use_container_width=True
)

# ============================================================
# PROFIT TREND
# ============================================================

st.subheader("💰 Profit Trend Over Time")

monthly_profit = (
    filtered_df
    .groupby("Year-Month", as_index=False)["Profit"]
    .sum()
)

fig_profit = px.line(
    monthly_profit,
    x="Year-Month",
    y="Profit",
    markers=True,
    title="Monthly Profit Trend"
)

fig_profit.update_layout(
    xaxis_title="Month",
    yaxis_title="Profit ($)"
)

st.plotly_chart(
    fig_profit,
    use_container_width=True
)

# ============================================================
# CATEGORY ANALYSIS
# ============================================================

col1, col2 = st.columns(2)

with col1:

    category_sales = (
        filtered_df
        .groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig_category_sales = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )

    fig_category_sales.update_layout(
        xaxis_title="Category",
        yaxis_title="Sales ($)"
    )

    st.plotly_chart(
        fig_category_sales,
        use_container_width=True
    )

with col2:

    category_profit = (
        filtered_df
        .groupby("Category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    fig_category_profit = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        title="Profit by Category"
    )

    fig_category_profit.update_layout(
        xaxis_title="Category",
        yaxis_title="Profit ($)"
    )

    st.plotly_chart(
        fig_category_profit,
        use_container_width=True
    )

# ============================================================
# REGION ANALYSIS
# ============================================================

col1, col2 = st.columns(2)

with col1:

    region_sales = (
        filtered_df
        .groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig_region_sales = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region"
    )

    fig_region_sales.update_layout(
        xaxis_title="Region",
        yaxis_title="Sales ($)"
    )

    st.plotly_chart(
        fig_region_sales,
        use_container_width=True
    )

with col2:

    region_profit = (
        filtered_df
        .groupby("Region", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    fig_region_profit = px.bar(
        region_profit,
        x="Region",
        y="Profit",
        title="Profit by Region"
    )

    fig_region_profit.update_layout(
        xaxis_title="Region",
        yaxis_title="Profit ($)"
    )

    st.plotly_chart(
        fig_region_profit,
        use_container_width=True
    )

# ============================================================
# TOP 10 PRODUCTS
# ============================================================

st.subheader("🏆 Top 10 Products by Sales")

top_products = (
    filtered_df
    .groupby("Product Name", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
    .head(10)
    .sort_values("Sales")
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales"
)

fig_products.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="Product"
)

st.plotly_chart(
    fig_products,
    use_container_width=True
)

# ============================================================
# SALES VS PROFIT
# ============================================================

st.subheader("🔎 Sales vs Profit")

fig_scatter = px.scatter(
    filtered_df,
    x="Sales",
    y="Profit",
    size="Quantity",
    hover_name="Product Name",
    title="Sales vs Profit",
    opacity=0.6
)

fig_scatter.update_layout(
    xaxis_title="Sales ($)",
    yaxis_title="Profit ($)"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)

# ============================================================
# DATA TABLE
# ============================================================

st.subheader("📋 Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "CodeAlpha Data Visualization Project | "
    "Built with Python, Pandas, Plotly and Streamlit"
)