import pandas as pd

#Probability Example 1

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

#------------------------------------------------------------------------------------------------

#probability Example 2

import random

# Simulating rolling a die
outcome = random.randint(1, 6)
probability_of_4 = 1 / 6  # There's one 4 on the die

print("Outcome:", outcome)
print("Probability of rolling a 4:", probability_of_4)

#------------------------------------------------------------------------------------------------

#Complement Example 1

# Total marbles
total_marbles = 5  # 2 red and 3 blue

# Probability of picking a blue marble given it's not red
probability_blue_given_not_red = 3 / total_marbles * 100

print("Probability of Blue:", probability_blue_given_not_red)

#------------------------------------------------------------------------------------------------

#Complement Example 2

p_heart = 13 / 52
p_not_heart = 1 - p_heart
print("Probability of drawing a heart:", p_heart)
print("Probability of not drawing a heart:", p_not_heart)

#------------------------------------------------------------------------------------------------

#Intersection Example

# Event A: Rolling an even number
probability_even = 3 / 6  # There are three even numbers (2, 4, 6)

# Event B: Rolling a number greater than 2
probability_greater_than_2 = 4 / 6  # There are four numbers greater than 2 (3, 4, 5, 6)

# Intersection of A and B: Rolling an even number greater than 2
intersection_probability = probability_even * probability_greater_than_2

print("Probability of rolling an even number and greater than 2:", intersection_probability)

#------------------------------------------------------------------------------------------------

#Union Example

# Union of A and B: Rolling an even number or a number greater than 2
union_probability = probability_even + probability_greater_than_2 - intersection_probability

print("Probability of rolling an even number or greater than 2:", union_probability)

#------------------------------------------------------------------------------------------------

#Probability Example 3

p_heart = 13 / 52
p_king = 4 / 52
p_heart_and_king = 1 / 52  # Intersection
p_heart_or_king = p_heart + p_king - p_heart_and_king  # Union

print(f"Probability of drawing a heart (P(Heart)): {p_heart}")
print(f"Probability of drawing a king (P(King)): {p_king}")
print(f"Probability of drawing a heart or a king (P(Heart ∪ King)): {p_heart_or_king}")
print(f"Probability of drawing a heart and a king (P(Heart ∩ King)): {p_heart_and_king}")

#------------------------------------------------------------------------------------------------

#Bayes' Theorem

# Probabilities
P_Bag1 = 1 / 2  # Probability of picking Bag 1
P_Bag2 = 1 / 2  # Probability of picking Bag 2
P_Blue_given_Bag1 = 3 / 5  # Probability of picking a blue marble from Bag 1
P_Blue_given_Bag2 = 4 / 7  # Probability of picking a blue marble from Bag 2
print(P_Bag1)
print(P_Bag2)
print(P_Blue_given_Bag1)
print(P_Blue_given_Bag2)
# Total probability of picking a blue marble
P_Blue = (P_Blue_given_Bag1 * P_Bag1) + (P_Blue_given_Bag2 * P_Bag2)
print(P_Blue)
# Bayes' Theorem: P(Bag1 | Blue)
P_Bag1_given_Blue = (P_Blue_given_Bag1 * P_Bag1) / P_Blue
P_Bag2_given_Blue = (P_Blue_given_Bag2 * P_Bag2) / P_Blue
print("Probability of being from Bag 1 if the marble is blue:", P_Bag1_given_Blue*100)
print("Probability of being from Bag 2 if the marble is blue:", P_Bag2_given_Blue*100)

#------------------------------------------------------------------------------------------------

#Probability Example 4

# Probability of spam
P_Spam = 0.3

# Probability of the word "free" given spam
P_Free_given_Spam = 0.8

# Probability of the word "free" given not spam
P_Free_given_NotSpam = 0.1

# Total probability of receiving an email with the word "free"
P_Free = (P_Free_given_Spam * P_Spam) + (P_Free_given_NotSpam * (1 - P_Spam))

# Applying Bayes' Theorem
P_Spam_given_Free = (P_Free_given_Spam * P_Spam) / P_Free

print(f"Probability of an email being spam if it contains 'free': {P_Spam_given_Free:.2f}")

#------------------------------------------------------------------------------------------------

#Probability Example 5

