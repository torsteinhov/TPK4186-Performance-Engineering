# Import

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import re

# Data Structure

#Task 1
class DTMC:

    """
    A class used to represent a discrete time markov chain

    ...

    Attributes
    ----------
    name : str
        a string with the name of the dtmc
    states : list
        a list of the different states the object can be in
    transitions : list
        a list of the different transitions between states that are possible

    Methods
    -------
    getName()
        gets the name of the markov chain
    setName(name)
        sets the name of the markov chain
    getStates()
        gets the states in the markov chain
    setStates(states)
        sets the states in the markov chain
    getTransitions()
        gets the transitions between states in the markov chain
    setTransitions(transitions)
        sets the transitions between states in the markov chain
    """
    
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

#Task 2
class probability_dist:

    """
    A class used to represent a probability distribution

    ...

    Attributes
    ----------
    name : str
        a string with the name of the probability distribution
    initial_state : str
        a string with the initial state
    states_probabilities : list
        a list of the different probabilites of each state

    Methods
    -------
    getName()
        gets the name of the probability distribution
    setName(name)
        sets the name of the probability distribution
    getInitialState()
        gets the initial state in the probability distribution
    setInitialState(initial_state)
        sets the initial state in the probability distribution
    getStatesProbabilities()
        gets the probabilities between states in the probability distribution
    setStatesProbabilities(states_probabilities)
        sets the probabilities between states in the probability distribution
    """

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

    def setStatesProbabilities(self, states_probabilities):
        self.states_probabilities = states_probabilities

#Task 6
class Token:

    """
    A class used to represent a token, which is the smallest individual unit in a python program.  
    They can't be used as variable names, function names, or any other random purpose.

    ...

    Attributes
    ----------
    type : str
        a string with the name of the probability distribution
    string : str
        a string with the initial state
    lineNumber : int
        an integer that keeps track of the row number of the token, if we imagine the .txt file as a grid
    columnNumber : int
        an integer that keeps track of the column number of the token, if we imagine the .txt file as a grid

    Methods
    -------
    getType()
        gets the type of the token
    setType(type)
        sets the type of the token
    getString()
        gets the string, or the value of the token
    setString(string)
        sets the string, or the value of the token
    getLineNumber()
        gets the row number of the token, if we imagine the .txt file as a grid
    setLineNumber(lineNumber)
        sets the row number of the token, if we imagine the .txt file as a grid
    getColumnNumber()
        gets the column number of the token, if we imagine the .txt file as a grid
    setColumnNumber(columnNumber)
        sets the column number of the token, if we imagine the .txt file as a grid
    """

    def __init__(self, type, string, lineNumber, columnNumber):
        self.type = type
        self.string = string
        self.lineNumber = lineNumber
        self.columnNumber = columnNumber

    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type
    
    def getString(self):
        return self.string

    def setString(self, string):
        self.string = string
    
    def getLineNumber(self):
        return self.lineNumber
    
    def setLineNumber(self, lineNumber):
        self.lineNumber = lineNumber
    
    def getColumnNumber(self):
        return self.columnNumber
    
    def setColumnNumber(self, columnNumber):
        self.columnNumber = columnNumber

