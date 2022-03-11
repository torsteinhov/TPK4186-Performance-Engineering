from manager import *
from database import *
import matplotlib.pyplot as plt

class kaplanMeierEstimator:

    """
    
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

    def __init__(self, KME):
        self.KME = KME
        self.x = 0
        self.y = 0      
    
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



def kmeCalcRun():

    database = DataBase('ReliabilityData')
    database.createDatabase()
    components = database.getWorksheets().keys()
    #print(components)

    KME_components = []
    calc_components = []

    for component in components:
        
        KME_object = kaplanMeierEstimator(component, database)
        KME_components.append(KME_object)

        calc_object = Calculator(KME_object)
        calc_object.preparePlotValues()
        calc_components.append(calc_object)

        calc_object.plotKME()
        calc_object.exportKMEtofile()

#kmeCalcRun()
