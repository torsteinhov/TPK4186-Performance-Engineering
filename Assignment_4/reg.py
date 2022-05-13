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


'''  
   TASK 16 

    Methods
    -------

    createPandasDataframe(leftTail, rightTail)
        creates a dataframe with all possible schedules
    prepare4ML(dataframe)
        prepares the data for the machine learning algorithms
    decisionTree(X_train, X_test, y_train, y_test, doPrint)
        initializes a desision tree regressor from scikit, fits the model, predicts it and prints the accuracy 
    linearSVR(X_train, X_test, y_train, y_test, doPrint)
        initializes a Linear Support Vector Regressor from scikit, fits the model, predicts it and prints the accuracy 
    kNearestNeighbor(X_train, X_test, y_train, y_test, doPrint)
        initializes a k-nearest neighbor regressor from scikit, fits the model, predicts it and prints the accuracy 
    lightGBM(X_train, X_test, y_train, y_test, doPrint)
        initializes a light GBM regressor from scikit, fits the model, predicts it and prints the accuracy 
    '''


problem = Problem(filename='test2.xlsx')
problem.loadAndFormatData()
calculator = Calculator(problem.getMachines(), problem.getJobs())

def createPandasDataframe(leftTail, rightTail):
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

dataframe = createPandasDataframe(leftTail=0.5, rightTail=1.5)
print('DATAFRAME:\n')
print(dataframe)

def prepare4ML(dataframe):

    X = dataframe.iloc[:, dataframe.columns != 'Target']
    y = dataframe['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    return X_train, X_test, y_train, y_test

def decisionTree(X_train, X_test, y_train, y_test, doPrint):
    dt = DecisionTreeRegressor(random_state=0)
    dt = dt.fit(X_train, y_train)
    y_predict = dt.predict(X_test)

    if doPrint:
        print("The accuracy of the Decision tree is:",metrics.r2_score(y_test, y_predict))

def linearSVR(X_train, X_test, y_train, y_test, doPrint):
    svr = LinearSVR(random_state=0)
    svr = make_pipeline(StandardScaler(), LinearSVR(random_state=0, tol=1e-5))
    svr = svr.fit(X_train, y_train)
    y_predict = svr.predict(X_test)

    if doPrint:
        print("The accuracy of the LinearSVR is:",metrics.r2_score(y_test, y_predict))

def kNearestNeighbor(X_train, X_test, y_train, y_test, doPrint):
    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(X_train, y_train)
    y_predict = knn.predict(X_test)

    if doPrint:
        print("The accuracy of the K nearest neighbor is:",metrics.r2_score(y_test, y_predict))

def lightGBM(X_train, X_test, y_train, y_test, doPrint):
    lgbm = LGBMRegressor()
    lgbm.fit(X_train, y_train)
    y_predict = lgbm.predict(X_test)

    if doPrint:
        print("The accuracy of the LightGBM is:",metrics.r2_score(y_test, y_predict))
    
    return y_predict

X_train, X_test, y_train, y_test = prepare4ML(dataframe)
print('\n')

'''Run the different regression algorithms'''
decisionTree(X_train, X_test, y_train, y_test, True)
linearSVR(X_train, X_test, y_train, y_test, True)
kNearestNeighbor(X_train, X_test, y_train, y_test, True)
lightGBM(X_train, X_test, y_train, y_test, True)