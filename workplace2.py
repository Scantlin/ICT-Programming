import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

def main():
    data = pd.read_csv('Salary_dataset.csv')
    X = data[['YearsExperience']]
    y = data['Salary']

    #Split Dataset into Train and Test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    
    #Create a model
    model = LinearRegression().fit(X_train, y_train)

    y_pred_train = model.predict(X_train) #Prediction for Y train, or the dataset that we have
    y_pred_test = model.predict(X_test)

    error = {
        'Y test': y_test,
        'Y Prediction Test': y_pred_test,
        'Error': y_test-y_pred_test
    }
    print(error)

    Train_MAE = mean_absolute_error(y_train, y_pred_train)
    r2_train = r2_score(y_train, y_pred_train)

    Test_MAE = mean_absolute_error(y_test, y_pred_test)
    r2_test = r2_score(y_test, y_pred_test)

    print(f'TRAIN MAE: {Train_MAE:.2f} R2_TRAIN: {r2_train:.2f}')
    print(f'TEST MAE : {Test_MAE:.2f} R2_TEST: {r2_test:.2f}')

if __name__ == '__main__':
    main()