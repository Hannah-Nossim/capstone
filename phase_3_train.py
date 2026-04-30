"""
train.py
Creates scatter plot, trains LinearRegression model, evaluates it,
predicts a value, and saves the model + chart.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib
import os

# data
study_hours = np.array([2, 3, 4, 5, 6, 7, 8, 3, 5, 6, 7, 4, 8, 2, 5])
exam_scores = np.array([55, 61, 66, 72, 79, 83, 91, 58, 74, 80, 88, 70, 95, 50, 77])

# reshape for sklearn
X = study_hours.reshape(-1, 1)
y = exam_scores

# pass/fail coloring
colors = np.where(y >= 70, "green", "red")

# scatter plot
passed = y >= 70
plt.scatter(X[passed],  y[passed],  color="green", label="Passed", s=70)
plt.scatter(X[~passed], y[~passed], color="red",   label="Failed", s=70, marker="x")
# model
model = LinearRegression()
model.fit(X, y)

# R² score
r2 = model.score(X, y)
print(f"R² Score: {r2:.4f}")

# prediction for 6 hours
pred_6 = model.predict([[6]])[0]
print(f"Predicted score for 6 hours: {pred_6:.2f}")

# regression line
x_line = np.linspace(min(X), max(X), 100).reshape(-1, 1)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, label="Regression Line")

# labels
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.legend()

# save chart
os.makedirs("../charts", exist_ok=True)
plt.savefig("../charts/scatter.png")

# save model
os.makedirs("../models", exist_ok=True)
joblib.dump(model, "../models/score_model.pkl")

plt.show()
