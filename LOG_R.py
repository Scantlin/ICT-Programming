from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as numpy
import pandas as pd
import matplotlib.pyplot as pyplot
from datetime import datetime
import pytz

def main():
    Time_zone = pytz.timezone('Asia/Manila')
    time = datetime.now(Time_zone).strftime('%d-%m-%y %H:%M')
    data = {
        "Number of sleep": [6, 5, 8, 9, 3, 4, 2, 2, 1, 7],
        "Hours of Review": [3, 4, 2, 1, 6, 5, 7, 7, 8, 3],
        "Result": [1, 1, 0, 0, 1, 1, 1, 0, 0, 1] #1 Passed 0 Failed
    }

    dataframe = pd.DataFrame(data)

    Independent_var = dataframe.iloc[:, :-1]
    Depedendent_var = dataframe.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Depedendent_var, test_size=0.2, random_state=42)

    sample = {
        "Number of sleep": [1, 7, 0],
        "Hours of Review": [11, 2, 9]
    }

    sample_df = pd.DataFrame(sample)
    sample = sample_df[["Number of sleep", "Hours of Review"]]

    #model = LogisticRegression().fit(X_train, y_train)
    model = RandomForestClassifier(criterion='gini', random_state=42).fit(X_train, y_train)
    sample_prediction = model.predict(sample)

    print(sample_prediction)

    for i, order in enumerate (sample_prediction):
        if order == 1:
            print(f'number of sleep is {sample["Number of sleep"][i]}, Hours Review is {sample["Hours of Review"][i]}, result: Passed')
        elif order == 0:
            print(f'number of sleep is {sample["Number of sleep"][i]}, Hours Review is {sample["Hours of Review"][i]}, result: Failed')
        else:
            print('Error')


if __name__ == '__main__':
    main()