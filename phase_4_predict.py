"""
predict.py
Loads trained model and makes predictions.
"""

import joblib
import numpy as np

# load model
model = joblib.load("../models/score_model.pkl")

# inputs
hours = np.array([1, 4, 9]).reshape(-1, 1)

# predictions
predictions = model.predict(hours)

for h, p in zip(hours.flatten(), predictions):
    print(f"{h} hours -> {p:.2f}")
