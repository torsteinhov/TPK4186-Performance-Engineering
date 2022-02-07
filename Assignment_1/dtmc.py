# Import

import numpy as np
import pandas as pd
from random import seed
from random import random
import matplotlib.pyplot as plt

# Data structure

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
    

    def writeToFile(self, filename, dtmc, probability_dist):
        states = dtmc.getStates()
        probability_states = probability_dist.getStatesProbabilites()
        initial_state = probability_dist.getInitialState()

        f = open(filename, 'w')
        f.write('MarkovChain ' + dtmc.getName() + '\n')
        f.write("  " + states[0] + ' -> ' + states[1] + ': ' + str(probability_states[0][1]) + '; \n')
        f.write("  " + states[1] + ' -> ' + states[0] + ': ' + str(probability_states[1][0]) + '; \n')
        f.write("  " + states[1] + ' -> ' + states[2] + ': ' + str(probability_states[1][2]) + '; \n')
        f.write("  " + states[2] + ' -> ' + states[1] + ': ' + str(probability_states[2][1]) + '; \n')

        f.write("\n")
        f.write('ProbabilityDistribution p0 of ' + dtmc.getName() + '\n')
        f.write('  ' + states[0]+"   "+str(initial_state[0]) + '; \n')
        f.write('  ' + states[1]+":  "+str(initial_state[1]) + '; \n')
        f.write('  ' + states[2]+":  "+str(initial_state[2]) + '; \n')
        f.close()

    def checkMarkovChain(self, dtmc, probability_dist):

        transitionMatrix = probability_dist.getStatesProbabilites()
        states = dtmc.getStates()
        correct = True
        
        #Checking sum:
        if sum(transitionMatrix[0]) + sum(transitionMatrix[1]) + sum(transitionMatrix[2]) != 3:
            print("The sum of the probabilities is not correct!")
            correct = False
            
        #Cheking in states:
        if (transitionMatrix[1][0] == 0 and transitionMatrix[2][0] == 0):
            print("You do not have in states for:", states[0])
            correct = False

        if (transitionMatrix[0][1] == 0 and transitionMatrix[2][1] == 0):
            print("You do not have in states for:", states[1])
            correct = False
        
        if (transitionMatrix[0][2] == 0 and transitionMatrix[1][2] == 0):
            print("You do not have in states for:", states[2])
            correct = False
            
        #Cheking outstates:
        if (transitionMatrix[0][1] == 0 and transitionMatrix[0][2] == 0):
            print("You do not have out states for:", states[0])
            correct = False

        if (transitionMatrix[1][0] == 0 and transitionMatrix[1][2] == 0):
            print("You do not have out states for:", states[1])
            correct = False

        if (transitionMatrix[2][0] == 0 and transitionMatrix[2][1] == 0):
            print("You do not have out states for:", states[2])
            correct = False

        if correct:
            print("Congratulations, the DTMC and the probability distribution has feasible values.")

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

