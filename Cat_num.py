from sklearn.model_selection import train_test_split, GridSearchCV #To split the data
from sklearn.ensemble import RandomForestRegressor #To create a model using random forest
from sklearn.metrics import r2_score, mean_absolute_error #To see the accuracy
from sklearn.preprocessing import OneHotEncoder #To convert categorical data into numerical
from sklearn.compose import ColumnTransformer #Upon convertion it is necessary to make it array
from sklearn.linear_model import LinearRegression
import numpy as np 
import pandas as pd #To access the data frame
from scipy import stats

class Main:
    def main(self):
        try:
            data = {
                'Size': [5, 7, 10, 12, 15, 8, 10, 20, 12, 18, 6, 9, 11, 14, 16, 4, 7, 13, 17, 19, 5, 8, 10, 15, 20, 10, 12, 14, 16, 18],
                'Colors': ['red', 'Blue', 'Yellow', 'Green', 'Violet', 'red', 'Blue', 'Yellow', 'Green', 'Violet', 
                            'red', 'Blue', 'Yellow', 'Green', 'Violet', 'red', 'Blue', 'Yellow', 'Green', 'Violet',
                            'red', 'Blue', 'Yellow', 'Green', 'Violet', 'red', 'Blue', 'Yellow', 'Green', 'Violet'],
                'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M',
                            'F', 'M', 'F', 'M', 'M', 'M'],
                'Price': [120, 220, 320, 420, 500, 130, 230, 350, 450, 510, 
                        110, 210, 310, 410, 490, 100, 200, 300, 400, 480,
                        125, 225, 325, 425, 505, 135, 235, 355, 455, 515]
                }

            #Since the dataset is in dict type, make it a dataframe using the pandas
            dataframe = pd.DataFrame(data)
            
            #Seperate the Independent Variable into the Dependent Var
            Independent_var = dataframe.iloc[:, :-1]
            Dependent_var = dataframe.iloc[:, -1]

            '''
            slope, intercept, r, p, std_error = stats.linregress(Independent_var, Dependent_var)

            info = {
                "slope": slope,
                "intercept": intercept,
                "r": r,
                "std_error": std_error
            }

            print(info)'''

            #Split the dataframe into Train and Test
            X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependent_var, test_size=0.2, random_state=42)

            print(X_train_scaled)
                        
            #Transformed the categorical Data into Numerical Data but in a Binary way since the data are nominal
            Categorical_var = dataframe.select_dtypes(include=['object']).columns.tolist()
            encoding = ColumnTransformer(transformers=[('cat', OneHotEncoder(sparse_output=False), Categorical_var)], remainder='passthrough', verbose_feature_names_out=False)

            X_train_encoded = encoding.fit_transform(X_train)
            X_test_encoded = encoding.transform(X_test)


            #Creating the grid search CV to find the best hyperparameters
            
            parameter_grid = {
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'max_features': ['sqrt', 'log2']
            }

            #Creating a model
            Model = GridSearchCV(RandomForestRegressor(), parameter_grid, cv=5).fit(X_train_encoded, y_train)
            y_pred = Model.predict(X_test_encoded)

            error = abs(y_test - y_pred)

            Analysis = {
                "Y prediction": y_pred.tolist(),
                "Y test": y_test.tolist(),
                'error': round(error, 2).tolist(),
                'Absolute Error': sum(error)/len(error)
            }
            print(Analysis)
            print(mean_absolute_error(y_test, y_pred))
            print(r2_score(y_test, y_pred) * 100)

        except Exception as e:
            print(e)

        finally:
            print('Thank you for using the program')


if __name__ == '__main__':
    program = Main()
    access = program.main()
