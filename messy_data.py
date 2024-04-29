import pandas as pd  # Import the pandas library as pd for data manipulation
import numpy as np  # Import the numpy library as np for numerical computations
import matplotlib.pyplot as plt  # Import the matplotlib library for plotting
import seaborn as sns  # Import the seaborn library for data visualization

data = pd.read_csv('messy_data.csv')  # Read the data from a CSV file into a pandas DataFrame
df = pd.DataFrame(data)  # Create a DataFrame from the read data

#Data Cleaning
df.rename(columns={'-01-08':'Products', '1600':'Date', '1':'Profit', '850':'Budget', '4':'Ad_Spend'}, inplace=True)  # Rename the columns with correct names
df.sort_values(by=['Date'], inplace=True)  # Sort the DataFrame by the 'Date' column
df.drop_duplicates(subset=['Date'], inplace=True)  # Drop duplicate rows based on the 'Date' column
df.set_index(['Date'], inplace=True)  # Set the 'Date' column as the index of the DataFrame

df.Budget.fillna(method='ffill', inplace=True)  # Fill missing values in the 'Budget' column with the last valid value
df.Ad_Spend.fillna(method='bfill', inplace=True)  # Fill missing values in the 'Ad_Spend' column with the next valid value
print(df)

#Data Manupulation

# Group the DataFrame 'df' by the 'Products' column and calculate the sum of 'Profit', 'Budget', and 'Ad_Spend' for each group
Products_Group = df.groupby('Products')[['Profit', 'Budget', 'Ad_Spend']].sum()
print(Products_Group)

merge1 = pd.merge(Products_Group.Profit, Products_By_Profit, on=Products_Group.index).set_index('key_0') # Merge Profit data from Products_Group and Products_By_Profit on the index, set index to 'key_0'
merge2 = pd.merge(Products_Group.Budget, Products_By_Budget, on=Products_Group.index).set_index('key_0') # Merge Budget data from Products_Group and Products_By_Budget on the index, set index to 'key_0'
merge3 = pd.merge(Products_Group.Ad_Spend, Products_By_Ad_Spend, on=Products_Group.index).set_index('key_0') # Merge Ad Spend data from Products_Group and Products_By_Ad_Spend on the index, set index to 'key_0'

# Merge the merged Profit and Budget dataframes, then merge with Ad Spend dataframe, setting index to 'key_0'
merge1_2 = pd.merge(merge1, merge2, on=merge1.index).set_index('key_0')
merge1_2_3 = pd.merge(merge1_2, merge3, on=merge1_2.index).set_index('key_0')

# Create a new DataFrame using the merged data, renaming columns for clarity
new_df = pd.DataFrame(data=merge1_2_3)
new_df.rename(columns={'Profit_x':'Profit', 'Profit_y':'Profit_P', 'Budget_x':'Budget', 'Budget_y':'Budget_P', 'Ad_Spend_x':'Ad_Spend', 'Ad_Spend_y':'Ad_Spend_P'}, inplace=True)
new_df.rename_axis('Products', inplace=True)

# Round the Profit_P, Budget_P, and Ad_Spend_P columns to 2 decimal places
new_df.Profit_P = new_df['Profit_P'].round(2)
new_df.Budget_P = new_df['Budget_P'].round(2)
new_df.Ad_Spend_P = new_df['Ad_Spend_P'].round(2)
print(new_df)

Products_By_Profit = Products_Group.loc[Products_Group.index, 'Profit'] / Products_Group.Profit.sum() * 100
Products_By_Budget = Products_Group.loc[Products_Group.index, 'Budget'] / Products_Group.Budget.sum() * 100
Products_By_Ad_Spend = Products_Group.loc[Products_Group.index, 'Ad_Spend'] / Products_Group.Ad_Spend.sum() * 100

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

more_ad_spend = df.query('Ad_Spend > Budget')[['Products', 'Ad_Spend', 'Budget']] # Dates when 'Ad_Spend' is greater than 'Budget'
#more_ad_spend.set_index('Date', inplace=True) # Set the 'Date' column as the index of the DataFrame
more_ad_spend['Difference'] = more_ad_spend.Ad_Spend - more_ad_spend.Budget # Calculate the difference between Ad Spend and Budget
spending_difference = more_ad_spend.sort_values(by=['Difference'], ascending=False) # Sort the DataFrame by the 'Difference' column in descending order
spending_difference.Difference.idxmax() #The date when there was the highest difference between Advertisement Budget and Advertisement Spending.
print(spending_difference)
#print(df)  # Print the cleaned DataFrame

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
