import pandas as pd
import matplotlib.pyplot as plt

# SAMPLE SALES DATA
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Headphones', 'Laptop', 'Phone', 'Tablet', 'Monitor', 'Headphones'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories'],
    'Region': ['North', 'North', 'North', 'South', 'South', 'East', 'East', 'West', 'West', 'West'],
    'Sales': [12500, 8900, 5600, 4300, 2100, 11200, 9500, 6100, 4800, 1950],
    'Month': ['Jan', 'Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb', 'Feb', 'Feb']
}

df = pd.DataFrame(data)

# ANALYSIS
print("=" * 50)
print("SALES ANALYSIS REPORT")
print("=" * 50)

print("\n📊 TOTAL SALES BY PRODUCT:")
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print(product_sales)
print(f"\n🏆 TOP SELLING PRODUCT: {product_sales.index[0]} (${product_sales.iloc[0]:,})")

print("\n📁 TOTAL SALES BY CATEGORY:")
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)

print("\n🌍 TOTAL SALES BY REGION:")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)
print(f"\n📍 BEST REGION: {region_sales.index[0]} (${region_sales.iloc[0]:,})")

print("\n📈 MONTHLY TREND:")
monthly_sales = df.groupby('Month')['Sales'].sum()
print(monthly_sales)

if monthly_sales.iloc[1] > monthly_sales.iloc[0]:
    print("\n✅ TREND: Sales INCREASED from Jan to Feb")
else:
    print("\n⚠️ TREND: Sales DECREASED from Jan to Feb")

print("\n" + "=" * 50)
print("RECOMMENDATIONS:")
print("=" * 50)
print("1. Focus marketing on Laptops - highest revenue product")
print("2. North region is top performer - replicate strategy elsewhere")
print("3. Accessories category has growth potential")
print("4. Consider bundling low-selling products with top sellers")
