import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel('Online Retail.xlsx')

# Drop rows with missing CustomerID, as it’s essential for customer-based analysis
data = data.dropna(subset=['CustomerID'])

# Filter out negative or zero quantities as they may represent returns or errors
data = data[data['Quantity'] > 0]

# Remove duplicates if any
data = data.drop_duplicates()

# Check the range of the Quantity column
print(f"Minimum Quantity: {data['Quantity'].min()}")
print(f"Maximum Quantity: {data['Quantity'].max()}")

# Plot a histogram with a limited x-axis to exclude outliers
plt.figure(figsize=(10, 6))
plt.hist(data['Quantity'], bins=50, edgecolor='black', range=(1, 100))  # This range we just focus on typical quantities
plt.title('Adjusted Quantity Distribution')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# Create a total sales column
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

# Group by date and sum total sales
daily_sales = data.groupby(data['InvoiceDate'].dt.date)['TotalPrice'].sum()

# Plot daily sales trend
plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales.values, marker='o', linestyle='-')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Calculate correlation matrix
correlation_matrix = data[['Quantity', 'UnitPrice', 'TotalPrice']].corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()

# Filter the data to include only the top 10 countries by transaction count
top_countries = data['Country'].value_counts().nlargest(10).index
data_top_countries = data[data['Country'].isin(top_countries)]

# Plot the violin plot for Unit Price by Country
plt.figure(figsize=(12, 8))
sns.violinplot(data=data_top_countries, x='Country', y='UnitPrice')
plt.title('Distribution of Unit Price by Country (Top 10 Countries)')
plt.xlabel('Country')
plt.ylabel('Unit Price')
plt.xticks(rotation=45)
plt.show()

# Summary statistics
print(data[['Quantity', 'UnitPrice', 'TotalPrice']].describe())

# Correlation matrix
print(data[['Quantity', 'UnitPrice', 'TotalPrice']].corr())

