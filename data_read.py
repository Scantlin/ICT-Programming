import pandas as pd
import sqlite3
from icecream import ic as print
from IPython.display import display, Markdown

def connect(connection):
    edit = connection.cursor()

    #edit.execute('CREATE TABLE users(Name TEXT, Age INTEGER, Program TEXT)')
    read = pd.read_sql('SELECT * FROM users', connection)
    read.to_csv('sample2.csv', index=False)
    display(pd.read_csv('sample2.csv'))

def delete(connection, name:str):
    query = 'DELETE FROM users WHERE Name=?'
    with connection:
        connection.execute(query, [name])

def editing(connection, name:str, age:int):
    query = 'UPDATE users SET Age = ? WHERE Name = ?'
    with connection:
        connection.execute(query, (age, name))

def adding(connection, name:str, age:int, program:str):
    query = 'INSERT INTO users(Name, Age, Program) VALUES(?,?,?)'
    #query = 'DELETE FROM users WHERE name=?'

    with connection:
        connection.execute(query, (name, age, program))

def main():
    set = sqlite3.connect('Practice.db')
    try:
        print('WELCOME TO YOUR DATABASE')
        choice = int(input('1. Add \n2. Delete\n3. Edit \n4. Show \nYour Choice: '))
        if choice == 1:
            name = input('Enter your name: ')
            age = int(input('Enter your age: '))
            program = input('Enter your program: ')
            adding(set, name, age, program)
        elif choice == 2:
            name = input("Enter the name you want to delete: ")
            delete(set, name)
        elif choice == 3:
            name = input('Enter your name: ')
            age = int(input('Enter your age: '))
            editing(set, name, age)

    except Exception as e:
        print(e)
    
    finally:
        connect(set)


if __name__ == '__main__':
    main()