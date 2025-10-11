from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

def get_mae(max_leaf_nodes, X_train, X_test, y_train, y_test):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    mae = mean_absolute_error(y_test, prediction)
    return mae

def main():
    data = pd.read_csv("Salary_dataset.csv") #Load Dataset

    X = data.drop(["Salary"], axis=1)
    y = data.Salary

    #Split the given dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    for leaf_node in [5, 50, 500, 5000]:
        mae = get_mae(leaf_node, X_train, X_test, y_train, y_test)

        print(f"max_leaf_node: {leaf_node} MAE: {mae}")

if __name__ == "__main__":
    main()
