
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Sample DataFrame creation (replace this with actual data loading and preprocessing)
data = pd.DataFrame({
    'Region': ['Region1', 'Region2', 'Region3', 'Region1', 'Region2'],
    'SeatingCapacity': [50, 100, 150, 200, 250],
    'BusinessType': ['Type1', 'Type2', 'Type1', 'Type3', 'Type2'],
    'ActualSales': [40000000, 60000000, 80000000, 50000000, 70000000]
})

# User input for target sales (e.g., 50000000 won)
user_target_sales = 50000000

# Creating a binary target variable based on user's target sales
data['TargetAchieved'] = (data['ActualSales'] >= user_target_sales).astype(int)

# Selecting features and target
features = data[['Region', 'SeatingCapacity', 'BusinessType']]
target = data['TargetAchieved']

# Encoding categorical variables
features = pd.get_dummies(features)

# Splitting the dataset into training and testing sets
X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(features, target, test_size=0.2, random_state=42)

# Initializing and training the RandomForestClassifier
model_rf = RandomForestClassifier(random_state=42)
model_rf.fit(X_train_rf, y_train_rf)

# Predicting probabilities for the test set
probabilities = model_rf.predict_proba(X_test_rf)[:, 1]

# Calculating the average probability of achieving the target sales
average_probability = probabilities.mean()

print("Average probability of achieving the target sales:", average_probability)

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

# Function to make predictions based on user input
def predict_success(location, seating_capacity, business_type):
    input_features = np.array([[location, seating_capacity, business_type]])
    predicted_success = model.predict(input_features)
    return predicted_success[0]

# Example Usage
predicted_success = predict_success(1, 50, 2)
print(f'Predicted Success Metric: {predicted_success}')

# Calculate Mean Squared Error (MSE) and R-squared (R²)

print("Mean Squared Error (MSE):", mse)
print("R-squared (R²):", r2)
