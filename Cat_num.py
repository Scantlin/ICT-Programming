from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import pandas as pd

def main():
    data = {
    'Size': [5, 7, 10, 12, 15, 8, 10, 20, 12, 18, 6, 9, 11, 14, 16, 4, 7, 13, 17, 19, 5, 8, 10, 15, 20, 10, 12, 14, 16, 18],
    'Colors': ['red', 'Blue', 'Yellow', 'Green', 'Violet', 'red', 'Blue', 'Yellow', 'Green', 'Violet', 
              'red', 'Blue', 'Yellow', 'Green', 'Violet', 'red', 'Blue', 'Yellow', 'Green', 'Violet',
              'red', 'Blue', 'Yellow', 'Green', 'Violet', 'red', 'Blue', 'Yellow', 'Green', 'Violet'],
    'Price': [120, 220, 320, 420, 500, 130, 230, 350, 450, 510, 
              110, 210, 310, 410, 490, 100, 200, 300, 400, 480,
              125, 225, 325, 425, 505, 135, 235, 355, 455, 515]
}

    dataframe = pd.DataFrame(data)

    X = dataframe[['Size', 'Colors']]
    y = dataframe['Price']

    #Split Data
    X_Train, X_Test, y_Train, y_Test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Variable = ColumnTransformer(transformers=[('new name', OneHotEncoder(drop='first', handle_unknown='ignore'), ['name of the column that has category'])], remainder='passthrough')
    preprocessing = ColumnTransformer(
        transformers=[('colors', OneHotEncoder(drop='first', handle_unknown='ignore'), ['Colors'])], 
        remainder='passthrough')

    X_Train_encoded = preprocessing.fit_transform(X_Train)
    X_Test_encoded = preprocessing.transform(X_Test)

    model = LinearRegression().fit(X_Train_encoded, y_Train)

    y_pred_train = model.predict(X_Train_encoded)
    y_pred_test = model.predict(X_Test_encoded)

    Train_MSE = mean_squared_error(y_Train, y_pred_train)
    Test_MSE = mean_squared_error(y_Test, y_pred_test)

    Train_r2 = r2_score(y_Train, y_pred_train)
    Test_r2 = r2_score(y_Test, y_pred_test)

    test_results = pd.DataFrame({
        'Actual': y_Test,
        'Predicted': y_pred_test,
        'Error': y_Test - y_pred_test
    })

    print(test_results)

    print(f'TRAIN AND TEST MAE {mean_absolute_error(y_Train, y_pred_train)} {mean_absolute_error(y_Test, y_pred_test)}')
    print(f'TRAIN MSE: {Train_MSE:.2f} TRAIN R2: {Train_r2:.2f}')
    print(f'TEST MSE: {Test_MSE:.2f} TEST R2: {Test_r2:.2f}')

if __name__ == '__main__':
    main()