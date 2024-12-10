from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Sample Data
X = np.array([[10, 3, 0.5], [20, 5, 0.6], [30, 2, 0.7]])  # [vehicle_count, time_of_day, air_quality]
y = np.array([15, 25, 35])  # Predicted green signal duration

# Train the model
model = RandomForestRegressor()
model.fit(X, y)

# Predict
new_data = np.array([[25, 4, 0.55]])  # Example input
predicted_time = model.predict(new_data)
print(f"Predicted Green Signal Time: {predicted_time[0]} seconds")
