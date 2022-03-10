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

class DataBase:
    
    def __init__(self):
        self.units = None
    
    def setUnitsFromExcel(self, path):

        dictionary = extractExcel(path)
        units = {}

        for key, value in dictionary.items():
            
            if key == 1:
                pass
                
            else:
                if value[1] not in units.keys():
                    units[value[1]] = [Unit(value[0], value[1], value[2], value[3], value[4])]
                else:
                    units[value[1]].append(Unit(value[0], value[1], value[2], value[3], value[4]))
        
        self.units = units

    def getUnits(self):
        return self.units

'''
test = DataBase()
test.setUnitsFromExcel('ReliabilityData/Plant1.xlsx')
units = test.getUnits()
print(units['Pressure sensor'][0].getCode())
'''

def printToExcel(DataBase):
    workbook = xlsxwriter.Workbook("Plant0.xlsx")
    worksheet = workbook.add_worksheet()

    data = DataBase.getUnits()
    worksheet.write('A1', 'Hello..')
    print('Data: ', data)
    workbook.close()



test2 = DataBase()
test2.setUnitsFromExcel('ReliabilityData/Plant1.xlsx')
printToExcel(test2)


#Writing to excel
#https://www.geeksforgeeks.org/python-create-and-write-on-excel-file-using-xlsxwriter-module/#:~:text=XlsxWriter%20is%20a%20Python%20module,conditional%20formatting%20and%20many%20others.


