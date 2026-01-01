from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def main():
    # Generate sample data
    Data = pd.read_csv('Salary_dataset.csv')

    X = Data[['YearsExperience']]
    y = Data['Salary']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Train a decision tree (to find splits)
    tree = DecisionTreeRegressor(max_depth=3)
    tree.fit(X_train, y_train)

    # Get leaf indices for training data
    leaf_ids = tree.apply(X_train)

    # Fit linear regression in each leaf
    linear_models = {}
    for leaf in np.unique(leaf_ids):
        mask = (leaf_ids == leaf)
        lm = LinearRegression().fit(X_train[mask], y_train[mask])
        linear_models[leaf] = lm

    # Predict
    test_leaf_ids = tree.apply(X_test)
    y_pred = np.array([linear_models[leaf].predict(X_test[i:i+1])[0] 
                       for i, leaf in enumerate(test_leaf_ids)])

    # Compare with pure decision tree
    pure_tree_pred = tree.predict(X_test)
    print("Linear Tree MSE:", np.mean((y_pred - y_test)**2))
    print("Pure Tree MSE:", np.mean((pure_tree_pred - y_test)**2))

if __name__ == '__main__':
    main()