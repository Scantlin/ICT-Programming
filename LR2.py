# this is linear regression multi variable
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    data = {
        "Size": [21, 37, 43, 51],
        "Price": [200, 700, 900, 1000],
        "Sales": [30, 70, 40, 20]
    }

    dataframe = pd.DataFrame(data)

    Xlabel = dataframe[['Size', 'Price']]
    Ylabel = dataframe['Sales']

    model = LinearRegression().fit(Xlabel, Ylabel)
    predictions = model.predict(Xlabel)
    
    print("Predictions:", predictions)
    print(f'Linear regression coefficients are {model.coef_} and the intercept is {model.intercept_}')
    
    # Create a 3D plot
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(10, 7))
    d3 = plt.subplot(111, projection='3d')
    
    # Plot the actual data points
    d3.scatter(dataframe['Size'], dataframe['Price'], dataframe['Sales'], 
               c='red', marker='*', s=100, label='Actual Data')
    
    # Create a meshgrid for the regression plane
    size = np.linspace(dataframe['Size'].min(), dataframe['Size'].max(), 10)
    Price = np.linspace(dataframe['Price'].min(), dataframe['Price'].max(), 10)
    size, Price = np.meshgrid(size, Price)
    
    # Calculate predicted values for the plane
    Sales = model.intercept_ + model.coef_[0] * size + model.coef_[1] * Price
    
    # Plot the regression plane
    d3.plot_surface(size, Price, Sales, color='orange', alpha=0.3, label='Regression Plane')
    
    # Set labels
    d3.set_xlabel('Size')
    d3.set_ylabel('Price')
    d3.set_zlabel('Sales')
    d3.set_title('Multiple Linear Regression')
    
    # Add legend
    plt.legend()
    
    plt.savefig('LR2.png')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()