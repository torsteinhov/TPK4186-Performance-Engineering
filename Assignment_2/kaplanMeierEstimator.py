'''
Assignment 2 - TPK4186

Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''


from manager import *
from database import *
import matplotlib.pyplot as plt

class kaplanMeierEstimator:

    """
    A class to represent a Kaplan-Meier Estimator that records the number of surviving components in a given fleet as a function of time.
    It is recorded as a number of points (time, number-of-survivors) ordered by time.
    The class represents all data structures to store the relevant information aswell as functions to calculate and retrieve data.
    ...

    Attributes
    ----------
    component : str
        A string with the name of the folder with the .xlsx files we would like to create a database from.
    database : database_object
        A database object with all relevant data for the kaplan meier estimator class.
    sorted_durations : list
        Durations of the lifetime of different components
    KME_list : list
        A list of tuples in format (time, number-of-survivors) ordered by time. In other words, a record of the number of surviving components in a given fleet
        as a function of time.

    Methods
    -------
    getComponent(self):
        returns the string component
    getDatabase(self):
        returns the database object
    calculateDurations(self):
        takes in the worksheets dictionary, parses it and calculates the lifetime of the different components based on the in date and either the out date or the failure date.
        Sets a sorted list(ascending) of the lifetime of different units of that specific component. 
    getCalculatedDurations(self):
        returns the lifetime durations of the component.
    generateKME(self):
        iterates through the list of ascending lifetime durations and calculates tuples of the format (time, number-of-survivors).
        Sets the KME_list with these values.
    getKMElist(self):
        returns a list of all the KME tuples (time, number-of-survivors)
    """

    def __init__(self, component, database):
        
        self.component = component
        self.database = database
        self.sorted_durations = []
        self.KME_list = []
        self.calculateDurations()
        self.generateKME()


    def getComponent(self):
        return self.component
    
    def getDatabase(self):
        return self.database
    
    def calculateDurations(self):
        
        durations = []
        worksheets = self.database.getWorksheets()
        component_list = worksheets[self.component]
        
        for unit in component_list:

            date1 = dateFromString(str(unit.getInDate()))
            
            if unit.getOutDate() == None:
                date2 = dateFromString(str(unit.getFailureDate()))
            else:
                date2 = dateFromString(str(unit.getOutDate()))
            
            duration = diffDate(date1, date2)
            durations.append(duration)
        
        self.sorted_durations = sorted(durations)

    def getCalculatedDurations(self):
        return self.sorted_durations
    

    def generateKME(self):
        
        unique_durations = sorted(list(set(self.sorted_durations)))
        KME_list = []

        for durations in unique_durations:

            value = (durations, len(self.sorted_durations[self.sorted_durations.index(durations):]))
            KME_list.append(value)

        self.KME_list = KME_list
    
    def getKMElist(self):
        return self.KME_list


class Calculator:

    """
    The Calculator class is a class that takes in a component and uses the calculation and management functions of the KME class.
    With this data it calculates values for plotting a Survival Analysis using the matplotlib library.
    It is focused on keeping the Calculator class for a single component, so that it is easy to modify and supports scalability.
    ...

    Attributes
    ----------
    KME : kaplanMeierEstimator_object
        An object of the kaplanMeierEstimator class
    x : list
        A database object with all relevant data for the kaplan meier estimator class.
    sorted_durations : list
        Durations of the lifetime of different components
    KME_list : list
        A list of tuples in format (time, number-of-survivors) ordered by time. In other words, a record of the number of surviving components in a given fleet
        as a function of time.

    Methods
    -------
    getKME(self):
        returns the kaplan-Meier-Estimator object
    getX(self):
        returns the x list
    getY(self):
        returns the y list
    preparePlotValues(self):
        takes in the sorted_durations and the KME_list from the KME object, and applies calculations to these list to prepare
        them for plotting, the modified(prepared) values are stored in the x and y list.
    plotKME(self):
        Uses the matplotlib library and the component of the KME object to plot a survival analysis.
    exportKMEtofile(self):
        Same functionality as plotKME() but it also saves the plots as .png and .pdf files in a dedicated folder (/KME_analysis).
    """

    def __init__(self, KME):
        self.KME = KME
        self.x = []
        self.y = []   
    
    def getKME(self):
        return self.KME

    def preparePlotValues(self):

        sorted_durations = self.KME.getCalculatedDurations()
        KME_list = self.KME.getKMElist()

        #unique_durations
        x = sorted(list(set(sorted_durations)))

        y = []
        for tup in KME_list:
            y.append(tup[1]/len(sorted_durations))

        print('x: ', x)
        print('y: ', y)
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def plotKME(self):

        plt.plot(self.getX(), self.getY())
        plt.title('Survival Analysis: '+ self.KME.getComponent())
        plt.xlabel('lifetime [h]')
        plt.ylabel('Percent survival')
        plt.show()
    
    def exportKMEtofile(self):

        plt.plot(self.getX(), self.getY())
        plt.title('Survival Analysis: '+ self.KME.getComponent())
        plt.xlabel('lifetime [h]')
        plt.ylabel('Percent survival')
        
        
        plt.savefig('KME_analysis/survival_analysis_'+ self.KME.getComponent()+".png")
        plt.savefig('KME_analysis/survival_analysis_'+ self.KME.getComponent()+".pdf")
        plt.show()