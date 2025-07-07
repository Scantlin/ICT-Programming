from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf 
import seaborn as sns

def main():
    #print(sns.get_dataset_names())
    data = sns.load_dataset('iris')

    independent_var = data.iloc[:, :-1]
    dependent_var = data.iloc[:, -1]

    le = LabelEncoder()
    dependent_var = le.fit_transform(dependent_var)

    #Split the data into Train and Test
    X_train, X_test, y_train, y_test = train_test_split(independent_var, dependent_var, test_size=0.2)
    
    #use tensorflow
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(256, input_shape = (X_train.shape[1], ), activation='relu'))
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dense(3, activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    #Fit the data test
    model.fit(X_train, y_train, epochs=100)
    print(model.evaluate(X_test, y_test))

if __name__ == '__main__':
    main()