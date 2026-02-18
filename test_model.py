import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import os

# Load the data
df = pd.read_csv('Housing_Price.csv')
print('Data shape:', df.shape)
print('First 10 rows:')
print(df.head(10))
print('Size range:', df['Size'].min(), 'to', df['Size'].max())
print('Price range:', df['Price'].min(), 'to', df['Price'].max())
print('Correlation between Size and Price:', df['Size'].corr(df['Price']))

# Load the trained model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Test the model with some sample data points from the dataset
sample_data = df.sample(n=5, random_state=42)
print("\nTesting model with sample data points:")
print("Size\tActual Price\tPredicted Price")

for index, row in sample_data.iterrows():
    size = row['Size']
    actual_price = row['Price']
    predicted_price = model.predict([[size]])[0]
    print(f"{size}\t{actual_price}\t\t{predicted_price:.2f}")

# Calculate overall model performance
X = df[['Size']]
y = df['Price']
y_pred = model.predict(X)

mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"\nModel Performance:")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R² Score: {r2:.4f}")

# Test with a few specific values
print("\nTesting with specific house sizes:")
test_sizes = [1000, 2000, 3000, 4000, 5000]
for size in test_sizes:
    predicted_price = model.predict([[size]])[0]
    # Convert to Rupees (using the same conversion rate as in app.py)
    price_inr = predicted_price * 83.0
    print(f"House size {size} sq ft -> ${predicted_price:.2f} -> ₹{price_inr:,.2f}")