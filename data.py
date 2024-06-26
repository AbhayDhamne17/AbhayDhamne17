import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('data.csv')
df = pd.DataFrame(data)
df.sort_index(inplace=True)
df.isnull()
df.duplicated()
print(df)

df.set_index(['Date'], inplace=True)
Products_Group = df.groupby('Product')[['Revenue', 'Expenses', 'Profit']].sum()
print(Products_Group)

Profit_P = Products_Group.loc[Products_Group.index, 'Profit'] / Products_Group.Profit.sum() * 100
Revenue_P = Products_Group.loc[Products_Group.index, 'Revenue'] / Products_Group.Revenue.sum() * 100
Expenses_P = Products_Group.loc[Products_Group.index, 'Expenses'] / Products_Group.Expenses.sum() * 100

# Identify products with expenses exceeding profit
more_expenses = df.query('Expenses > Profit')[['Product', 'Expenses', 'Profit']]

# Set the 'Date' column as the index
#more_expenses.set_index('Date', inplace=True)

# Calculate the difference between expenses and profit
more_expenses['Difference'] = more_expenses['Expenses'] - more_expenses['Profit']

# Sort products by spending difference in descending order
spending_difference = more_expenses.sort_values(by=['Difference'], ascending=False)

# Find the date with the highest spending difference
max_spending_date = spending_difference.Difference.idxmax()
max_spending_difference = spending_difference.Difference.max()

# Print the results
print(f"Date with the highest spending difference: {max_spending_date}")
print(f"Maximum spending difference: {max_spending_difference}")
print(spending_difference)
-----------------

# Calculate the percentage of profit contribution by each product
bar1 = plt.bar(x=Products_Group.index, height=Profit_P.values.round(2), color='dodgerblue')
plt.xticks(Products_Group.index, rotation='vertical')
z = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.bar_label(bar1)
plt.yticks(z)
plt.ylabel('Percentage')
plt.xlabel('Products')
plt.magma()
plt.show(bar1)

# Calculate the percentage of Expenses on each product
bar2 = plt.bar(x=Products_Group.index, height=Expenses_P.values.round(2), color='dodgerblue')
plt.xticks(Products_Group.index, rotation='vertical')
z = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.bar_label(bar2)
plt.yticks(z)
plt.ylabel('Percentage')
plt.xlabel('Products')
plt.show(bar2)

# Calculate the percentage of Revenue generated by each product
bar3 = plt.bar(x=Products_Group.index, height=Revenue_P.values.round(2), color='dodgerblue')
plt.xticks(Products_Group.index, rotation='vertical')
z = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.bar_label(bar3)
plt.yticks(z)
plt.ylabel('Percentage')
plt.xlabel('Products')
plt.show(bar3)

print(f"Highest Profit: {Profit_P.idxmax()} generated the highest profit of ${Products_Group.Profit.max()} with a profit percentage of {Profit_P.max().round(2)}%")
print(f"Lowest Profit: {Profit_P.idxmin()} generated the lowest profit of ${Products_Group.Profit.min()} with a profit percentage of {Profit_P.min().round(2)}%")
print(f"Highest Expenses: {Expenses_P.idxmax()} had the highest expenses of ${Products_Group.Expenses.max()}")
print(f"Lowest Expenses: {Expenses_P.idxmin()} had the lowest expenses of ${Products_Group.Expenses.min()}")
print(f"Highest Revenue: {Revenue_P.idxmax()} generated the highest revenue of ${Products_Group.Revenue.max()}")
print(f"Lowest Revenue: {Revenue_P.idxmin()} generated the lowest revenue of ${Products_Group.Revenue.min()}")

#Data Visualization

bar1 = plt.bar(x=Products_Group.index, height=Products_Group.Expenses, edgecolor='white', width=1, label='Expenses') # Create a bar plot showing Budget allocation for each product
bar2 = plt.bar(x=Products_Group.index, height=Products_Group.Revenue, edgecolor='white', width=1, bottom=Products_Group.Expenses, label='Revenue') # Create a bar plot showing Ad Spend on top of Budget allocation for each product
bar3 = plt.bar(x=Products_Group.index, height=Products_Group.Profit, edgecolor='white', width=1, bottom=[i+j for i, j in zip(Products_Group.Expenses, Products_Group.Revenue)], label='Profit') # Create a stacked bar plot showing Profit on top of Budget and Ad Spend for each product
plt.xticks(Products_Group.index, rotation='vertical') # Set the x-axis ticks to display product names vertically

# Add labels to the bars displaying their values
plt.bar_label(bar1)
plt.bar_label(bar2)
plt.bar_label(bar3)

# Display the legend and show the plot
plt.legend()
plt.show()

# Correlation Analysis
correlation_matrix = df[['Revenue', 'Expenses', 'Profit']].corr()  # Calculate the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  # Visualize the correlation matrix as a heatmap
plt.title('Correlation Matrix')
plt.show()