#Task 3
class Manage:

    """
    A class with intention to manage sets of DTMC and probability distributions and
    implement associated management functions.

    ...

    Attributes
    ----------
    name : str
        a string with the name of the class
    dtmc : DTMC object
        a DTMC object from the class written above
    probability_dist : probability_dist object
        a probability_dist object from the class written above
    transitionMatrix : list
        a matrix consisting of the probabilities of transition between different states
    states = list
        a list of the different states the object can be in
    initial_state : str
        a string with the initial state of the probability distribution
    transitions : list
        a list of the different transitions between states that are possible
    
    

    Methods
    -------
    writeToFile()
        A function that prints a list of DTMC and a list of probability distributions into a file.
    checkMarkovChain(dtmc, probability_dist)
        A function that checks the dtmc and the probability dist for errors. Checks if the sum equals 1,
        if the initialvalues are greater than 1 and the in- and outstates.
    readFileCreateTokens(filename)
        A function that reads a text file and returns the list of tokens that consists in the file.
    calcProbDist()
        A function that calculates the product of a probability distribution by the
        sparse matrix.
    calcProbDistContinous(iterations)
        A function that, given a DTMC and an initial probability distribution,
        calculate the probability distribution and the sojourn times in each state after a
        mission of n steps.
    timeseries(numberOfIterations, currentSituation)
        A function that, given a DTMC and an initial state, generates a time series
        (a sequence of states). The next state is chosen at random from the current
        one, according to the probabilities of the transitions.
    createDTMC(timeseries)
        A function that, given a time series, creates a DTMC using the frequency
        of transitions from one state to the next one observed in the time series.


    """
    
    def __init__(self, name, dtmc, probability_dist):
        self.name=name
        self.dtmc=dtmc
        self.probability_dist=probability_dist
        self.transitionMatrix = probability_dist.getStatesProbabilites()
        self.states = dtmc.getStates()
        self.initialState = probability_dist.getInitialState()
        self.transitions=dtmc.getTransitions()
        
    #Task 5
    def writeToFile(self, filename, dtmc, probability_dist):
        states = dtmc.getStates()
        #probability_states = probability_dist.getStatesProbabilites()
        initial_state = probability_dist.getInitialState()
        try:
            with open(filename, 'w') as f:
        #f = open(filename, 'w')
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
                print("Success! Textfile """+ filename +""" has been created.""")

        except IOError as e:
            print("Couldn't write to file (%s)." % e)

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
            print("You do not have in states for:", self.states[0])
            correct = False

        if (self.transitionMatrix[0][1] == 0 and self.transitionMatrix[2][1] == 0):
            print("You do not have in states for:", self.states[1])
            correct = False
        
        if (self.transitionMatrix[0][2] == 0 and self.transitionMatrix[1][2] == 0):
            print("You do not have in states for:", self.states[2])
            correct = False

       
            
        #Checking outstates:
        if (self.transitionMatrix[0][1] == 0 and self.transitionMatrix[0][2] == 0):
            print("You do not have out states for:", self.states[0])
            correct = False

        if (self.transitionMatrix[1][0] == 0 and self.transitionMatrix[1][2] == 0):
            print("You do not have out states for:", self.states[1])
            correct = False

        if (self.transitionMatrix[2][0] == 0 and self.transitionMatrix[2][1] == 0):
            print("You do not have out states for:", self.states[2])
            correct = False

        if correct:
            print("Congratulations, the DTMC and the probability distribution has feasible values.")

    #Task 7
    def readFileCreateTokens(self, filename):

        keywords = ['and', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
                    'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
                    'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

        operators = ['+', '-', '*', '/', '%', '**', '//', '<<', '>>', '&', 
                    '|', '^', '~', '<', '<=', '>', '>=', '<>', '!=', '==']

        delimiters = ['(', ')', '[', ']', '{', '}', ',', ':', '.', '`', '=', ';', '+=', 
                    '-=', '*=', '/=', '//=', '%=', '&=', '|=', '^=', '>>=', '<<=', '**=']

        separators = [' ', '    ', '\n']

        identifiers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        tokens = []
        lines = []

        with open(filename) as f:
            for line in f:
                lines.extend([line.split()])
        

        row = 1
        for line in lines:
            col = 1
            for word in line:
                for element in word:
                    if element in separators:
                        continue
                    elif element in keywords:
                        type = 'keyword'
                    elif element in operators:
                        type = 'operator'
                    elif element in delimiters:
                        type = 'delimiter'
                    elif element in identifiers:

                        type = 'identifier'
                        if word[-1] in delimiters:
                            tokens.append(Token(type, word[:-1], row, col))
                            type = 'delimiter'
                            tokens.append(Token(type, word[-1], row, col))
                            col += len(word)
                            break
                        tokens.append(Token(type, word, row, col))
                        col += len(word)
                        break

                    tokens.append(Token(type, word, row, col))
                    col += len(word)
            row += 1
        return tokens

    # Task 8
    # Help function
    def parseTokens2DTMC(self, tokens):
        # Would like to generate a discrete time markov chain from a list of tokens

        trans = False
        transitions = {}
        states = []
        name = None

        # We need a start and end state for the transitions
        startState = None
        endState = None
        transVal = None

        numbers = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']

        for token in tokens:

            if name == None:
                name = token.string

            elif trans:
                if token.type == 'Identifiers':
                    endState = token.string
                    if endState not in states:
                        states.append(token.string)
                

                if token.type in numbers:
                    transVal = token.string

                if token.string == ';':
                    trans = False
                    transitions[(startState,endState)] = transVal
                
            elif token.columnNumber == 1:
                trans = True
                startState = token.string
                if startState not in states:
                    states.append(token.string)
            
            elif token.string == ';':

                tMatrix = np.zeros((len(states), len(states)))
                for key, tranState in transitions.items():
                    toState = key[1]
                    fromState = key[0]

                    y = states.index(toState)
                    x = states.index(fromState)

                    tMatrix[x][y] = tranState
                
            
                return DTMC(name, states, tMatrix)

    #Help function
    def parseTokens2ProbabilityDistribution(self, manage, tokens):
        # We need our manage class to connect the appropriate DTMC

        DTMC = None
        prob = False
        probList = []

        index = None
        name = None

        numbers = ['0.0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0']

        for token in tokens:
            if not prob and token.string != ';':

                if token.type in numbers:
                    name += str(token.string)
                
                elif name == None:
                    name = token.string

                elif token.type == 'identifiers' and DTMC == None:
                    dtmcName = token.string
                    for dtmc in manage.dtmc:
                        if dtmc.name == token.string:
                            DTMC = dtmc
                    
                    probList = np.zeros(len(DTMC.states))
                
                if token.columnNumber == 1:
                    prob = True
            
            if prob:
                if token.type == 'identifiers':
                    index = DTMC.states.index(token.string)
                
                if token.type in numbers:
                    probList[index] = token.string
                
                if token.string == ';':
                    prob = False
                    return probability_dist(name=name, initial_state=DTMC, states_probabilities=probList)
        
    def parser(self, tokens):

        '''
        Creates DTMC's and probability distributions by parsing a list of tokens,
        utilizes the help functions parseTokens2ProbabilityDistribution(self, manage, tokens)
        and parseTokens2DTMC(self, tokens).
        '''




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
        print("After " + str(it) + " iterations the probability distribution converged. The probability distribution is: \n" + str(prob))    
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
    def timeseries(self, numberOfIterations, currentSituation):  #SE OVER OG RYDDE LITT

        #print("Start state: "+ str(self.states[0]))
        timeseries = []

        for i in range(numberOfIterations):
            
            if currentSituation==self.states[0]:
                
                nextStateOptions= ([self.states[0]]*int((seaConditionProbability.getStatesProbabilites()[0][0])*10)+
                [self.states[1]]*int(seaConditionProbability.getStatesProbabilites()[0][1]*10))
               
                change=random.choice(nextStateOptions)
            elif currentSituation==self.states[1]:

                nextStateOptions= ([self.states[0]]*int((seaConditionProbability.getStatesProbabilites()[1][0])*10)+ 
                [self.states[1]]*int(seaConditionProbability.getStatesProbabilites()[1][1]*10)+ 
                [self.states[2]]*int(seaConditionProbability.getStatesProbabilites()[1][2]*10))

                change=random.choice(nextStateOptions)
            
            elif currentSituation==self.states[2]:

                nextStateOptions=([self.states[2]]*int((seaConditionProbability.getStatesProbabilites()[2][2])*10)+
                [self.states[1]]*int(seaConditionProbability.getStatesProbabilites()[2][1]*10))
 
                change=random.choice(nextStateOptions)

            else:
                print("Check input")
   
            timeseries.append(change)
            currentSituation=change

        print("After "+str(numberOfIterations)+" sequenses of states we end up with the follow timeseries: ")
        return timeseries
    
    
                    
    #Task 13

    def createDTMC(self, timeseries):

        matrix = []
        sequence = []
        duos = []
        for uniqeStates in self.states:
            for i in range(len(timeseries)-1):
                if timeseries[i]==uniqeStates and [timeseries[i]]+[timeseries[i+1]] not in duos:
                    duos.append([timeseries[i]]+[timeseries[i+1]])
        
        #appearences:  {'CALM': #, 'MODERATE': #, 'ROUGH': #}
        appearences = {self.states[0]: 0, self.states[1]: 0, self.states[2]: 0}
        for duo in duos:
            for i in range(len(timeseries)-1):
                if [timeseries[i]]+[timeseries[i+1]]==duo:
                    appearences[duo[0]] += 1
        

        for duo in duos:
            for i in range(len(timeseries)-1):
                if [timeseries[i]]+[timeseries[i+1]]==duo:
                    sequence.append(duo)
            matrix.append(sequence)
            duo.append(len(sequence))
            duo.append(len(sequence)/appearences[duo[0]])
            sequence = []

        
        return duos
    
    # Task 14
    def determineLengthSeries(self, startState):
        # An experimental study of determining the length of a timeseries to get an offset of <= 1%

        # First we try with 15 iterations of timeseries
        startTimeseries = self.timeseries(15, startState)
        startDtmc = self.createDTMC(startTimeseries)

        #print('15 iterations Timeseries ', startTimeseries)
        print('15 iterations dtmc: ', startDtmc)

        # Second we try with 50 iterations of timeseries
        secondTimeseries = self.timeseries(50, startState)
        secondDtmc = self.createDTMC(startTimeseries)

        #print('50 iterations Timeseries ', secondTimeseries)
        print('50 iterations dtmc: ', secondDtmc)

        # Third we try with 100 iterations of timeseries
        thirdTimeseries = self.timeseries(100, startState)
        thirdDtmc = self.createDTMC(thirdTimeseries)

        #print('100 iterations Timeseries ', thirdTimeseries)
        print('100 iterations dtmc: ', thirdDtmc)

        # Fourth we try with 300 iterations of timeseries
        fourthTimeseries = self.timeseries(300, startState)
        fourthDtmc = self.createDTMC(fourthTimeseries)

        #print('300 iterations Timeseries ', fourthTimeseries)
        print('300 iterations dtmc: ', fourthDtmc)

        # Finally we try with 50000 iterations of timeseries
        finalTimeseries = self.timeseries(50000, startState)
        finalDtmc = self.createDTMC(finalTimeseries)

        #print('50000 iterations Timeseries ', finalTimeseries)
        print('50000 iterations dtmc: ', finalDtmc)

                    
"""
Below we will test the different tasks.  

We will first setup the DTMC and the sea condition probability.

"""
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



"""
Test task 1,2,3 and 4:
"""
print("Task 1,2,3 and 4:")
print(seaCondition.getName())
print(seaCondition.getStates())
print(seaCondition.getTransitions())

print(seaConditionProbability.getName())
print(seaConditionProbability.getInitialState())
print(seaConditionProbability.getStatesProbabilites())

seaConditionManage = Manage('seaCondition', seaCondition, seaConditionProbability)



print("\n")

"""
Test task 5:
"""
print("Task 5:")
seaConditionManage.writeToFile('seaCondition.txt', seaCondition, seaConditionProbability)
print("\n")

"""
Test task 6:
"""


"""
Test task 7:
"""
print("Task 7:")
tokens = seaConditionManage.readFileCreateTokens('seaCondition.txt')
for element in tokens:
    print([element.type, element.string, element.lineNumber, element.columnNumber])
print("\n")

"""
Test task 8:
"""
print("Task 8:")
print(seaConditionManage.parseTokens2DTMC(tokens))
print(seaConditionManage.parseTokens2ProbabilityDistribution(seaCondition, tokens))
print('\n')

"""
Test task 9:
"""
print("Task 9:")
seaConditionManage.checkMarkovChain(seaCondition, seaConditionProbability)
print("\n")


"""
Test task 10:
"""
print("Task 10:")
seaConditionManage.calcProbDist()
print("\n")


"""
Test task 11:
"""
print("Task 11:")
seaConditionManage.calcProbDistContinous(5)
print("\n")


"""
Test task 12:
"""
print("Task 12:")
timeseries = seaConditionManage.timeseries(50, "CALM")
print("\n")


"""
Test task 13:
"""
print("Task 13:")
print(seaConditionManage.createDTMC(timeseries))
print("\n")

"""
Test task 14:
"""
print("Task 14:")
seaConditionManage.determineLengthSeries("CALM")
print("\n")