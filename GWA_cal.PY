from icecream import ic as print
import sqlite3
import pandas as pd
import matplotlib.pyplot
from sklearn.linear_model import LinearRegression

def calculation():
    #where calculation happens
    print('calculate')

def main():
    Course = []
    Units = []

    count = int(input('Enter how many course you\'ll enter: ' ))
    for i in range(1, count+1):
        inCourse = input('Enter your courses: ').upper()
        inUnits = int(input("Enter units: "))
        Course.append(inCourse)
        Units.append(inUnits)
    
    print(Course)
    print(Units)

if __name__ == '__main__':
    main()