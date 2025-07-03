import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime
import pytz

def main():
    time_zone = pytz.timezone('Asia/Manila')
    time = datetime.now(time_zone).strftime('%d-%m-%Y %H:%M')

    independent_var = np.array([10, 30, 45, 65]).reshape(-1, 1)
    dependent_var = np.array([5, 7, 9, 10])

    model = LinearRegression().fit(independent_var, dependent_var)

    plt.style.use('dark_background')
    fig = plt.figure() #make it on the outside of looping to avoid complication

    for i, data in enumerate(independent_var, start=1):

        if i == 1:
            plt.subplot(1, 2, i)
            plt.xlabel('Independent Variable')
            plt.ylabel('Dependent Variable')
            plt.title('Perfect Fit')
            plt.grid(alpha=0.3)
            plt.scatter(independent_var, dependent_var, color='blue', label='Actual Data', marker='*')
            plt.plot(independent_var, model.predict(independent_var), color='red', label='Prediction Line')

        elif i == 2:
            plt.subplot(1, 2, i)
            plt.xlabel('Independent Variable')
            plt.ylabel('Dependent Variable')
            plt.title('Perfect Prediction')
            plt.grid(alpha=0.3)
            plt.scatter(dependent_var, model.predict(independent_var), color='red', label='Dependent and Predicted')
            plt.plot([dependent_var.min(), dependent_var.max()], [dependent_var.min(), dependent_var.max()], label='Accuracy')
        plt.legend()
        
    fig.text(0.01, 0.01, time, fontsize=7.5, color='gray', alpha=0.7, 
             ha='left', va='bottom')
    print(f'the prediction are {model.predict(independent_var)}')

    plt.tight_layout()
    plt.savefig('workplace.png')
    plt.show()

if __name__ == '__main__':
    main()