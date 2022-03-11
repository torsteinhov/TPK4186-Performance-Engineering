from manager import *
from database import *
import matplotlib.pyplot as plt

class kaplanMeierEstimator:
    def __init__(self, component, database):
        
        self.component = component
        self.database = database
        self.sorted_durations = 0
        self.KME_list = 0
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
