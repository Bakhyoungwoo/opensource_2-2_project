import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate a simulated dataset
np.random.seed(0)
n_samples = 100

# Features: Location, Seating Capacity, Business Type
X = np.column_stack((
    np.random.randint(0, 3, n_samples),  # Location (encoded as 0, 1, 2)
    np.random.randint(20, 100, n_samples),  # Seating Capacity
    np.random.randint(0, 3, n_samples)  # Business Type (encoded as 0, 1, 2)
))

# Target: A success metric (like revenue)
y = X[:, 1] * np.random.uniform(0.5, 1.5, n_samples) + \
    X[:, 0] * np.random.uniform(-20, 20, n_samples) + \
    X[:, 2] * np.random.uniform(-10, 10, n_samples)

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Function to make predictions based on user input
def predict_success(location, seating_capacity, business_type):
    input_features = np.array([[location, seating_capacity, business_type]])
    predicted_success = model.predict(input_features)
    return predicted_success[0]

# Example Usage
predicted_success = predict_success(1, 50, 2)
print(f'Predicted Success Metric: {predicted_success}')
