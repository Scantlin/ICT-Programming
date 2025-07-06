from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import seaborn as sns
import pandas as pd

app = Flask(__name__)

# Route for the home page with a form
@app.route('/', methods=['GET', 'POST'])
def home():
    data = sns.load_dataset('iris')

    Independent_var = data.iloc[:, :-1]
    Dependent_var = data.iloc[:, -1]

    X_train, X_test, y_train, y_test = train_test_split(Independent_var, Dependent_var, test_size=0.5, random_state=0)

    model = RandomForestClassifier(random_state=0, criterion='gini').fit(X_train, y_train)

    y_pred = model.predict(X_test)

    output = "please enter all necessary data....."
    data = "not yet inputted"
    data2 = "not yet inputted"
    data3 = "not yet inputted"
    data4 = "not yet inputted"
    Accuracy = str(round(accuracy_score(y_test, y_pred), 2) * 100) + "%"

    if request.method == 'POST':

        # Get input from form
        Sepal_length = float(request.form.get('Sepal_length'))
        Sepal_width = float(request.form.get('Sepal_width'))
        Petal_length = float(request.form.get('Petal_length'))
        Petal_width = float(request.form.get('Petal_width'))

        output = "The Species of iris is " + str(model.predict([[Sepal_length, Sepal_width, Petal_length, Petal_width]])[0]).upper()
        data = "sepal length: " + str(Sepal_length)
        data2 = "sepal width: " + str(Sepal_width)
        data3 = "petal length: " + str(Petal_length)
        data4 = "petal width: " + str(Petal_width)

    # Render the template with the output
    return render_template('index.html', output=output, data=data, data2 = data2, data3 = data3, data4 = data4, Accuracy = Accuracy)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)