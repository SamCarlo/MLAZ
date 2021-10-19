# Data Preprocessing template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#Fitting Linear Regression onto the Dataset
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predict the test set results
y_pred = regressor.predict(X_test)

#Sam's own thing: create an error vector
err_vect = y_pred-y_test

#Visualize the training set with pyplot
plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train, regressor.predict(X_train), color ='green')
plt.title('Year of Experience vs Salary (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

#viz the test set as well
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Test Set Results')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""