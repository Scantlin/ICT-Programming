from sklearn.model_selection import train_test_split
import tensorflow as tf 
import seaborn as sns

def main():
    #print(sns.get_dataset_names())
    data = sns.load_dataset('iris')

    independent_var = data.iloc[:, :-1]
    dependent_var = data.iloc[:, -1]

    #Split the data into Train and Test
    X_train, X_test, y_train, y_test = train_test_split(independent_var, dependent_var, test_size=0.2)

    
    #use tensorflow
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(256, input_shape = X_train.shape, activation='sigmoid'))
    model.add(tf.keras.layers.Dense(256, activation='sigmoid'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    #Fit the data test
    model.fit(X_train, y_train, epochs=600)
    
if __name__ == '__main__':
    main()