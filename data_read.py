import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot 
import pandas as pd
import sqlite3

def connection(connection):
    edit = connection.cursor()

    """edit.execute('''
CREATE TABLE 'users'('Name' TEXT, 'Age' INTEGER)''')"""

    edit.execute('INSERT INTO users(Name, Age, Program) VALUES (?, ?, ?)', ('Scantlin Cayson', 19, 'BSCPE'))
    #edit.execute('ALTER TABLE users ADD Program TEXT')
    
    read = pd.read_sql('SELECT * FROM users', connection)
    print(read)

def main():
    connect = sqlite3.connect('practice.db')
    connection(connect)

if __name__ == '__main__':
    main()