import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

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
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initializing and training the RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predicting probabilities for the test set
probabilities = model.predict_proba(X_test)[:, 1]

# Calculating the average probability of achieving the target sales
average_probability = probabilities.mean()

print("Average probability of achieving the target sales:", average_probability)
