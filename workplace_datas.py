import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sqlite3
from datetime import datetime
import pytz
#from icecream import ic as print

def connection(connect):
    edit = connect.cursor()

    #edit.execute('''CREATE TABLE data(age INTEGER, size INTEGER, temperature INTEGER, 
    #             Price INTEGER)''')
    #connect.executemany('INSERT INTO data(age) VALUES (?)', data())
    #update = [(12, 16), ]
    #edit.executemany('''UPDATE data 
    #                SET age = ?
    #                WHERE age == ? ''', update)
    #connect.commit()
    read  = pd.read_sql('SELECT * FROM data', connect)
    connect.close()
    return read

def data():
    sample_data = [(12, 24, 51, 105),
                   (17, 27, 60, 160),
                   (19, 30, 65, 200),
                   (20, 32, 67, 230),
                   (25, 40, 65, 300)]
    
    return sample_data

def main():
    timezone = pytz.timezone('Asia/Manila')
    time = datetime.now(timezone).strftime('%d-%m-%Y %H:%M')

    set = sqlite3.connect('sample.db')
    df = connection(set)

    #creating a Independent_var and Dependent_var
    Independent_var = df[['temperature']] #independent Variable
    Dependent_var = df.iloc[:, -1]

    variables = [Independent_var, Dependent_var]

    #Creating Train and Test set
    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependent_var, test_size=0.25, random_state=42)
    
    model = LinearRegression().fit(X_train, y_train)
    prediction = model.predict(X_test)

    accuracy = {
        "prediction": prediction,
        "y_test": y_test, 
        "error": abs(prediction - y_test),
        "MAE": mean_absolute_error(y_test, prediction)
    }

    print(accuracy)

    plt.style.use('dark_background')
    fig = plt.figure()

    for i, data in enumerate(variables, start=1):
        if i == 1:
            plt.subplot(1, 2, i)
            plt.title('Test prediction')
            plt.xlabel('Temperature')
            plt.ylabel('Price')
            plt.grid(alpha=0.4)
            plt.scatter(X_test, y_test, marker='x', color='blue', label='Actual Data')
            plt.plot(X_test, prediction, color='red', label='Prediction')


        elif i == 2:
            plt.subplot(1, 2, i)
            plt.title('Perfect Prediction')
            plt.xlabel('Price')
            plt.ylabel('Price')
            plt.grid(alpha=0.4)
            plt.scatter(y_test, prediction, marker='o', color='green', label='Accuracy')
            plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='violet', label='Perfect Line')
        plt.legend()
    
    fig.text(0.99, 0.01, time, color='gray', fontsize=8, ha='right', va='bottom')
    plt.tight_layout()
    plt.savefig('workplace_datas.png')
    plt.show()
    print('The Program is executed Successfully')
    print(f'Predictions are {prediction}')
    print(df)

if __name__ == '__main__':
    main()