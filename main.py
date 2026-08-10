#!/usr/bin/env python3
"""
Simple Machine Learning Demonstration: Linear Regression Model
"""

import numpy as np
from sklearn.linear_model import LinearRegression


def train_and_predict():
    # 1. Prepare Training Data (Feature: X, Target: y)
    # Example: X represents input features (e.g., house size in hundreds of sq ft)
    # y represents target values (e.g., price in tens of thousands)
    X = np.array([[1], [2], [3], [4], [5]], dtype=float)
    y = np.array([150, 200, 250, 300, 350], dtype=float)

    # 2. Instantiate and Train the Machine Learning Model
    model = LinearRegression()
    model.fit(X, y)

    # 3. Make a Prediction on Unseen Data
    new_input = np.array([[6]], dtype=float)
    prediction = model.predict(new_input)

    print("=== Machine Learning Model Output ===")
    print(f"Learned Slope (Weight): {model.coef_[0]:.2f}")
    print(f"Learned Intercept (Bias): {model.intercept_:.2f}")
    print(f"Prediction for input X=6: {prediction[0]:.2f}")


if __name__ == "__main__":
    train_and_predict()
