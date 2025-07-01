import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

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
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        Categorical_var = dataframe.select_dtypes(include=['object']).columns.tolist()

        #TRANSFORM the X_TRAIN AND TEST SINCE IT HAS CATEGORY
        encoder = ColumnTransformer(transformers=[('categorical', OneHotEncoder(), Categorical_var)], remainder='passthrough')
        X_train_encoded = encoder.fit_transform(X_train)
        X_test_encoded = encoder.transform(X_test)

        model = LinearRegression().fit(X_train_encoded, y_train)

        y_pred_test = model.predict(X_test_encoded)

        #MSE
        Test_mse = mean_absolute_error(y_test, y_pred_test)

        #R2
        Test_r2 = r2_score(y_test, y_pred_test)

        print(round(Test_mse, 2))
        print(round(Test_r2*100, 2))


    except Exception as e:
        print(e)
        raise
    
    finally:
        print('Thank you for using the program')

if __name__ == '__main__':
    main()