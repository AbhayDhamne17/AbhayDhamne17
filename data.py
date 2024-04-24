import pandas as pd  # Import the pandas library as pd for data manipulation
import numpy as np  # Import the numpy library as np for numerical computations
import matplotlib.pyplot as plt  # Import the matplotlib library for plotting
import seaborn as sns  # Import the seaborn library for data visualization

data = pd.read_csv('data.csv')  # Read the data from a CSV file into a pandas DataFrame
df = pd.DataFrame(data)  # Create a DataFrame from the read data

#Data Cleaning

df.rename(columns={'-01-08':'Products', '1600':'Date', '1':'Profit', '850':'Budget', '4':'Ad_Spend'}, inplace=True)  # Rename the columns with correct names
df.sort_values(by=['Date'], inplace=True)  # Sort the DataFrame by the 'Date' column
df.drop_duplicates(subset=['Date'], inplace=True)  # Drop duplicate rows based on the 'Date' column
df.set_index(['Date'], inplace=True)  # Set the 'Date' column as the index of the DataFrame

df.Budget.fillna(method='ffill', inplace=True)  # Fill missing values in the 'Budget' column with the last valid value
df.Ad_Spend.fillna(method='bfill', inplace=True)  # Fill missing values in the 'Ad_Spend' column with the next valid value

#Data Manupulation

# Group the DataFrame 'df' by the 'Products' column and calculate the sum of 'Profit', 'Budget', and 'Ad_Spend' for each group
Products_Group = df.groupby('Products')[['Profit', 'Budget', 'Ad_Spend']].sum()

# Calculate the percentage of profit contribution by each product
Products_By_Profit = Products_Group.loc[Products_Group.index, 'Profit'] / Products_Group.Profit.sum() * 100
bar1 = plt.bar(x=Products_By_Profit.index, height=Products_By_Profit.values)
plt.xticks(Products_By_Profit.index, rotation='vertical')
plt.yticks(Products_By_Profit.values)
print(bar1)

# Calculate the percentage of budget allocation for each product
Products_By_Budget = Products_Group.loc[Products_Group.index, 'Budget'] / Products_Group.Budget.sum() * 100
bar2 = plt.bar(x=Products_By_Budget.index, height=Products_By_Budget.values)
plt.xticks(Products_By_Budget.index, rotation='vertical')
plt.yticks(Products_By_Budget.values)
print(bar2)

# Calculate the percentage of advertising spend by each product
Products_By_Ad_Spend = Products_Group.loc[Products_Group.index, 'Ad_Spend'] / Products_Group.Ad_Spend.sum() * 100
bar3 = plt.bar(x=Products_By_Ad_Spend.index, height=Products_By_Ad_Spend.values)
plt.xticks(Products_By_Ad_Spend.index, rotation='vertical')
plt.yticks(Products_By_Ad_Spend.values)
print(bar3)


more_ad_spend = df.query('Ad_Spend > Budget')[['Products', 'Date', 'Ad_Spend', 'Budget']] # Dates when 'Ad_Spend' is greater than 'Budget'
more_ad_spend.set_index('Date', inplace=True) # Set the 'Date' column as the index of the DataFrame
more_ad_spend['Difference'] = more_ad_spend.Ad_Spend - more_ad_spend.Budget # Calculate the difference between Ad Spend and Budget
spending_difference = more_ad_spend.sort_values(by=['Difference'], ascending=False) # Sort the DataFrame by the 'Difference' column in descending order
spending_difference.Difference.idxmax() #The date when there was the highest difference between Advertisement Budget and Advertisement Spending.

print(Products_Group)
print(df)  # Print the cleaned DataFrame

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
