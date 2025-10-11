import pandas as pd #To read CSV files from Local
from sklearn.linear_model import LogisticRegression #Classifier model
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import seaborn as sns

def main():
    Data_names_SNS = sns.get_dataset_names() #Get the set of dataset inside seaborn library

    load_data = sns.load_dataset('iris')
    
    X = load_data.drop(["species"], axis=1)
    y = load_data["species"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    model = LogisticRegression(random_state=42, max_iter=200).fit(X_train, y_train)

    prediction = model.predict(X_test)

    for i in range(len(prediction)):
        print(f"Predicted: {prediction[i]} Actual: {y_test[i]}")
    
    print(accuracy_score(y.head(), prediction))

if __name__ == "__main__":
    main()