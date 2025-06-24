import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
import statsmodels.formula.api as smf

def main():
    dataset = {
        "Duration": [30, 30, 45, 45, 45, 60, 60, 60, 75, 75], 
        "Average_Pulse": [80, 85, 90, 95, 100, 105, 110, 115, 120, 125],
        "Max_Pulse": [120, 120, 130, 130, 140, 140, 145, 145 ,150, 150],
        "Calorie_Burnage": [240, 250, 260, 270, 280, 290, 300, 310, 320, 330],
        "Hours_Work": [10, 10, 8, 8, 0, 7, 7, 8, 0, 8],
        "Hours_sleep":[7, 7, 7, 7, 7, 8, 8, 8, 8, 8]
    }

    sample1 = np.array([80, 90]).reshape(-1, 1)
    sample2 = np.array([240, 260])

    dataframe = pd.DataFrame(dataset)
    
    Independent_var = dataframe[["Average_Pulse"]]
    Dependent_var = dataframe["Calorie_Burnage"]

    #Regression Table 
    model = smf.ols('Calorie_Burnage ~Average_Pulse', data=dataframe).fit()
    print(model.summary())

    slope, intercept, r, p, std_err = stats.linregress(dataframe["Average_Pulse"], dataframe["Calorie_Burnage"])
    print(f'slope: {slope} intercept: {intercept} r: {r} std_error: {std_err}')

    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependent_var, test_size=0.2, random_state=0)

    model = LinearRegression().fit(X_train, y_train)

    print(model.coef_[0])
    print(model.intercept_)

    #print(f'TEST MAE: {mean_absolute_error(y_train, y_pred_train)} R2: {r2_score(y_test, y_pred_test)}')
    #rint(dataframe.describe())
    
    #SEABORN HEATMAP
    correlation = dataframe.corr()
    axis = sns.heatmap(correlation, vmin=-1, vmax=1, center=0, cmap=sns.diverging_palette(50, 500, n=500), square=True)
    plt.savefig('Sample Test.png')
    plt.show()
    '''
    plt.style.use('dark_background')
    plt.figure(figsize=(8, 5))
    plt.scatter(dataframe['Hours_Work'], dataframe['Calorie_Burnage'], color='red', marker="*")
    #plt.plot(dataframe['Average_Pulse'], dataframe['Calorie_Burnage'])
    plt.xlabel('Hours_Work')
    plt.title('Sample Test')
    plt.ylabel('Calorie_Burnage')
    plt.savefig('Sample Test.png')
    plt.show()'''


if __name__ == '__main__':
    main()