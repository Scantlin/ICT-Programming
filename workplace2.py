import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

def main():
    data = pd.read_csv('Salary_dataset.csv')
    print(data['Salary'])

if __name__ == '__main__':
    main()