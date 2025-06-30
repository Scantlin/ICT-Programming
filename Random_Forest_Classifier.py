from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import seaborn as sns
import numpy as np 

def main():
    #print(sns.get_dataset_names()) <- to see all the free dataset
    dataset = sns.load_dataset('titanic')
    dataset.dropna(inplace=True)
    dataset.drop(['survived','pclass', 'deck', 'fare', 'embark_town', 'embarked'], axis=1, inplace=True) #Drop the column that is not needed in determining the survival

    categorical_var = dataset.select_dtypes(include=['object', 'category']).columns.tolist()

    for cat in categorical_var:
        LE = LabelEncoder()
        dataset[cat] = LE.fit_transform(dataset[cat])
    
    #Assigned the Independent Var and the Dependent Variable
    Independent_var = dataset.drop(['alive'], axis=1)
    Depedendent_var = dataset['alive']

    print(Depedendent_var)
    print(Independent_var)

    #Split the dataset into train and Test
    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Depedendent_var, test_size=0.2, random_state=42)

    #Create a model
    model = RandomForestClassifier(n_estimators=42, criterion='gini', random_state=42).fit(X_train, y_train)

    #Prediction for Testing data
    y_pred = model.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))

if __name__ == '__main__':
    main()