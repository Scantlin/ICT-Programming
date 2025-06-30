#THIS IS A RANDOM TREE CLASSIFIER
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

def main():
    try:
        data = pd.read_csv('heart.csv')
        Independent_var = data.iloc[:, :-1]
        Depedendent_var = data.iloc[:, -1]

        #Split the dataset
        X_train, X_test, y_train, y_test = train_test_split(Independent_var, Depedendent_var, test_size=0.2, random_state=42)

        #print(data.isnull().sum()) to check  if the dataset contains null 

        #Convert the Categorical into numerical data
        Categorical = data.select_dtypes(include=['object']).columns.tolist() #We must first know which column consist of categorical data
        
        #Processing for the encoding #Drop None when you are using ENSEMBLE
        Encoding = ColumnTransformer(transformers=[('cat', OneHotEncoder(sparse_output=False, drop=None), Categorical)], remainder='passthrough', verbose_feature_names_out=False)

        #Starting encoding the categorical infos
        X_train_encoded = Encoding.fit_transform(X_train) #Fit_transform
        X_test_encoded = Encoding.transform(X_test) #transform, to avoid overfitting

        model = RandomForestClassifier(criterion='gini', random_state=42, max_depth=10, max_samples=100).fit(X_train_encoded, y_train)
        #model = LogisticRegression(max_iter=100).fit(X_train_encoded, y_train)
        y_pred_test = model.predict(X_test_encoded)

        accuracy = accuracy_score(y_test, y_pred_test) * 100
        
    except Exception as e:
        print(e)

    finally:
        print('Thank you for using the program')

if __name__ == '__main__':
    main()