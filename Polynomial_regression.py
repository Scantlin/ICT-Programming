#sample of polynomial regression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.array([1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]).reshape(-1, 1)
    y = np.array([100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100])

    #Split the data
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    #initialize a polynomial to transform the X
    initialization_poly = PolynomialFeatures(degree=3, include_bias=False)

    #fit and transform the train set into polynomial before fitting into the model
    X_train_poly = initialization_poly.fit_transform(X_train)

    #Create a model
    model = LinearRegression().fit(X_train_poly, y_train)

    #Fit and transform also the test set before the prediction
    X_test_poly = initialization_poly.fit_transform(X_test)
    Y_prediction = model.predict(X_test_poly)

    '''
    sample = np.array([25, 23, 25, 27, 19]).reshape(-1, 1)
    sample_poly = initialization_poly.fit_transform(sample)
    print(model.predict(sample_poly))'''

    #to see the accuracy and error of the test set and the prediction
    accuracy = {
        'prediction: ':Y_prediction,
        'y_test: ': y_test,
        'error': abs(Y_prediction - y_test)
    }

    print(accuracy)

    #To plot the Polynomial Regression we must have a X_plot
    x_plot = np.linspace(min(x), max(x), max(y)).reshape(-1, 1)
    #fit and transform the X_plot
    x_plot_poly = initialization_poly.fit_transform(x_plot)
    #Predict it to form a line
    y_plot = model.predict(x_plot_poly)

    plt.scatter(X_train, y_train, color='blue', label='training set')
    plt.scatter(X_test, y_test, color='violet', label='Test set')
    plt.plot(x_plot, y_plot, color='red',linewidth=2 ,label='Polynomial Regression (degree of 3)')
    plt.legend()
    plt.savefig('Polynomial_regression2.png')
    plt.show()

def main2():
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

    mymodel = np.polyfit(x, y, 3)
    model = np.poly1d(mymodel)

    myline = np.linspace(1, 22, 100)
    print(model(1)) #predict a data in x or my choice

    plt.scatter(x, y)
    plt.plot(myline, model(myline))
    plt.savefig('Polynomial_regression.png')
    plt.show()


if __name__ == '__main__':
    main()
    #main2()

