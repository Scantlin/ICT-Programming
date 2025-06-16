import numpy as np #for array and manipulation of data
import pandas as pd #for data reading or database
from sklearn.linear_model import LinearRegression #for predicting 
import matplotlib.pyplot as plt #for visualization
import sqlite3 #for database


def main():
    try:
        #The dataset

        xlabel = np.array([25, 28, 30, 18, 22]).reshape(-1,1) #independent Variable or inputted
        ylabel = np.array([50, 65, 75, 30, 45]) #dependent Variable or output

        plt.style.use('dark_background')

        #Linear Regression (Prediction)
        model = LinearRegression().fit(xlabel, ylabel)
        predict = model.predict(xlabel)
        print(predict)
        print(f'The slope: {model.coef_[0]}')
        print(f'The intercept: {model.intercept_}')

        #calculating the predicted price
        #Designing the graph for two diminsional
        plt.scatter(xlabel, ylabel, color='red', label='Data points')
        plt.title('Practice Graph')
        plt.xlabel('Independent (area)')
        plt.ylabel('Dependent (Sales)')
        plt.grid(alpha=0.5)

        #plotting the prediction
        plt.plot(xlabel, predict, color='blue', label='Regression Line')

        #Visualizing the graph
        legend = plt.legend()
        legend.get_frame().set_alpha(0.5)
        plt.show()

        #since the codespace doesnt support display, save it first
        plt.savefig('plot.png')
        plt.show()
        print('successfully saved')

    except Exception as e:
        print(e)

    finally:
        print('Thank you for using the program')

if __name__ == '__main__':
    main()