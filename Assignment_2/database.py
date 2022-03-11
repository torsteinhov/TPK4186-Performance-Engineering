from manager import *
import xlsxwriter

class Unit:
        
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
        self.FailureDate = FailureDate

'''
Value: ['PRS-001-00001', 'Pressure sensor', datetime.datetime(2021, 2, 14, 14, 0), datetime.datetime(2021, 11, 15, 8, 0), None]

{2: ['PRS-001-00001', 'Pressure sensor', datetime.datetime(2021, 2, 14, 14, 0), datetime.datetime(2021, 11, 15, 8, 0), None], 
3: ['SLV-001-00001', 'Solenoid valve', datetime.datetime(2019, 6, 26, 21, 0), None, datetime.datetime(2019, 12, 17, 21, 0)], 
4: ['SLV-001-00002', 'Solenoid valve', datetime.datetime(2019, 2, 5, 19, 0), None, datetime.datetime(2019, 9, 17, 0, 0)],
 5: ['SLV-001-00003', 'Solenoid valve', datetime.datetime(2021, 6, 28, 22, 0), None, datetime.datetime(2021, 12, 5, 5, 0)],}
'''

# Task 4
class DataBase:
    


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

database = DataBase('ReliabilityData')
'''database.setUnitsFromExcel('ReliabilityData','Plant1.xlsx')
worksheets = database.getWorksheets()
print('Worksheets: ', worksheets)
database.setUnitsFromExcel('ReliabilityData','Plant2.xlsx')
worksheets = database.getWorksheets()
print('Worksheets: ', worksheets)'''
database.createDatabase()
print(database.getWorksheets())
database.printToExcel()