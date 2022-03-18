'''
Assignment 2 - TPK4186

Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from manager import *
import xlsxwriter

class Unit:

    """
    A class used to represent a Unit, which is a row in the excel worksheets with different attributes like code, description, dates and etc.
    Used by the Database class to create dictionaries based on the components.
    ...

    Attributes
    ----------
    code : str
        String with the code id of the component
    description : str
        A description of the component
    inDate : datetime_object
        The date the component was set in service.
    outDate : datetime_object
        The date the component was taken out of service.
    failureDate : datetime_object
        The date the component failed, and had to be taken out of service.

    Methods
    -------
    def getCode(self):
        gets the code
    def setCode(self, code):
        sets the code
    def getDescription(self):
        gets the description
    def setDescription(self, description):
        sets the description
    def getInDate(self):
        gets the In Date
    def setInDate(self, inDate):
        sets the In Date
    def getOutDate(self):
        gets the Out Date
    def setOutDate(self, outDate):
        sets the Out Date
    def getFailureDate(self):
        gets the FailureDate
    def setFailureDate(self, FailureDate):
        sets the Failure Date
    """
        
    def __init__(self, code, description, inDate, outDate, failureDate):
        self.code = code
        self.description = description
        self.inDate = inDate
        self.outDate = outDate
        self.failureDate = failureDate

    def getCode(self):
        return self.code
    
    def setCode(self, code):
        self.code = code
    
    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description
    
    def getInDate(self):
        return self.inDate
    
    def setInDate(self, inDate):
        self.inDate = inDate

    def getOutDate(self):
        return self.outDate

    def setOutDate(self, outDate):
        self.outDate = outDate
    
    def getFailureDate(self):
        return self.failureDate

    def setFailureDate(self, FailureDate):
        self.failureDate = FailureDate

# Task 4
class DataBase:
    
    """
    A class to store all Reliabilitydata in an easy to access format. Contains multiple functionalities that parses the worksheets and stores it in the database.
    Some of this functionality could have been initiated in the __init__ function, but for extendability reasons we wanted to leave this as an optional function.
    ...

    Attributes
    ----------
    folder : str
        A string with the name of the folder with the .xlsx files we would like to create a database from.
    worksheets : dictionary
        A dictionary of the data in all the worksheets, after processed, contains all components as keys and all the associating data as value in list format.
        {component: [reliability_data..]}

    Methods
    -------
    def setUnitsFromExcel(self, path):
        uses the extractExcel() function to read the excel worksheets and extract it in a dictionary format. Parses this dictionary format to return a new dictionary
        with format {component: [units..]}. A format that stores all units for each type of component.
    def createDatabase(self):
        Initializes the database and runs the setUnitsFromExcel on all the worksheet files in the folder, which is collected with the listFilesInFolder() functions.
        Sets the worksheets of the database equal to all the data in all the excel files, parsed and finalized as in the setUnitsFromExcel() function.
    def printToExcel(self):
        Iterates through the parsed dictionary and prints to an excel file sorted on each component.
    """

    def __init__(self, folder):
        self.folder = folder
        self.worksheets = {}
    
    def getWorksheets(self):
        return self.worksheets
    
    # Task 4
    def setUnitsFromExcel(self, path):
        
        units = {}
        dictionary = extractExcel(self.folder+'/'+path)
        
        for key, value in dictionary.items():
            
            if key == 1:
                pass
                
            else:
                if value[1] not in units.keys():
                    units[value[1]] = [Unit(value[0], value[1], value[2], value[3], value[4])]
                else:
                    units[value[1]].append(Unit(value[0], value[1], value[2], value[3], value[4]))
                    
        for key, value in units.items():
            if key in self.worksheets:
                self.worksheets[key].extend(value)
            else:
                self.worksheets[key] = value
        
    
    def createDatabase(self):
        
        files = listFilesInFolder(self.folder)
        #print('FILES: ', files)

        for excel_file in files:
            self.setUnitsFromExcel(excel_file)

    # Task 5
    def printToExcel(self):
        workbook = xlsxwriter.Workbook(self.folder+"_database.xlsx")
        write_worksheet = workbook.add_worksheet()
        
        write_worksheet.write('A1', 'Code')
        write_worksheet.write('B1', 'Description')
        write_worksheet.write('C1', 'In-Service Date')
        write_worksheet.write('D1', 'Out-Service Date')
        write_worksheet.write('E1', 'Failure Date')

        worksheets = self.getWorksheets()
        col = 0
        row = 1
        
        #  {'Pressure sensor': [<__main__.Unit object at 0x7f30ed16c5d0>, <__main__.Unit object at 0x7f30ed2161d0>, <__main__.Unit object at 0x7f30ed2160d0>]}
        for key, value in worksheets.items():
            for unit in value:
                write_worksheet.write(row,col,unit.getCode())
                write_worksheet.write(row,col+1,unit.getDescription())
                write_worksheet.write(row,col+2,unit.getInDate())
                write_worksheet.write(row,col+3,unit.getOutDate())
                write_worksheet.write(row,col+4,unit.getFailureDate())
                col=0
                row+=1

        print('worksheets: ', worksheets)
        workbook.close()