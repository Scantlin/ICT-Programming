from flask import Flask, render_template, request #To create webpage with the python as backend
from sklearn.model_selection import train_test_split #for splitting the data
from sklearn.ensemble import RandomForestRegressor #For regression using random forest
from sklearn.metrics import r2_score, mean_absolute_error
import pandas as pd 
import seaborn as sns
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #Route for the home page

def home():
    greet = ""
    if request.method == 'POST':
        greet = request.form.get('Scantlin')

    return render_template('structure.html', name=greet)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)