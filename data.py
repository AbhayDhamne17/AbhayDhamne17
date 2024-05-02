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
bar1 = plt.bar(x=new_df.index, height=new_df.Profit_P, color='dodgerblue')
plt.xticks(new_df.index, rotation='vertical')
z = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.bar_label(bar1)
plt.yticks(z)
plt.ylabel('Percentage')
plt.xlabel('Products')
plt.magma()
plt.show(bar1)

# Calculate the percentage of budget allocation for each product
bar2 = plt.bar(x=new_df.index, height=new_df.Budget_P, color='dodgerblue')
plt.xticks(new_df.index, rotation='vertical')
z = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.bar_label(bar2)
plt.yticks(z)
plt.ylabel('Percentage')
plt.xlabel('Products')
plt.show(bar2)

# Calculate the percentage of advertising spend by each product
bar3 = plt.bar(x=new_df.index, height=new_df.Ad_Spend_P, color='dodgerblue')
plt.xticks(new_df.index, rotation='vertical')
z = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
plt.bar_label(bar3)
plt.yticks(z)
plt.ylabel('Percentage')
plt.xlabel('Products')
plt.show(bar3)

#Data Visualization

bar1 = plt.bar(x=Products_Group.index, height=Products_Group.Budget, edgecolor='white', width=1, label='Budget') # Create a bar plot showing Budget allocation for each product
bar2 = plt.bar(x=Products_Group.index, height=Products_Group.Ad_Spend, edgecolor='white', width=1, bottom=Products_Group.Budget, label='Ad_Spend') # Create a bar plot showing Ad Spend on top of Budget allocation for each product
bar3 = plt.bar(x=Products_Group.index, height=Products_Group.Profit, edgecolor='white', width=1, bottom=[i+j for i, j in zip(Products_Group.Budget, Products_Group.Ad_Spend)], label='Profit') # Create a stacked bar plot showing Profit on top of Budget and Ad Spend for each product
plt.xticks(Products_Group.index, rotation='vertical') # Set the x-axis ticks to display product names vertically

# Add labels to the bars displaying their values
plt.bar_label(bar1)
plt.bar_label(bar2)
plt.bar_label(bar3)

# Display the legend and show the plot
plt.legend()
plt.show()

# Correlation Analysis
correlation_matrix = df[['Profit', 'Budget', 'Ad_Spend']].corr()  # Calculate the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  # Visualize the correlation matrix as a heatmap
plt.title('Correlation Matrix')
plt.show()
