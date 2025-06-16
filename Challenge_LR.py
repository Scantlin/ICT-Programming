import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
import warnings

#datesets
def main():
    data = {
        "feature1" : [2.5, 4.1, 3.2, 5.0, 1.8, 3.6, 4.8, 2.0, 5.5, 1.5],
        "feature2" : [3.5, 2.2, 4.6, 1.5, 5.0, 2.8, 3.0, 4.2, 2.0, 6.0],
        #"Feature3" : [1.8, 3.0, 2.5, 4.2, 0.9, 3.5, 2.0, 1.5, 5.0, 0.5],
        "Target" : [12.1, 15.3, 18.7, 20.5, 9.8, 17.2, 22.0, 13.5, 25.1, 8.3]
    }

    warnings.filterwarnings('ignore')

    dataframe = pd.DataFrame(data)

    Xlabel = dataframe[['feature1', 'feature2']]
    ylabel = dataframe['Target']

    model = LinearRegression().fit(Xlabel, ylabel)
    #print(model.predict(Xlabel))
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 7))

    ax = plt.subplot(111, projection='3d')

    ax.scatter(dataframe['feature1'], dataframe['feature2'], dataframe['Target'], c='red', marker='*', s=100 ,label='Actual Data')

    feature1 = np.linspace(dataframe['feature1'].min(), dataframe['feature1'].max(), 10)
    feature2 = np.linspace(dataframe['feature2'].min(), dataframe['feature2'].max(), 10)

    feature1, feature2 = np.meshgrid(feature1, feature2)

    #formula for the prediction
    Target = model.intercept_ + model.coef_[0] * feature1 + model.coef_[1] * feature2

    ax.plot_surface(feature1, feature2, Target, color='yellow', label='Linear Regression', alpha=0.5)
    ax.legend()
    ax.set_xlabel('feature1')
    ax.set_ylabel('feature2')
    ax.set_zlabel('Target')
    ax.set_title('Challenge for Linear Regression')

    plt.savefig('Challenge.png')
    plt.show()
    print('Saved Successfully')

if __name__ == '__main__':
    main()