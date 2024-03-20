import pandas as pd
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm

# Read the spreadsheet into a pandas DataFrame
df = pd.read_excel('your_spreadsheet.xlsx')

# Select the relevant columns for the regression
X = df[['Year', 'Month', 'Dom_Pax', 'Dom_Flt', 'Dom_RPM', 'Dom_ASM']]
y = df['Dom_LF']

# Fit the multiple regression model
model = LinearRegression()
model.fit(X, y)

# Print the regression statistics
X = sm.add_constant(X)  # Add a constant term for the intercept
regression_model = sm.OLS(y, X)
results = regression_model.fit()
print(results.summary())

# Predict the Dom_LF for the nine months of 2023
new_data = pd.DataFrame({
    'Year': [2023] * 9,
    'Month': range(1, 10),
    'Dom_Pax': [0] * 9,  # Replace with your actual data
    'Dom_Flt': [0] * 9,  # Replace with your actual data
    'Dom_RPM': [0] * 9,  # Replace with your actual data
    'Dom_ASM': [0] * 9   # Replace with your actual data
})
predictions = model.predict(new_data)

# Calculate and print the percentage difference between actual and predicted Dom_LF
actual_dom_lf = [0] * 9  # Replace with your actual data
percentage_difference = [(actual - predicted) / actual * 100 for actual, predicted in zip(actual_dom_lf, predictions)]
for month, difference in zip(range(1, 10), percentage_difference):
    print(f"Month {month}: {difference}% difference")