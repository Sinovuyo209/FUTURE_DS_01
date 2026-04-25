"""
TASK 1: Sales Data Analysis
Future Interns - Data Science & Analytics
"""

import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# SAMPLE SALES DATA
# ============================================

sales_data = {
    'Date': ['2024-01-05', '2024-01-12', '2024-01-19', '2024-01-26',
             '2024-02-02', '2024-02-09', '2024-02-16', '2024-02-23',
             '2024-03-01', '2024-03-08', '2024-03-15', '2024-03-22'],
    'Product': ['Laptop Pro', 'Wireless Mouse', 'Laptop Pro', 'USB-C Hub',
                'Wireless Mouse', 'Laptop Pro', 'USB-C Hub', 'Wireless Mouse',
                'Laptop Pro', 'USB-C Hub', 'Wireless Mouse', 'Laptop Pro'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories',
                 'Accessories', 'Electronics', 'Accessories', 'Accessories',
                 'Electronics', 'Accessories', 'Accessories', 'Electronics'],
    'Region': ['North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West'],
    'Quantity': [5, 20, 8, 15, 25, 10, 18, 30, 12, 22, 28, 7],
    'Unit_Price': [1200, 25, 1200, 40, 25, 1200, 40, 25, 1200, 40, 25, 1200]
}

df = pd.DataFrame(sales_data)
df['Revenue'] = df['Quantity'] * df['Unit_Price']
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%B')

# ============================================
# ANALYSIS
# ============================================

print("=" * 60)
print("SALES ANALYSIS REPORT")
print("Data Science & Analytics - Future Interns")
print("=" * 60)

# 1. REVENUE TRENDS BY MONTH
print("\n📈 REVENUE TRENDS BY MONTH:")
monthly_revenue = df.groupby('Month')['Revenue'].sum()
for month, revenue in monthly_revenue.items():
    print(f"   {month}: ${revenue:,.0f}")

# 2. TOP SELLING PRODUCTS
print("\n🏆 TOP SELLING PRODUCTS (by Revenue):")
product_revenue = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
for i, (product, revenue) in enumerate(product_revenue.items(), 1):
    print(f"   {i}. {product}: ${revenue:,.0f}")
top_product = product_revenue.index[0]

# 3. HIGH-VALUE CATEGORIES
print("\n📁 REVENUE BY CATEGORY:")
category_revenue = df.groupby('Category')['Revenue'].sum()
for category, revenue in category_revenue.items():
    percentage = (revenue / category_revenue.sum()) * 100
    print(f"   {category}: ${revenue:,.0f} ({percentage:.1f}%)")

# 4. REGIONAL PERFORMANCE
print("\n🌍 REVENUE BY REGION:")
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
for region, revenue in region_revenue.items():
    print(f"   {region}: ${revenue:,.0f}")
top_region = region_revenue.index[0]

# ============================================
# KEY INSIGHTS
# ============================================

print("\n" + "=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

print(f"\n✅ Top selling product: {top_product}")
print(f"✅ Best performing region: {top_region}")
print(f"✅ Electronics category contributes {((category_revenue['Electronics']/category_revenue.sum())*100):.1f}% of revenue")

# Trend analysis
if len(monthly_revenue) >= 2:
    months = list(monthly_revenue.index)
    if monthly_revenue.iloc[-1] > monthly_revenue.iloc[0]:
        print(f"✅ Revenue INCREASED from {months[0]} to {months[-1]}")
    else:
        print(f"⚠️ Revenue DECREASED from {months[0]} to {months[-1]}")

# ============================================
# ACTIONABLE RECOMMENDATIONS
# ============================================

print("\n" + "=" * 60)
print("ACTIONABLE RECOMMENDATIONS")
print("=" * 60)

print("""
1. Increase marketing spend on Laptop Pro - it's the highest revenue driver

2. Expand North region strategy to East and West regions - replicate what works

3. Bundle Accessories with Electronics purchases to increase average order value

4. Run regional promotions in underperforming regions (South and West)

5. Consider subscription model for accessories to stabilize revenue
""")

# ============================================
# OPTIONAL: Generate simple chart
# ============================================

try:
    # Bar chart for product revenue
    plt.figure(figsize=(8, 5))
    product_revenue.plot(kind='bar', color='skyblue')
    plt.title('Revenue by Product')
    plt.xlabel('Product')
    plt.ylabel('Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('product_revenue_chart.png')
    print("\n✅ Chart saved as 'product_revenue_chart.png'")
except:
    print("\n⚠️ Chart generation requires matplotlib - install with: pip install matplotlib")

print("\n" + "=" * 60)
print("REPORT END")
print("=" * 60)
