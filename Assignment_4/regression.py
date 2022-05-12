'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

'''TASK 16'''

from random import random
import numpy as np
import pandas as pd
from calculator import Calculator
from problem import Problem
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import LinearSVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from lightgbm import LGBMRegressor
from sklearn import metrics

problem = Problem(filename='test2.xlsx')
problem.loadAndFormatData()
calculator = Calculator(problem.getMachines(), problem.getJobs())

def createDataframe(leftTail, rightTail):
    data = []
    allSchedules = calculator.generateAllPossibleSchedulesWithUncertainties(leftTail, rightTail)
    for schedule in allSchedules:
        operationTime = calculator.calcTotalUncertainOperationTime(schedule, problem)
        datarow = schedule
        datarow.append(operationTime)
        data.append(datarow)
    
    df = pd.DataFrame(data)
    
    columns = []
    for i in range(len(df.iloc[0])):
        if i == len(df.loc[0])-1:
            columns.append('Target')
            break
        columns.append('Attribute_'+str(i+1))
    
    df.columns = columns
    return df

dataframe = createDataframe(leftTail=0.5, rightTail=1.5)
print('DATAFRAME:\n')
print(dataframe)

def prepare4ML(dataframe):

    X = dataframe.iloc[:, dataframe.columns != 'Target']
    y = dataframe['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = prepare4ML(dataframe)
print('\n')

def decisionTree():
    dt = DecisionTreeRegressor(random_state=0)
    dt = dt.fit(X_train, y_train)
    y_predict = dt.predict(X_test)

    print("The accuracy of the Decision tree is:",metrics.r2_score(y_test, y_predict))

def linearSVR():
    svr = LinearSVR(random_state=0)
    svr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, tol=1e-5))
    svr = svr.fit(X_train, y_train)
    y_predict = svr.predict(X_test)

    print("The accuracy of the LinearSVR is:",metrics.r2_score(y_test, y_predict))

def kNearestNeighbor():
    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_predict = knn.predict(X_test)
    print("The accuracy of the K nearest neighbor is:",metrics.r2_score(y_test, y_predict))

def lightGBM():
    lgbm = LGBMRegressor()
    lgbm.fit(X_train, y_train)
    y_predict = lgbm.predict(X_test)
    print("The accuracy of the LightGBM is:",metrics.r2_score(y_test, y_predict))


'''Run the different regression algorithms'''
decisionTree()
linearSVR()
kNearestNeighbor()
lightGBM()