# Probabilities
P_Box1 = 1 / 2  # Probability of picking Box 1
P_Box2 = 1 / 2  # Probability of picking Box 2
P_Car_given_Box1 = 3 / 5  # Probability of picking a car from Box 1
P_Car_given_Box2 = 1 / 4  # Probability of picking a car from Box 2

total_pro = (P_Box1*P_Car_given_Box1) + (P_Box2*P_Car_given_Box2)
probability_of_car_from_box_1 = P_Box1*P_Car_given_Box1/total_pro
probability_of_car_from_box_2 = P_Box2*P_Car_given_Box2/total_pro
print(probability_of_car_from_box_1*100)
print(probability_of_car_from_box_2*100)

#------------------------------------------------------------------------------------------------

#Percentiles, quartiles, and the interquartile range (IQR)

import numpy as np

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculate percentiles
p25 = np.percentile(data, 25)  # 25th percentile (Q1)
p50 = np.percentile(data, 50)  # 50th percentile (Q2 or median)
p75 = np.percentile(data, 75)  # 75th percentile (Q3)

# Print percentiles
print("25th percentile (Q1):", p25)
print("50th percentile (Q2 or Median):", p50)
print("75th percentile (Q3):", p75)

# Calculate IQR
IQR = p75 - p25
print("Interquartile Range (IQR):", IQR)

#------------------------------------------------------------------------------------------------

#Variance, Standard Deviation, and Standard Error (SE)

import numpy as np

# Let's say we have ages of a group of people
ages = np.array([23, 25, 22, 19, 25, 28, 23, 21, 20, 29])

# Mean (average) age
mean_age = np.mean(ages)
print(f"Mean Age: {mean_age}")

# Variance
variance = np.var(ages)
print(f"Variance: {variance}")

# Standard Deviation
std_dev = np.sqrt(variance)  # Or directly np.std(ages)
print(f"Standard Deviation: {std_dev}")

# Standard Error
# SE = standard deviation / sqrt(n)
n = len(ages)  # Number of data points

SE = std_dev / np.sqrt(n)
print(np.sqrt(n))
print(f"Standard Error: {SE}")

#------------------------------------------------------------------------------------------------

#Causality, Covariance, and Correlation

import numpy as np
import matplotlib.pyplot as plt

# Ages of children
ages = np.array([5, 6, 7, 8, 9, 10])

# Heights of children in cm
heights = np.array([110, 115, 120, 125, 130, 135])

# Let's calculate covariance
covariance_matrix = np.cov(ages, heights)
print(f"Covariance between age and height: \n{covariance_matrix}")

# Calculating correlation
correlation_matrix = np.corrcoef(ages, heights)
print(f"Correlation between age and height: \n{correlation_matrix}")

# Plotting age vs. height
plt.scatter(ages, heights)
plt.title('Age vs Height of Children')
plt.xlabel('Age (years)')
plt.ylabel('Height (cm)')
plt.show()

#------------------------------------------------------------------------------------------------

#Probability Mass Function (PMF)

import matplotlib.pyplot as plt
import pandas as pd

# Here are the numbers of friends who visited each hour
visits = [2, 3, 2, 4, 5, 2, 3, 4, 3, 2]

# Now we make a special list to remember how many times each number happened
visits_series = pd.Series(visits)

# Then we count them
visits_count = visits_series.value_counts().sort_index()

# Now, let's make our chart!
plt.bar(height=visits_series, x=['8-9', '9-10', '10-11', '11-12', '12-1', '1-2', '2-3', '3-4', '4-5', '5-6'])

# We add labels to tell everyone what our chart is about
plt.xlabel('Timing')
plt.ylabel('Number of Friends Visiting')
plt.title('My Lemonade Stand Visitors')
plt.show()

#------------------------------------------------------------------------------------------------

#Probability Density Function (PDF)

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Pretend we have a DataFrame with people's weights
weights = pd.DataFrame({
    'Weight': np.random.normal(150, 15, size=1000)  # Average weight 150, standard deviation 15
})

# We use seaborn to plot the PDF
sns.histplot(weights['Weight'], kde=True)
plt.title('PDF of People’s Weights')
plt.xlabel('Weight')
plt.ylabel('Density')
plt.show()

#------------------------------------------------------------------------------------------------

