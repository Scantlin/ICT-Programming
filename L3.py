import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Data preparation
    X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Independent Variable
    y = np.array([2, 4, 5, 4, 5, 7, 8, 9, 10, 10])  # Dependent Variable
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # Model training
    model = LinearRegression().fit(X_train, y_train)
    
    # Predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Error metrics
    train_mse = mean_squared_error(y_train, y_pred_train)
    test_mse = mean_squared_error(y_test, y_pred_test)
    train_r2 = r2_score(y_train, y_pred_train)
    test_r2 = r2_score(y_test, y_pred_test)
    
    print(f"Training MSE: {train_mse:.2f}, R²: {train_r2:.2f}")
    print(f"Testing MSE: {test_mse:.2f}, R²: {test_r2:.2f}")
    
    # Plotting with Matplotlib
    plt.style.use('dark_background')
    plt.figure(figsize=(14, 6))
    
    # Plot 1: Regression fit
    plt.subplot(1, 2, 1)
    # Training data and regression line
    plt.scatter(X_train, y_train, color='cyan', label='Train Data')
    plt.plot(X_train, y_pred_train, color='violet', 
             label=f'Regression Line\nSlope: {model.coef_[0]:.2f}')
    # Test data
    plt.scatter(X_test, y_test, color='red', label='Test Data')
    plt.title('Regression Fit')
    plt.xlabel('Independent')
    plt.ylabel('Dependent')
    plt.legend()
    
    # Plot 2: Actual vs Predicted with error metrics
    plt.subplot(1, 2, 2)
    max_val = max(max(y), max(y_pred_train), max(y_pred_test))
    min_val = min(min(y), min(y_pred_train), min(y_pred_test))
    
    plt.scatter(y_train, y_pred_train, color='cyan', label='Train Predictions')
    plt.scatter(y_test, y_pred_test, color='red', label='Test Predictions')
    plt.plot([min_val, max_val], [min_val, max_val], color='yellow', 
             linestyle='--', label='Perfect Prediction')
    
    plt.title(f'Actual vs Predicted\nTrain MSE: {train_mse:.2f}, Test MSE: {test_mse:.2f}')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('L3_with_metrics.png')
    plt.show()

if __name__ == '__main__':
    main()