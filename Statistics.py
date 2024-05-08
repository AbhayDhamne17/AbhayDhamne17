import pandas as pd

# Create the DataFrame with customer purchase data
data = {
    'customer_id': [1, 2, 3, 4, 5],
    'electronics': [1, 1, 0, 0, 1],
    'clothing': [1, 0, 1, 0, 0],
    'watches': [0, 0, 1, 0, 1],
    'groceries': [0, 1, 0, 1, 0]
}

# Display the customer purchase data
df = pd.DataFrame(data)
df.set_index('customer_id', inplace=True)
print(df)

# Calculate overall probabilities of making a purchase
total_customers = len(df.electronics)
total_purchases = df['electronics'].sum()

p_purchase = total_purchases / total_customers

p_electronics = df['electronics'].mean()
p_clothing = df['clothing'].mean()
p_watches = df['watches'].mean()
p_groceries = df['groceries'].mean()

# Display the overall probabilities of making a purchase
print("Overall probability of making a purchase of electronics:", p_purchase)
print("Overall probability of making a purchase of clothing:", p_clothing)
print("Overall probability of making a purchase of watches:", p_watches)
print("Overall probability of making a purchase of groceries:", p_groceries)