#Cumulative Distribution Function (CDF)

import pandas as pd
import numpy as np
# Again, our data
df = np.random.randint(1, 6, 5)
data = pd.Series(df)
print(f'Data: {data}')
# Get the value counts and sort the index
value_counts = data.value_counts().sort_index()
print(f'Value_Counts: {value_counts}')
# Calculate the cumulative sum of the value counts
cumulative_value_counts = value_counts.cumsum()
print(f'Cumulative_Value_Counts: {cumulative_value_counts}')
# Divide by the total number of data points to get the CDF
cdf = cumulative_value_counts / len(data)*100
print(cdf)

#------------------------------------------------------------------------------------------------

#Cumulative Distribution Function (CDF) Example 2

# Generate random delivery times (exponential distribution)
delivery_times = np.random.exponential(scale=1, size=1000)

# Plotting CDF
plt.hist(delivery_times, bins=30, density=True, cumulative=True, alpha=0.6, color='b')
plt.xlabel('Delivery Time')
plt.ylabel('Cumulative Probability')
plt.title('CDF of Delivery Times')
plt.show()

#------------------------------------------------------------------------------------------------

#Continuous Probability Distribution
#Uniform Distribution Example 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create 1000 numbers between 0 and 10
uniform_data = np.random.uniform(0, 10, 1000)

# Turn our NumPy array into a Pandas DataFrame
df = pd.DataFrame(uniform_data, columns=['UniformData'])

# Let's see the first few rows
print(df)

# Plot a histogram of the uniform data
df['UniformData'].hist(bins=50)
plt.title('Uniform Distribution Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#------------------------------------------------------------------------------------------------

#Uniform Distribution Example 2

# Simulate rolling a fair six-sided die 1000 times
die_roll_results = np.random.randint(low=1, high=7, size=1000)

# Plot a histogram to visualize the distribution of die roll results
plt.hist(die_roll_results, bins=np.arange(0.5, 7.5, 1), align='mid', rwidth=0.8)
plt.title("Uniform Distribution of Die Roll Results")
plt.xlabel("Result")
plt.ylabel("Frequency")
plt.xticks(range(1, 7))
plt.show()

#------------------------------------------------------------------------------------------------

#Uniform Distribution Example 3

# Simulate sales quantities for different products with equal likelihood
num_products = 10
sales_quantities = np.random.randint(50, 100, size=num_products)
print(sales_quantities)
# Simulate sales prices for each product from a uniform distribution
sales_prices = np.random.uniform(10, 50, size=num_products)
print(sales_prices)
# Analyze revenue forecasts based on simulated sales data

#------------------------------------------------------------------------------------------------

#Normal/Gaussian Distribution

import numpy as np
import matplotlib.pyplot as plt

# Generate random data with a Normal distribution
mu, sigma = 0, 1 # mean and standard deviation
data = np.random.normal(mu, sigma, 1000)

# Plot the histogram
plt.hist(data, bins=30, density=True, alpha=0.6, color='r')
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#------------------------------------------------------------------------------------------------

#Exponential Distribution Example 1

import numpy as np
import matplotlib.pyplot as plt

# Simulate time between customer arrivals (exponential distribution)
average_arrival_time = 5  # Average time between arrivals (minutes)
num_arrivals = 1000
interarrival_times = np.random.exponential(scale=average_arrival_time, size=num_arrivals)

# Plot histogram of interarrival times
plt.hist(interarrival_times, bins=30, density=True, alpha=0.6, color='g')
plt.xlabel('Time between arrivals (minutes)')
plt.ylabel('Probability density')
plt.title('Interarrival Time Distribution')
plt.grid(True)
plt.show()

#------------------------------------------------------------------------------------------------

#Exponential Distribution Example 2

# Simulate time between page views (exponential distribution)
average_time_between_views = 10  # Average time between views (seconds)
num_views = 1000
interarrival_times = np.random.exponential(scale=average_time_between_views, size=num_views)

# Plot histogram of interarrival times
plt.hist(interarrival_times, bins=30, density=True, alpha=0.6, color='r')
plt.xlabel('Time between page views (seconds)')
plt.ylabel('Probability density')
plt.title('Interarrival Time between Page Views')
plt.grid(True)
plt.show()
