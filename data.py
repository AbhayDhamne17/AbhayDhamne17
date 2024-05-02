


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
more_ad_spend.set_index('Date', inplace=True) # Set the 'Date' column as the index of the DataFrame
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
