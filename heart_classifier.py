from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd 
import numpy as np

class Main:
    def main(self):
        try:
            #Load datasets
            data = pd.read_csv('heart.csv')

            #Study the datasets
            '''
            print(data.info())
            print(data.describe())
            print(data.isnull().sum())'''

            #Independent and Dependent Var
            Independent_var = data.iloc[:, :-1]
            Dependent_var = data.iloc[:, -1]

            #Category identifier and converted into list
            Categorical_var = data.select_dtypes(include=['object', 'category']).columns.tolist()

            #Split the dataset
            X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependent_var, test_size=0.2, random_state=42)

            #Encoding of categorical variable
            Encoding = ColumnTransformer(transformers=[('cat', OneHotEncoder(), Categorical_var)], remainder='passthrough', verbose_feature_names_out=False)

            X_train_encoded = Encoding.fit_transform(X_train) #use fit_transform always in X_train set
            X_test_encoded = Encoding.transform(X_test) #transform to avoid overfitting or data leakage

            #Create a grid parameter for the model

            grid_param = {
                'n_estimators': [100, 200, 300],
                'max_depth': [None, 10, 20, 30],
                'min_samples_split': [2, 5, 10],
                'max_features': ['sqrt', 'log2'],
            }

            #Model
            Model = GridSearchCV(RandomForestClassifier(random_state=42), grid_param, cv=5).fit(X_train_encoded, y_train)
            prediction_test = Model.predict(X_test_encoded)

            print(accuracy_score(y_test, prediction_test))
            print(confusion_matrix(y_test, prediction_test))

        except Exception as e:
            print(e)

        finally:
            print('Thank you for using the program')

if __name__ == '__main__':
    Main().main()
