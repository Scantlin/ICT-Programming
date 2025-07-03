from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error #For the readings of predictions
from sklearn.preprocessing import OneHotEncoder, StandardScaler #For categories 
from sklearn.model_selection import train_test_split #For spliting the dataset
from sklearn.linear_model import LinearRegression, RidgeCV #For Linear Regression
from sklearn.ensemble import RandomForestRegressor
import numpy as np #For performing operations on to the data
import pandas as pd #for readings of data from CSV files
import matplotlib.pyplot as plt #For visualization
import sqlite3 #For connection of Datavase 

def main():
    datas = pd.read_csv('Salary_dataset.csv')

    #datas = datas.dropna() #Handles missing values

    #Assign which is independent and Dependent 
    #Independent_Var = datas.iloc[:, :-1].values
    #Dependent_Var = datas.iloc[:, -1].values

    Independent_Var = datas[['YearsExperience']]
    Dependent_Var = datas['Salary']
    ''''
    plt.style.use('dark_background')
    plt.figure(figsize=(7, 5))
    plt.scatter(Independent_Var, Dependent_Var, color='blue')
    plt.title('Experience Vs Salary')
    plt.xlabel('Years of experience')
    plt.ylabel('Salary')
    plt.savefig('TEST_L.png')
    plt.show()'''

    #Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(Independent_Var, Dependent_Var, test_size=0.2, random_state=42)

    #Scale the Independent Variable
    x_scaler = StandardScaler()
    x_train_scaled = x_scaler.fit_transform(X_train)
    x_test_scaled = x_scaler.transform(X_test)

    #Model
    #model = LinearRegression().fit(x_train_scaled, y_train)
    model = RandomForestRegressor().fit(x_train_scaled, y_train)
    #model = RidgeCV(alphas=[0.01, 0.1, 1, 10, 100], cv=5).fit(x_train_scaled, y_train)

    y_pred_train = model.predict(x_train_scaled)
    y_pred_test = model.predict(x_test_scaled)

    print(f'TRAIN MAE {mean_absolute_error(y_train, y_pred_train):.2f} TEST MAE {mean_absolute_error(y_test, y_pred_test):.2f}')
    print(f'TRAIN MSE: {mean_squared_error(y_train, y_pred_train):.2f} R2 Score: {r2_score(y_train, y_pred_train):.2f}')
    print(f'TEST MSE: {mean_squared_error(y_test, y_pred_test):.2f} R2 Score: {r2_score(y_test, y_pred_test):.2f}')

    #Visualizing the Datas
    '''plt.scatter(y_pred_test, y_test - y_pred_test, alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.xlabel("Predicted Salary")
    plt.ylabel("Residuals (Actual - Predicted)")
    plt.title("Residual Analysis")
    plt.legend()
    plt.savefig('TEST_L.png')
    plt.show()'''



if __name__ == '__main__':
    main()