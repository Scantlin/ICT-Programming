from flask import Flask, render_template, request
import pandas as pd
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) #Route for the home page
def home():
    name = ''
    score = 0
    result = ''
    if request.method == 'POST':
        name = request.form.get('Your_name').replace('.', '').lower()
        crush = request.form.get('Crush').replace('.', '').lower()

        sum_len = len(name + crush)

        score = function(name, crush, sum_len)

        flames = 'FLAMES'
        flames = flames * score
        result = flames[score-1]

        print(f'result: {result}')

        match(result):
            case 'F':
                result = 'FRIEND'
            case 'L':
                result = 'LOVER'
            case 'A':
                result = 'AFFECTIONATE'
            case 'M':
                result = 'MARRIAGE'
            case 'E':
                result = 'ENEMY'
            case 'S':
                result = 'SEX'
            case _:
                result = 'Cant Identify'

        database(names=name, crushes=crush, results=result)
                    
    return render_template('structure.html', name=result)

def database(names:str, crushes:str, results:str):
    set_connect = sqlite3.connect('Flames.db')
    #edit = set_connect.cursor()
    #edit.execute('CREATE TABLE users(Name TEXT, Crush TEXT, result TEXT)') #Creating a table

    #query = 'INSERT INTO users (Name, Crush, result) VALUES(?,?,?)'
    query = 'DELETE FROM users WHERE Name=?'

    with set_connect:
        set_connect.execute(query, ['John Scantlin B Cayson'])

    read = pd.read_sql('SELECT * FROM users', set_connect)
    read.to_csv('Flames.csv', index=False)

def function(Name:str, Crush:str, Ov_len:int):
    for i in Name:
        if i in Crush:
            Name = Name.replace(i, '')
            Crush = Crush.replace(i, '')

    print(Name)
    print(Crush)
    return Ov_len - len(Name + Crush)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)