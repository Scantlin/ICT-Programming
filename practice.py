import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
import pytz

def main():
    time_zone = pytz.timezone('Asia/Manila')
    time = datetime.now(time_zone).strftime('%d-%m-%y %H:%M')

    data = {
        "feature1": [2.5, 4.1, 3.2, 5.0, 1.8, 3.6, 4.8, 2.0, 5.5, 1.5],
        "feature2": [3.5, 2.2, 4.6, 1.5, 5.0, 2.8, 3.0, 4.2, 2.0, 6.0],
        "feature3": [1.8, 3.0, 2.5, 4.2, 0.9, 3.5, 2.0, 1.5, 5.0, 0.5],
        "target": [12.1, 15.3, 18.7, 20.5, 9.8, 17.2, 22.0, 13.5, 25.1, 8.3]
    }

    Independent_var = ['feature1', 'feature2', 'feature3']
    Dependent_var = 'target'

    plt.figure(figsize=(15, 5))

    for i, feature in enumerate(Independent_var, 1):
        Xdata = np.array(data[feature]).reshape(-1, 1)
        ydata = np.array(data[Dependent_var]) 

        model = LinearRegression().fit(Xdata, ydata)

        plt.subplot(1, 3, i)
        plt.scatter(Xdata, ydata, color='blue', label='Actual Data') #Actual Data
        plt.plot(Xdata, model.predict(Xdata), color='brown', label='Xdata vs prediction')
        #plt.scatter(ydata, model.predict(Xdata), color='orange', alpha=0.7, label='data') #visualize actual data of Y and predicted data of Y
        #plt.plot([ydata.min(), ydata.max()], [ydata.min(), ydata.max()], '--r' ,label='Prediction') #for perfect prediction
        plt.title(f'{feature} vs Target')
        plt.xlabel('Features')
        plt.ylabel('Target')
        plt.legend()
        
    #plt.tight_layout()
    plt.savefig('practice.png')
    plt.show()


if __name__ == '__main__':
    main()