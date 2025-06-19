import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Hours studied (input feature)
hours_studied = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]).reshape(-1, 1)

# Pass (1) or fail (0) (target variable)
exam_result = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1, 1])

model = LogisticRegression().fit(hours_studied, exam_result)

#Predict for new Data
list_of_prediction = np.array([1.2, 1.9, 2.8, 3]).reshape(-1, 1)
prediction = model.predict(list_of_prediction)

print(prediction)

# Plot the data points
plt.scatter(hours_studied, exam_result, color='blue', label='Actual data')

# Create a range of values for plotting the curve
x_values = np.linspace(0, 5, 100).reshape(-1, 1)
y_proba = model.predict_proba(x_values)[:, 1]

# Plot the logistic regression curve
plt.plot(x_values, y_proba, color='red', label='Logistic regression curve')

plt.xlabel('Hours Studied')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression Example')
plt.legend()
plt.savefig('LOG_R.png')
plt.show()

print('Done')