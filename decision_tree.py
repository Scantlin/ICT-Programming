from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    dataset = sns.load_dataset('iris')

    Independent_var = dataset.drop(['species'], axis=1)
    Dependent_var = dataset['species']


    Independent_var_names = Independent_var.columns.tolist()

    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependent_var, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100,criterion='gini').fit(X_train, y_train)
    y_pred2 = model.predict(X_test)

    print(accuracy_score(y_test, y_pred2))
    
    '''
    fig = plt.figure(figsize=(10, 8))
    tree.plot_tree(model, feature_names= Independent_var_names,filled=True)
    plt.savefig('decision_tree.png')
    plt.show()'''


if __name__ == '__main__':
    main()