import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

import warnings

def main():
    #Data
    try:
        warnings.filterwarnings("ignore")
        Data = {
            "Size": [1500, 2000, 1200, 1800, 2200, 1600, 1900, 2100, 1300, 1700],
            "Bedrooms": [2, 3, 2, 3, 4, 3, 3, 4, 2, 3],
            "Neighborhood": ["Suburban", "Urban", "Rural", "Suburban", "Urban", "Rural", "Urban", "Suburban", "Rural", "Urban"],
            "Price": [250000, 350000, 180000, 300000, 400000, 220000, 320000, 380000, 190000, 310000]
        }

        dataframe = pd.DataFrame(Data)

        #dataframe = pd.get_dummies(dataframe, columns=["Colors"], drop_first=False)
        #print(dataframe)

        #SPLIT THE DATA
        X = dataframe[["Size", "Bedrooms", "Neighborhood"]]
        y = dataframe["Price"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        #TRANSFORM the X_TRAIN AND TEST SINCE IT HAS CATEGORY
        preprocessor = ColumnTransformer(transformers=[("neighborhood", OneHotEncoder(drop="first"), ["Neighborhood"])], remainder='passthrough')
        X_train_encoded = preprocessor.fit_transform(X_train)
        X_test_encoded = preprocessor.transform(X_test)

        model = LinearRegression().fit(X_train_encoded, y_train)

        y_pred_train = model.predict(X_train_encoded) #Actual Data
        y_pred_test = model.predict(X_test_encoded)

        print(f'XTrain are {X_train_encoded} \nXTest are {X_test_encoded}')
        print(f'yTrain are {y_pred_train} \nyTest {y_pred_test}')

        #MSE
        Train_mse = mean_squared_error(y_train, y_pred_train)
        Test_mse = mean_squared_error(y_test, y_pred_test)

        #R2
        Train_R2 = r2_score(y_train, y_pred_train)
        Test_R2 = r2_score(y_test, y_pred_test)

        print(f'TRAIN: MSE {Train_mse:.2f} R2 {Train_R2:.2f}')
        print(f'TEST: MSE {Test_mse:.2f} R2 {Test_R2:.2f}')
        #print(f'Coef_ {dict(zip(X.columns, model.coef_))}' )

    except Exception as e:
        print(e)
        raise
    
    finally:
        print('Thank you for using the program')

if __name__ == '__main__':
    main()