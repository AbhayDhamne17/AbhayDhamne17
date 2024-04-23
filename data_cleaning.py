import pandas as pd  # Import the pandas library as pd for data manipulation
import numpy as np  # Import the numpy library as np for numerical computations
import matplotlib.pyplot as plt  # Import the matplotlib library for plotting
import seaborn as sns  # Import the seaborn library for data visualization

data = pd.read_csv('data.csv')  # Read the data from a CSV file into a pandas DataFrame
df = pd.DataFrame(data)  # Create a DataFrame from the read data

# Renaming the wrong column names
df.rename(columns={'-01-08':'Products', '1600':'Date', '1':'Profit', '850':'Budget', '4':'Ad_Spend'}, inplace=True)  # Rename the columns with correct names
df.sort_values(by=['Date'], inplace=True)  # Sort the DataFrame by the 'Date' column
df.drop_duplicates(subset=['Date'], inplace=True)  # Drop duplicate rows based on the 'Date' column
df.set_index(['Date'], inplace=True)  # Set the 'Date' column as the index of the DataFrame

df.Budget.fillna(method='ffill', inplace=True)  # Fill missing values in the 'Budget' column with the last valid value
df.Ad_Spend.fillna(method='bfill', inplace=True)  # Fill missing values in the 'Ad_Spend' column with the next valid value
print(df)  # Print the cleaned DataFrame
