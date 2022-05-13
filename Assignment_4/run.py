'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

'''
IT IS VERY IMPORTANT THAT THE RESULTS OF THIS CODE IS PUT IN CONTEXT WITH THE ATTACHED DOCUMENT
'''

from calculator import Calculator
from problem import Problem
from regression import Regression
import time

class Run:

    def __init__(self):
        pass
    
    def task5(self):
        problem = Problem()
        problem.loadAndFormatData('test_data\\test3.xlsx')
        problem.printData()
        print('\n')
        problem.printProblem()
        problem.exportProblem2Excel('test_data\\exported_data.xlsx')

    # Show experimentally why this approach is limited to small problems
    def task9(self):
        print('\n')
        problem = Problem()
        problem.loadAndFormatData('test_data\\test1.xlsx')
        calculator = Calculator(problem.getMachines(), problem.getJobs())
        print('TEST1:')
        calculator.experimentAllSchedules(problem)
        print('\n')

        # This part takes about 10 seconds to run, hold on
        problem = Problem()
        problem.loadAndFormatData('test_data\\test2.xlsx')
        calculator = Calculator(problem.getMachines(), problem.getJobs())
        print('TEST2:')
        calculator.experimentAllSchedules(problem)
        print('\n')

        # This part takes about 2 minutes to run, hold on
        problem = Problem()
        problem.loadAndFormatData('test_data\\test3.xlsx')
        calculator = Calculator(problem.getMachines(), problem.getJobs())
        print('TEST3:')
        calculator.experimentAllSchedules(problem)
    
    def task12(self):
        problem = Problem()
        # Notice that this is the same dataset as the one the brute force method used 2 minutes
        problem.loadAndFormatData('test_data\\test3.xlsx')
        calculator = Calculator(problem.getMachines(), problem.getJobs())

        # Task 10 and 11
        calculator.experimentalStudyGradientDescent(problem, 5)
    
    def task14and15(self):
        problem = Problem()
        problem.loadAndFormatData('test_data\\test3.xlsx')
        calculator = Calculator(problem.getMachines(), problem.getJobs())

        # Task 14 and 15
        calculator.experimentalStudyUncertainties(problem, 5, leftTail=0.5, rightTail=1.5, allowedError=0.005)

    def task16(self):
        problemML = Problem()
        #problemML.createRandomJobScheduling(10, 50, 30, 5, 10)
        problemML.loadAndFormatData('test_data\\test2.xlsx')
        calculatorML = Calculator(problemML.getMachines(), problemML.getJobs())  
        regressionML = Regression(problemML, calculatorML)

        dataframe = regressionML.createPandasDataframe(leftTail=0.5, rightTail=1.5)
        print(dataframe)
        X_train, X_test, y_train, y_test = regressionML.prepare4ML(dataframe, test_size=0.3)

        '''Run the different regression algorithms'''
        regressionML.decisionTree(X_train, X_test, y_train, y_test, True)
        #LinearSVR struggles to converge, needs more data
        regressionML.linearSVR(X_train, X_test, y_train, y_test, True)
        regressionML.kNearestNeighbor(X_train, X_test, y_train, y_test, True)
        regressionML.bayesianRidge(X_train, X_test, y_train, y_test, True)
        regressionML.lightGBM(X_train, X_test, y_train, y_test, True)
    
    def task18(self):
        problemML = Problem()
        problemML.createRandomJobScheduling(5, 50, 20, 5, 20)
        #problemML.loadAndFormatData('test_data\\test2.xlsx')
        calculatorML = Calculator(problemML.getMachines(), problemML.getJobs())

        start_timeGD = time.time()
        uncertainSchedule, uncertainMakespan = calculatorML.gradientDescentV2Uncertainties(problemML, n_initialStates=5, leftTail=0.5, rightTail=1.5, doPrint=False)
        print(f'The best schedule was: {uncertainSchedule}')
        print(f'The makespan of the best schedule was: {uncertainMakespan}')
        print(f'The runtime of the gradient descent algorithm V2 with uncertainties was: {round(time.time() - start_timeGD, 3)} seconds\n')

        start_timeML = time.time()
        MLSchedule, MLMakespan = calculatorML.gradientDescentUncertaintiesWithML(problemML, 5, 0.5, 1.5, 1000, doPrint=False)
        print(f'The best schedule was: {MLSchedule}')
        print(f'The makespan of the best schedule was: {MLMakespan}')
        print(f'The runtime of the gradient descent algorithm with uncertainties and ML was: {round(time.time() - start_timeML, 3)} seconds\n')


        
run = Run()

'''UNCOMMENT TO RUN TASK 5'''
#run.task5()

'''UNCOMMENT TO RUN TASK 9'''
#run.task9()

'''UNCOMMENT TO RUN TASK 12'''
#run.task12()

'''UNCOMMENT TO RUN TASK 14 and 15'''
#run.task14and15()

'''UNCOMMENT TO RUN TASK 16'''
#run.task16()

'''UNCOMMENT TO RUN TASK 18'''
#run.task18()