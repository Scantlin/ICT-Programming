from sklearn.linear_model import LogisticRegression
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
        "Hours of Review": [3, 4, 2, 1, 6, 5, 7, 7, 8, 2],
        "Result": [1, 1, 0, 0, 1, 1, 1, 1, 1, 0] #1 Passed 0 Failed
    }

    dataframe = pd.DataFrame(data)

    Independent_var = dataframe[["Number of sleep", "Hours of Review"]]
    Dependent_var = dataframe["Result"]

    sample = {
        "Number of sleep": [10, 7, 0],
        "Hours of Review": [0, 2, 9]
    }

    sample = pd.DataFrame(sample)
    sample = sample[["Number of sleep", "Hours of Review"]]

    model = LogisticRegression().fit(Independent_var, Dependent_var)
    prediction = model.predict(sample)
    interpretation = []

    for i in range(len(prediction)):
        if prediction[i] == 1:
            interpretation.append('Passed')
        else:
            interpretation.append('Failed')

    for i in range(len(interpretation)):
        print(f'Number of sleep: {sample["Number of sleep"][i]} Hours of review: {sample["Hours of Review"][i]} result: {interpretation[i]}')
        
    print(time)

if __name__ == '__main__':
    main()