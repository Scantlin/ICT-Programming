from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import numpy as np 
import pandas as pd
from tqdm import tqdm
import time

class Main:
    def main(self):
        try:
            '''
            for i in tqdm(range(10)):
                time.sleep(1) '''
                
            data = sns.load_dataset('iris')

            Independent_var = data.drop(['species'], axis=1)
            Dependendent_var = data['species']

            X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependendent_var, test_size=0.5, random_state=0)

            '''
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)'''

            #model = KNeighborsClassifier().fit(X_train, y_train)
            model = LogisticRegression().fit(X_train, y_train)

            y_pred = model.predict(X_test)

            '''
            for i, datas in enumerate(model.feature_importances_):
                print(f'{X_train.columns[i]}: {datas}')'''

            print(accuracy_score(y_test, y_pred))

            #print(model.feature_importances_.argsort()[::-1])
        except Exception as e:
            print(e)

        finally:
            print('Thank you for using the program')

if __name__ == '__main__':
    Main().main()