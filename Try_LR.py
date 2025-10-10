import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def main():
    data = {
        "Size": [2, 3, 6, 7, 8, 10, 2, 12, 15, 13, 15, 17, 18, 21, 12, 2, 4, 10, 12, 13, 17],
        "Sex": ['male', 'female', 'female', 'female', 'female', 'male', 'male', 'male', 'unisex', 'female', 'unisex', 'unisex', 'male', 'unisex', 'unisex', 'female', 'female', 'female', 'male', 'male', 'unisex'],
        "Price":[100, 150, 230, 150, 175, 230, 300, 100, 350, 250, 370, 380, 340, 430, 230, 205, 220, 230, 200, 210, 300]
    }

    dataframe = pd.DataFrame(data) #use dataframe if you have a data store in dictionary
    
    Independent_var = dataframe.drop(["Price"], axis=1) #Drop the Dependent
    Dependent_var = dataframe["Price"]

    #Split the Data
    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependent_var, test_size=0.2, random_state=0)

    #Transform the categorical data
    Processing = ColumnTransformer(transformers=[("sex", OneHotEncoder(drop='first'), ["Sex"])], remainder='passthrough')
    
    #The transformed data must be insert into the train and test independent var
    X_train_encoded = Processing.fit_transform(X_train) # must use fit transform
    X_test_encoded = Processing.transform(X_test) #must use transform only

    model = LinearRegression().fit(X_train_encoded, y_train)

    y_train_pred = model.predict(X_train_encoded)
    y_test_pred = model.predict(X_test_encoded)

    print(f'TRAIN MAE: {mean_absolute_error(y_train, y_train_pred):.2f} R2: {(r2_score(y_train, y_train_pred)*100):.2f}%')
    print(f'TEST MAE: {mean_absolute_error(y_test, y_test_pred):.2f} R2: {(r2_score(y_test, y_test_pred) * 100 ):.2f}%')

if __name__ == '__main__':
    main()
