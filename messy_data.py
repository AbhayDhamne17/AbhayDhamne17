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

# Group the DataFrame 'df' by the 'Products' column and calculate the sum of 'Profit', 'Budget', and 'Ad_Spend' for each group
Products_Group = df.groupby('Products')[['Profit', 'Budget', 'Ad_Spend']].sum()
print(Products_Group)

Products_By_Profit = Products_Group.loc[Products_Group.index, 'Profit'] / Products_Group.Profit.sum() * 100
Products_By_Budget = Products_Group.loc[Products_Group.index, 'Budget'] / Products_Group.Budget.sum() * 100
Products_By_Ad_Spend = Products_Group.loc[Products_Group.index, 'Ad_Spend'] / Products_Group.Ad_Spend.sum() * 100

merge1 = pd.merge(Products_Group.Profit, Products_By_Profit, on=Products_Group.index).set_index('key_0') # Merge Profit data from Products_Group and Products_By_Profit on the index, set index to 'key_0'
merge2 = pd.merge(Products_Group.Budget, Products_By_Budget, on=Products_Group.index).set_index('key_0') # Merge Budget data from Products_Group and Products_By_Budget on the index, set index to 'key_0'
merge3 = pd.merge(Products_Group.Ad_Spend, Products_By_Ad_Spend, on=Products_Group.index).set_index('key_0') # Merge Ad Spend data from Products_Group and Products_By_Ad_Spend on the index, set index to 'key_0'

# Merge the merged Profit and Budget dataframes, then merge with Ad Spend dataframe, setting index to 'key_0'
merge1_2 = pd.merge(merge1, merge2, on=merge1.index).set_index('key_0')
merge1_2_3 = pd.merge(merge1_2, merge3, on=merge1_2.index).set_index('key_0')

# We can also use `pd.merge` to combine all three DataFrames in one step: "merged_df = pd.merge(merge1, merge2, merge3, left_index=True, right_index=True).set_index('key_0')" This approach is more concise and efficient, as it avoids the need to perform multiple merge operations.

# Create a new DataFrame using the merged data, renaming columns for clarity
new_df = pd.DataFrame(data=merge1_2_3)
new_df.rename(columns={'Profit_x':'Profit', 'Profit_y':'Profit_P', 'Budget_x':'Budget', 'Budget_y':'Budget_P', 'Ad_Spend_x':'Ad_Spend', 'Ad_Spend_y':'Ad_Spend_P'}, inplace=True)
new_df.rename_axis('Products', inplace=True)

# Round the Profit_P, Budget_P, and Ad_Spend_P columns to 2 decimal places
new_df.Profit_P = new_df['Profit_P'].round(2)
new_df.Budget_P = new_df['Budget_P'].round(2)
new_df.Ad_Spend_P = new_df['Ad_Spend_P'].round(2)
print(new_df)
