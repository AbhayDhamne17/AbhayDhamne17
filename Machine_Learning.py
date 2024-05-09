#Linear Regression Single Variable Example 1

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Example dataset
data = {
    'Advertising_Spend': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
    'Sales': [120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200]
}
df = pd.DataFrame(data)
print(df)

plt.scatter(df['Advertising_Spend'], df['Sales'])
plt.title('Advertising Spend vs. Sales')
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Sales ($)')
plt.show()

X = df[['Advertising_Spend']]  # Features
y = df['Sales']  # Labels

# Splitting dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Actual Sales vs Predicted Sales")
for actual, predicted in zip(y_test, predictions):
    print(f"${actual} vs ${predicted:.2f}")
    
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='green', label='Testing data')
plt.plot(X_train, model.predict(X_train), color='red', linewidth=2, label='Linear regression')
plt.title('Advertising Spend vs. Sales')
plt.xlabel('Advertising Spend ($)')
plt.ylabel('Sales ($)')
plt.legend()
plt.show()

#------------------------------------------------------------------------------------------------

#Linear Regression Single Variable Example 2

data = {'Investment' : [14, 94, 30, 82, 75, 41, 28, 31, 99, 25],
'Sales' : [24, 104, 40,  92, 85, 51,  38,  41, 109,  35]}

df = pd.DataFrame(data)
print(df)
sns.lmplot(x='Investment', y='Sales', data=df)

X_train, X_test, y_train, y_test = train_test_split(df[['Investment']], df['Sales'], random_state=42, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)
plt.scatter(X_train, y_train)
new_data = pd.DataFrame({'Investment': [10000]})
predicted_sales = model.predict(new_data)
print("Predicted Sales for Next Quarter:", predicted_sales)

#------------------------------------------------------------------------------------------------

#Linear Regression with Multiple Variables

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {'Age': [25, 30, 35, 40, 45], 'Height': [162.56, 172.72, 167.64, 165.10, 157.48], 'Weight': [70, 95, 78, 110, 85], 'Premium': [18000, 38000, 38000, 60000, 70000]}

df = pd.DataFrame(data)
print(df)

model = LinearRegression()
model.fit(df[['Age', 'Height', 'Weight']], df['Premium'])

model.predict([[50, 165, 55]])

#------------------------------------------------------------------------------------------------

#Polynomial Regression

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {'Position': ['Business Analyst', 'Junior Consultant', 'Senior Consultant', 'Manager', 'Country Manager', 'Region Manager', 'Partner', 'Senior Partner', 'C-Level', 'CEO'],
        'Level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Salary': [45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]}

df = pd.DataFrame(data)

# Independent and dependent variables
X = df[['Level']]
y = df['Salary']

# Polynomial Features
poly = PolynomialFeatures(degree=4)  # Adjusting degree to better fit the data
X_poly = poly.fit_transform(X)

# Linear Regression
reg = LinearRegression()
reg.fit(X_poly, y)

# Predicting a new result with Polynomial Regression
level_value = 6.5
prediction = reg.predict(poly.transform([[level_value]]))

# Plotting
plt.scatter(X, y, color='red')
plt.plot(X, reg.predict(X_poly), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Displaying the prediction
prediction

#------------------------------------------------------------------------------------------------

#Logistic Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = {'Age': [21, 45, 32, 41, 20, 35, 20, 23, 42, 34, 24, 22, 23, 25, 43, 44, 25, 30, 31], 'Bought_Insurance': ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes']}

df = pd.DataFrame(data)

# It's better to convert 'Yes' and 'No' to 1 and 0 using astype for model compatibility
df['Bought_Insurance'] = df['Bought_Insurance'].map({'Yes': 1, 'No': 0})

X_train, X_test, Y_train, Y_test = train_test_split(df[['Age']], df['Bought_Insurance'], test_size=0.2, random_state=42)

log = LogisticRegression()
log.fit(X_train, Y_train)

# Predicting the test set results
predictions = log.predict(X_test)

# Calculating the model accuracy
score = log.score(X_test, Y_test)

# Displaying predictions and model accuracy
print(predictions)
print(score)
