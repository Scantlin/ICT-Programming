#from icecream import ic as print
import sqlite3
import pandas as pd
import matplotlib.pyplot
from sklearn.linear_model import LinearRegression

def insering(course, units):
    Course.append(course)
    Units.append(units)

    return Course, Units

def calculation():
    #where calculation happens
    print('calculate')

def main():
    global Course
    global Units

    Course = []
    Units = []

    count = int(input('Enter how many course you\'ll enter: ' ))
    for i in range(1, count+1):
        inCourse = input('Enter your courses: ').upper()
        inUnits = int(input("Enter units: "))
        container(inCourse, inUnits)

    print(Course)
    print(Units)

if __name__ == '__main__':
    main()