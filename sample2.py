from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

def main():
    dataset = {
        "Colors": ['red', 'yellow', 'green', 'blue', 'white', 'orange'],
        "Num": [1, 5, 6, 8, 10, 11]
    }

    df = pd.DataFrame(dataset)

    encoder = ColumnTransformer(transformers=[('cat', OneHotEncoder(sparse_output=False), ['Colors'])], remainder='passthrough')
    print(encoder.fit_transform(df))

    LE = LabelEncoder()
    print(LE.fit_transform(df['Colors']))

    #Manually Assigning the corresponds numerical Value into the categorical
    ''' from sklearn.preprocessing import LabelEncoder

data = {'Size': ['S', 'M', 'L', 'XL']}
df = pd.DataFrame(data)

size_order = {'S': 0, 'M': 1, 'L': 2, 'XL': 3}  # Manually define order
df['Size_Encoded'] = df['Size'].map(size_order)'''

if __name__ == '__main__':
    main()
