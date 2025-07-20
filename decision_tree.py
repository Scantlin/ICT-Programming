from sklearn.model_selection import train_test_split #to split the dataset into train and test
from sklearn.tree import DecisionTreeRegressor #tree model
from sklearn.metrics import mean_absolute_error, mean_squared_error #to study the accuracy
from sklearn.preprocessing import OneHotEncoder #to convert categorical data into numerical
from sklearn.compose import ColumnTransformer #to transform it into columns
from sklearn.linear_model import LinearRegression #simple linear regression model
from sklearn.ensemble import RandomForestRegressor #random forest model
import pandas as pd
import numpy as np
import seaborn as sns #to load datesets

def main():
    data = sns.load_dataset('tips') #load dateset

    categorical_var =  data.select_dtypes(include=['object', 'category']).columns.tolist()

    #get dummies using pandas
    #get_dummies = pd.get_dummies(data, columns=categorical_var)
    #print(get_dummies)

    #Independent Variable and Dependent Variable
    Independent_var = data.drop(['tip'], axis=1)
    Depedendent_var = data['tip']

    #Split the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Depedendent_var, test_size=0.2, random_state=42)

    #Transform the categorical data
    processing = ColumnTransformer(transformers=[('category', OneHotEncoder(), categorical_var)], remainder='passthrough', verbose_feature_names_out=False)

    X_train_encoded = processing.fit_transform(X_train)
    X_test_encoded = processing.transform(X_test)

    #model
    model1 = RandomForestRegressor(random_state=42).fit(X_train_encoded, y_train)
    model = LinearRegression().fit(X_train_encoded, y_train) #got the highest
    model2 = DecisionTreeRegressor(random_state=42).fit(X_train_encoded, y_train)

    #predict
    predict = model.predict(X_test_encoded)
    print(predict)
    print(y_test.tolist())
    print(round(mean_absolute_error(y_test, predict), 2) * 100)

if __name__ == '__main__':
    main()