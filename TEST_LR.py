import pandas as pd
from sklearn.tree import DecisionTreeRegressor

def main():
    print(data2)
    data = pd.read_csv('Salary_dataset.csv')
    data = data.dropna(axis=0) #Drop null Value

    X = data.drop(['Salary'], axis=1)
    y = data.Salary

    Model = DecisionTreeRegressor(random_state=1)

    Model.fit(X, y)
    print("Making prediction for 5 Man")
    print(X.head())

    print("Predictions")
    print(Model.predict(X.head()))
    
if __name__ == '__main__':
    main()