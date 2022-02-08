# Import

import numpy as np
import pandas as pd
from random import seed
from random import random
import matplotlib.pyplot as plt

# Data Structure

class DTMC:

    '''
    seaCondition = DTMC("seaCondition", 
                    ['calm', 'moderate', 'rough'],
                    ["CC","CM","CR","MC","MM","MR","RC","RM","RR"]
    '''
    
    def __init__(self, name, states, transitions):
        self.name = name
        self.states = np.array(states)
        self.transitions = np.array(transitions)

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getStates(self):
        return self.states

    def setStates(self, states):
        self.states = states

    def getTransitions(self):
        return self.transitions

    def setTransitions(self, transitions):
        self.transitions = transitions

      
"""seaConditionProbability = probability_dist('seaCondition',
                                            [1.0, 0.0, 0.0],
                                            [[0.6, 0.4, 0.0],
                                            [0.6, 0.3, 0.1],
                                            [0.0, 0.9, 0.1]])
"""

class probability_dist:

    def __init__(self, name, initial_state, states_probabilities):
        self.name = name
        self.initial_state = initial_state
        self.states_probabilities = states_probabilities
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getInitialState(self):
        return self.initial_state

    def setInitialState(self, initial_state):
        self.initial_state = initial_state

    def getStatesProbabilites(self):
        return self.states_probabilities

    def setStatesProbabilities(self, states_probabilites):
        self.states_probabilities = states_probabilities

class Manage:
    
    def __init__(self, name, dtmc, probability_dist):
        self.name=name
        self.dtmc=dtmc
        self.probability_dist=probability_dist
        self.transitionMatrix = probability_dist.getStatesProbabilites()
        self.states = dtmc.getStates()
        self.initialState = probability_dist.getInitialState()
        self.transitions=dtmc.getTransitions()
        


    def writeToFile(self, filename, dtmc, probability_dist):
        states = dtmc.getStates()
        #probability_states = probability_dist.getStatesProbabilites()
        initial_state = probability_dist.getInitialState()

        f = open(filename, 'w')
        f.write('MarkovChain ' + dtmc.getName() + '\n')
        f.write("  " + states[0] + ' -> ' + states[1] + ': ' + str(self.transitionMatrix[0][1]) + '; \n')
        f.write("  " + states[1] + ' -> ' + states[0] + ': ' + str(self.transitionMatrix[1][0]) + '; \n')
        f.write("  " + states[1] + ' -> ' + states[2] + ': ' + str(self.transitionMatrix[1][2]) + '; \n')
        f.write("  " + states[2] + ' -> ' + states[1] + ': ' + str(self.transitionMatrix[2][1]) + '; \n')

        f.write("\n")
        f.write('ProbabilityDistribution p0 of ' + dtmc.getName() + '\n')
        f.write('  ' + states[0]+"   "+str(self.initialState[0]) + '; \n')
        f.write('  ' + states[1]+":  "+str(self.initialState[1]) + '; \n')
        f.write('  ' + states[2]+":  "+str(self.initialState[2]) + '; \n')
        f.close()

    #Task 9
    def checkMarkovChain(self, dtmc, probability_dist):

        correct = True

        #Sjekk at initialvalues ikke er større enn 1:
        if sum(self.initialState)!=1:
            print("The sum of the initialvalues have to be equal to one")

        #Checking sum
        if (sum(self.transitionMatrix[0]) or sum(self.transitionMatrix[1]) or sum(self.transitionMatrix[2])) != 1:
            print("The sum of the probabilities is not correct!")
            correct = False 


         #Checking that CR and RC are not greater than 0.0. IF NEEDED
        '''if (transitionMatrix[0][2]):
            print("CR can not be greater than 0.0")
            correct = False

        if (transitionMatrix[2][0] > 0):
            print("RC can not be greater than 0.0")
            correct = False'''  


        #Checking in states:
        if (self.transitionMatrix[1][0] == 0 and self.transitionMatrix[2][0] == 0):
            print("You do not have in states for:", states[0])
            correct = False

        if (self.transitionMatrix[0][1] == 0 and self.transitionMatrix[2][1] == 0):
            print("You do not have in states for:", states[1])
            correct = False
        
        if (self.transitionMatrix[0][2] == 0 and self.transitionMatrix[1][2] == 0):
            print("You do not have in states for:", states[2])
            correct = False

       
            
        #Checking outstates:
        if (self.transitionMatrix[0][1] == 0 and self.transitionMatrix[0][2] == 0):
            print("You do not have out states for:", states[0])
            correct = False

        if (self.transitionMatrix[1][0] == 0 and self.transitionMatrix[1][2] == 0):
            print("You do not have out states for:", states[1])
            correct = False

        if (self.transitionMatrix[2][0] == 0 and self.transitionMatrix[2][1] == 0):
            print("You do not have out states for:", states[2])
            correct = False

        if correct:
            print("Congratulations, the DTMC and the probability distribution has feasible values.")


#CALCULATIONS
    #Task 10
    
    def calcProbDist(self):

        it = 0
        check = np.array([0, 0, 0])
        prob = np.dot(self.initialState,self.transitionMatrix)
       
        while not np.array_equal(check, prob):
            check = prob
            prob = np.round(np.dot(prob,self.transitionMatrix), decimals=4)
            it+=1
        print("Etter " + str(it) + " iterasjoner konvergerte sannsynligheten. Sannsynlighetsfordelingen ble: \n" + str(prob))    
        #return prob

    #Task 11
    
    def calcProbDistContinous(self, iterations):

        prob_progression = []
        distr_hist = [[0,0,0]]
        
        prob = np.dot(self.initialState,self.transitionMatrix)
        for x in range(1,iterations+1):
            prob = np.round(np.dot(prob,self.transitionMatrix), decimals=4)
            prob_progression.append(prob)
            print("The probability distribution after "+str(x)+" steps is: "+str(prob))

        return prob_progression


#Time Series

#Task 12
    def timeseries(self, numberOfStates):

        print("Start state: "+ str(self.states[0]))
        timeseries = []
        situationNow="CALM"
        for i in range(numberOfStates):
            if situationNow=="CALM":
                nextStateOptions=[self.states[0]]*6+[self.states[1]]*4
                change=random.choice(nextStateOptions)
            elif situationNow=="MODERATE":
                nextStateOptions=[self.states[0]]*6+[self.states[1]]*3+[self.states[2]]*1
                change=random.choice(nextStateOptions)
            else:
                nextStateOptions=[self.states[1]]*9+[self.states[2]]*1
                change=random.choice(nextStateOptions)
            timeseries.append(change)
            situationNow=change
        print("After "+str(numberOfStates)+" sequenses of states we end up with the follow timeseries: ")
        return timeseries
            
                    
#Task 4:

seaCondition = DTMC("seaCondition", 
                    ['CALM', 'MODERATE', 'ROUGH'],
                    [["CC","CM","CR"],
                    ["MC","MM","MR"],
                    ["RC","RM","RR"]])
                    
seaConditionProbability = probability_dist('seaCondition',
                                            [1.0, 0.0, 0.0],
                                            [[0.6, 0.4, 0.0],
                                            [0.6, 0.3, 0.1],
                                            [0.0, 0.9, 0.1]])

seaConditionManage = Manage('seaCondition', seaCondition, seaConditionProbability)
seaConditionManage.writeToFile('seaCondition.txt', seaCondition, seaConditionProbability) 
seaConditionManage.checkMarkovChain(seaCondition, seaConditionProbability)
seaConditionManage.calcProbDist()
seaConditionManage.calcProbDistContinous(15)
print(seaConditionManage.timeseries(100))


