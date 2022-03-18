'''
Assignment 2 - TPK4186

Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from manager import *
from database import *
from kaplanMeierEstimator import *
from reportGenerator import *
import unittest

class Test(unittest.TestCase):

    def test_task1(self): 

        #Test task 1
        print("\n")
        print("Task 1:")
         #Choose your own folder, if needed.
        self.assertEqual(listFilesInFolder('ReliabilityData'),['Plant1.xlsx', 'Plant10.xlsx', 'Plant100.xlsx', 'Plant101.xlsx', 'Plant102.xlsx', 'Plant103.xlsx', 'Plant104.xlsx', 'Plant105.xlsx', 'Plant106.xlsx', 'Plant107.xlsx', 'Plant108.xlsx', 'Plant109.xlsx', 'Plant11.xlsx', 'Plant110.xlsx', 'Plant111.xlsx', 'Plant112.xlsx', 'Plant113.xlsx', 'Plant114.xlsx', 'Plant115.xlsx', 'Plant116.xlsx', 'Plant117.xlsx', 'Plant118.xlsx', 'Plant119.xlsx', 'Plant12.xlsx', 'Plant120.xlsx', 'Plant121.xlsx', 'Plant122.xlsx', 'Plant123.xlsx', 'Plant13.xlsx', 'Plant14.xlsx', 'Plant15.xlsx', 'Plant16.xlsx', 'Plant17.xlsx', 'Plant18.xlsx', 'Plant19.xlsx', 'Plant2.xlsx', 'Plant20.xlsx', 'Plant21.xlsx', 'Plant22.xlsx', 'Plant23.xlsx', 'Plant24.xlsx', 'Plant25.xlsx', 'Plant26.xlsx', 'Plant27.xlsx', 'Plant28.xlsx', 'Plant29.xlsx', 'Plant3.xlsx', 'Plant30.xlsx', 'Plant31.xlsx', 'Plant32.xlsx', 'Plant33.xlsx', 'Plant34.xlsx', 'Plant35.xlsx', 'Plant36.xlsx', 'Plant37.xlsx', 'Plant38.xlsx', 'Plant39.xlsx', 'Plant4.xlsx', 'Plant40.xlsx', 'Plant41.xlsx', 'Plant42.xlsx', 'Plant43.xlsx', 'Plant44.xlsx', 'Plant45.xlsx', 'Plant46.xlsx', 'Plant47.xlsx', 'Plant48.xlsx', 'Plant49.xlsx', 'Plant5.xlsx', 'Plant50.xlsx', 'Plant51.xlsx', 'Plant52.xlsx', 'Plant53.xlsx', 'Plant54.xlsx', 'Plant55.xlsx', 'Plant56.xlsx', 'Plant57.xlsx', 'Plant58.xlsx', 'Plant59.xlsx', 
        'Plant6.xlsx', 'Plant60.xlsx', 'Plant61.xlsx', 'Plant62.xlsx', 'Plant63.xlsx', 'Plant64.xlsx', 'Plant65.xlsx', 'Plant66.xlsx', 'Plant67.xlsx', 'Plant68.xlsx', 'Plant69.xlsx', 'Plant7.xlsx', 'Plant70.xlsx', 'Plant71.xlsx', 'Plant72.xlsx', 'Plant73.xlsx', 'Plant74.xlsx', 'Plant75.xlsx', 'Plant76.xlsx', 'Plant77.xlsx', 'Plant78.xlsx', 'Plant79.xlsx', 'Plant8.xlsx', 'Plant80.xlsx', 'Plant81.xlsx', 'Plant82.xlsx', 'Plant83.xlsx', 'Plant84.xlsx', 'Plant85.xlsx', 'Plant86.xlsx', 'Plant87.xlsx', 'Plant88.xlsx', 'Plant89.xlsx', 'Plant9.xlsx', 'Plant90.xlsx', 'Plant91.xlsx', 'Plant92.xlsx', 'Plant93.xlsx', 'Plant94.xlsx', 'Plant95.xlsx', 'Plant96.xlsx', 'Plant97.xlsx', 'Plant98.xlsx', 'Plant99.xlsx'])

    def test_task2(self):
        #Test task 2:
        print("\n")
        print("Task 2:")
        #print(extractExcel('ReliabilityData/Plant1.xlsx')) #Choose your own path, if needed
        self.assertEqual(str(extractExcel('ReliabilityData/Plant1.xlsx')),  
            "{1: ['Code', 'Description', 'In-Service Date', 'Out-Service Date', 'Failure Date']," 
            +" 2: ['PRS-001-00001', 'Pressure sensor', datetime.datetime(2021, 2, 14, 14, 0), datetime.datetime(2021, 11, 15, 8, 0), None],"
            +" 3: ['SLV-001-00001', 'Solenoid valve', datetime.datetime(2019, 6, 26, 21, 0), None, datetime.datetime(2019, 12, 17, 21, 0)],"
            +" 4: ['SLV-001-00002', 'Solenoid valve', datetime.datetime(2019, 2, 5, 19, 0), None, datetime.datetime(2019, 9, 17, 0, 0)],"
            +" 5: ['SLV-001-00003', 'Solenoid valve', datetime.datetime(2021, 6, 28, 22, 0), None, datetime.datetime(2021, 12, 5, 5, 0)],"
            +" 6: ['MP3-001-00001', 'Motor pump type 3', datetime.datetime(2019, 7, 23, 17, 0), None, datetime.datetime(2020, 3, 23, 15, 0)],"
            +" 7: ['AQM-001-00001', 'Acquisition module', datetime.datetime(2021, 11, 29, 5, 0), datetime.datetime(2022, 8, 29, 23, 0), None],"
            +" 8: ['AQM-001-00002', 'Acquisition module', datetime.datetime(2021, 8, 2, 9, 0), datetime.datetime(2022, 5, 3, 3, 0), None],"
            +" 9: ['VBS-001-00001', 'Vibration sensor', datetime.datetime(2018, 2, 18, 17, 0), None, datetime.datetime(2018, 2, 21, 8, 0)],"
            +" 10: ['AQM-001-00003', 'Acquisition module', datetime.datetime(2017, 8, 11, 5, 0), None, datetime.datetime(2017, 8, 22, 12, 0)],"
            +" 11: ['LGS-001-00001', 'Logic solver', datetime.datetime(2018, 6, 14, 5, 0), datetime.datetime(2019, 6, 14, 5, 0), None], 12: ['LGS-001-00002', 'Logic solver', datetime.datetime(2021, 9, 13, 22, 0), datetime.datetime(2022, 9, 13, 22, 0), None], 13: ['TPS-001-00001', 'Temperature sensor', datetime.datetime(2021, 8, 13, 13, 0), datetime.datetime(2022, 5, 14, 7, 0), None], 14: ['MP3-001-00002', 'Motor pump type 3', datetime.datetime(2018, 5, 19, 14, 0), None, datetime.datetime(2018, 5, 27, 19, 0)], 15: ['TPS-001-00002', 'Temperature sensor', datetime.datetime(2019, 1, 11, 7, 0), datetime.datetime(2019, 10, 12, 1, 0), None], 16: ['VBS-001-00002', 'Vibration sensor', datetime.datetime(2017, 9, 9, 13, 0), datetime.datetime(2018, 6, 10, 7, 0), None], 17: ['VBS-001-00003', 'Vibration sensor', datetime.datetime(2020, 2, 14, 7, 0), datetime.datetime(2020, 11, 14, 1, 0), None], 18: ['SLV-001-00004', 'Solenoid valve', datetime.datetime(2019, 3, 1, 0, 0), datetime.datetime(2020, 2, 29, 0, 0), None], 19: ['SDV-001-00001', 'Shutdown valve', datetime.datetime(2017, 5, 8, 6, 0), None, datetime.datetime(2017, 7, 16, 13, 0)], 20: ['MP3-001-00003', 'Motor pump type 3', datetime.datetime(2021, 2, 25, 6, 0), None, datetime.datetime(2021, 10, 31, 1, 0)], 21: ['AQM-001-00004', 'Acquisition module', datetime.datetime(2018, 1, 30, 17, 0), datetime.datetime(2018, 10, 31, 11, 0), None], 22: ['AQM-001-00005', 'Acquisition module', datetime.datetime(2021, 12, 23, 2, 0), datetime.datetime(2022, 9, 22, 20, 0), None], 23: ['MP1-001-00001', 'Motor pump type 1', datetime.datetime(2018, 3, 29, 6, 0), None, datetime.datetime(2018, 8, 6, 12, 0)], 24: ['LGS-001-00003', 'Logic solver', datetime.datetime(2018, 8, 15, 20, 0), None, datetime.datetime(2018, 11, 19, 23, 0)], 25: ['SLV-001-00005', 'Solenoid valve', datetime.datetime(2020, 8, 7, 19, 0), datetime.datetime(2021, 8, 7, 19, 0), None], 26: ['MP3-001-00004', 'Motor pump type 3', datetime.datetime(2021, 3, 29, 2, 0), datetime.datetime(2022, 3, 29, 2, 0), None], 27: ['VBS-001-00004', 'Vibration sensor', datetime.datetime(2019, 4, 8, 13, 0), None, datetime.datetime(2019, 4, 8, 15, 0)], 28: ['MP2-001-00001', 'Motor pump type 2', datetime.datetime(2019, 1, 14, 5, 0), None, datetime.datetime(2019, 12, 8, 15, 0)], 29: ['LGS-001-00004', 'Logic solver', datetime.datetime(2021, 6, 26, 18, 0), datetime.datetime(2022, 6, 26, 18, 0), None], 30: ['MP1-001-00002', 'Motor pump type 1', datetime.datetime(2018, 9, 29, 16, 0), None, datetime.datetime(2019, 2, 16, 13, 0)], 31: ['LGS-001-00005', 'Logic solver', datetime.datetime(2017, 1, 12, 10, 0), None, datetime.datetime(2017, 4, 11, 4, 0)], 32: ['VBS-001-00005', 'Vibration sensor', datetime.datetime(2017, 2, 6, 22, 0), None, datetime.datetime(2017, 10, 27, 16, 0)], 33: ['VBS-001-00006', 'Vibration sensor', datetime.datetime(2020, 2, 22, 9, 0), None, datetime.datetime(2020, 10, 29, 16, 0)], 34: ['VBS-001-00007', 'Vibration sensor', datetime.datetime(2018, 1, 24, 14, 0), None, datetime.datetime(2018, 3, 13, 12, 0)], 35: ['MP2-001-00002', 'Motor pump type 2', datetime.datetime(2019, 7, 3, 18, 0), None, datetime.datetime(2019, 9, 21, 20, 0)], 36: ['MP3-001-00005', 'Motor pump type 3', datetime.datetime(2020, 2, 23, 20, 0), None, datetime.datetime(2020, 2, 28, 21, 0)], 37: ['MP1-001-00003', 'Motor pump type 1', datetime.datetime(2021, 12, 9, 13, 0), None, datetime.datetime(2022, 5, 6, 10, 0)], 38: ['MP3-001-00006', 'Motor pump type 3', datetime.datetime(2020, 11, 1, 1, 0), None, datetime.datetime(2020, 12, 20, 11, 0)], 39: ['VBS-001-00008', 'Vibration sensor', datetime.datetime(2018, 3, 10, 10, 0), datetime.datetime(2018, 12, 9, 4, 0), None], 40: ['AQM-001-00006', 'Acquisition module', datetime.datetime(2018, 10, 7, 3, 0), datetime.datetime(2019, 7, 7, 21, 0), None], 41: ['VBS-001-00009', 'Vibration sensor', datetime.datetime(2017, 12, 9, 0, 0), datetime.datetime(2018, 9, 8, 18, 0), None], 42: ['VBS-001-00010', 'Vibration sensor', datetime.datetime(2021, 4, 9, 12, 0), datetime.datetime(2022, 1, 8, 6, 0), None], 43: ['SDV-001-00002', 'Shutdown valve', datetime.datetime(2017, 6, 5, 5, 0), datetime.datetime(2018, 6, 5, 5, 0), None], 44: ['SDV-001-00003', 'Shutdown valve', datetime.datetime(2021, 2, 4, 13, 0), None, datetime.datetime(2021, 11, 21, 17, 0)], 45: ['MP2-001-00003', 'Motor pump type 2', datetime.datetime(2019, 6, 12, 14, 0), datetime.datetime(2020, 6, 11, 14, 0), None], 46: ['SLV-001-00006', 'Solenoid valve', datetime.datetime(2020, 2, 21, 13, 0), datetime.datetime(2021, 2, 20, 13, 0), None], 47: ['MP2-001-00004', 'Motor pump type 2', datetime.datetime(2017, 11, 16, 5, 0), None, datetime.datetime(2018, 6, 7, 2, 0)], 48: ['AQM-001-00007', 'Acquisition module', datetime.datetime(2017, 2, 17, 4, 0), datetime.datetime(2017, 11, 17, 22, 0), None], 49: ['MP1-001-00004', 'Motor pump type 1', datetime.datetime(2019, 5, 17, 0, 0), None, datetime.datetime(2019, 7, 6, 0, 0)], 50: ['MP2-001-00005', 'Motor pump type 2', datetime.datetime(2021, 4, 1, 13, 0), None, datetime.datetime(2021, 10, 6, 1, 0)], 51: ['SLV-001-00007', 'Solenoid valve', datetime.datetime(2019, 4, 7, 6, 0), None, datetime.datetime(2019, 7, 4, 6, 0)], 52: ['MP2-001-00006', 'Motor pump type 2', datetime.datetime(2021, 7, 21, 10, 0), None, datetime.datetime(2022, 6, 9, 6, 0)], 53: ['PRS-001-00002', 'Pressure sensor', datetime.datetime(2020, 8, 29, 6, 0), datetime.datetime(2021, 5, 30, 0, 0), None], 54: ['LGS-001-00006', 'Logic solver', datetime.datetime(2021, 4, 11, 23, 0), None, datetime.datetime(2021, 4, 11, 23, 0)], 55: ['TPS-001-00003', 'Temperature sensor', datetime.datetime(2018, 12, 7, 19, 0), None, datetime.datetime(2018, 12, 14, 14, 0)], 56: ['PRS-001-00003', 'Pressure sensor', datetime.datetime(2021, 1, 21, 3, 0), None, datetime.datetime(2021, 6, 29, 5, 0)], 57: ['MP3-001-00007', 'Motor pump type 3', datetime.datetime(2017, 4, 3, 14, 0), datetime.datetime(2018, 4, 3, 14, 0), None], 58: ['TPS-001-00004', 'Temperature sensor', datetime.datetime(2018, 12, 28, 15, 0), datetime.datetime(2019, 9, 28, 9, 0), None], 59: ['SDV-001-00004', 'Shutdown valve', datetime.datetime(2020, 5, 6, 18, 0), datetime.datetime(2021, 5, 6, 18, 0), None], 60: ['MP1-001-00005', 'Motor pump type 1', datetime.datetime(2021, 3, 3, 15, 0), None, datetime.datetime(2021, 9, 9, 5, 0)], 61: ['LGS-001-00007', 'Logic solver', datetime.datetime(2020, 4, 25, 21, 0), None, datetime.datetime(2020, 12, 23, 7, 0)], 62: ['MP3-001-00008', 'Motor pump type 3', datetime.datetime(2017, 11, 12, 23, 0), None, datetime.datetime(2017, 12, 20, 20, 0)], 63: ['MP3-001-00009', 'Motor pump type 3', datetime.datetime(2020, 7, 27, 16, 0), None, datetime.datetime(2021, 5, 8, 6, 0)], 64: ['PRS-001-00004', 'Pressure sensor', datetime.datetime(2019, 3, 8, 11, 0), datetime.datetime(2019, 12, 7, 5, 0), None], 65: ['PRS-001-00005', 'Pressure sensor', datetime.datetime(2020, 4, 7, 8, 0), datetime.datetime(2021, 1, 6, 2, 0), None], 66: ['PRS-001-00006', 'Pressure sensor', datetime.datetime(2017, 9, 3, 22, 0), None, datetime.datetime(2018, 1, 11, 19, 0)], 67: ['MP3-001-00010', 'Motor pump type 3', datetime.datetime(2019, 8, 5, 4, 0), None, datetime.datetime(2020, 5, 17, 13, 0)], 68: ['VBS-001-00011', 'Vibration sensor', datetime.datetime(2017, 10, 28, 0, 0), datetime.datetime(2018, 7, 28, 18, 0), None], 69: ['MP1-001-00006', 'Motor pump type 1', datetime.datetime(2017, 6, 15, 0, 0), None, datetime.datetime(2017, 12, 23, 0, 0)], 70: ['MP3-001-00011', 'Motor pump type 3', datetime.datetime(2020, 6, 24, 19, 0), None, datetime.datetime(2021, 3, 28, 0, 0)], 71: ['AQM-001-00008', 'Acquisition module', datetime.datetime(2017, 6, 16, 3, 0), None, datetime.datetime(2017, 6, 22, 10, 0)], 72: ['VBS-001-00012', 'Vibration sensor', datetime.datetime(2021, 12, 22, 11, 0), None, datetime.datetime(2022, 9, 2, 5, 0)], 73: ['SDV-001-00005', 'Shutdown valve', datetime.datetime(2017, 9, 4, 20, 0), None, datetime.datetime(2018, 6, 29, 5, 0)], 74: ['VBS-001-00013', 'Vibration sensor', datetime.datetime(2017, 3, 22, 4, 0), datetime.datetime(2017, 12, 20, 22, 0), None], 75: ['VBS-001-00014', 'Vibration sensor', datetime.datetime(2018, 6, 24, 14, 0), datetime.datetime(2019, 3, 25, 8, 0), None], 76: ['PRS-001-00007', 'Pressure sensor', datetime.datetime(2019, 9, 19, 15, 0), datetime.datetime(2020, 6, 19, 9, 0), None], 77: ['SDV-001-00006', 'Shutdown valve', datetime.datetime(2020, 3, 6, 15, 0), datetime.datetime(2021, 3, 6, 15, 0), None], 78: ['SDV-001-00007', 'Shutdown valve', datetime.datetime(2020, 2, 8, 2, 0), None, datetime.datetime(2020, 2, 16, 19, 0)], 79: ['TPS-001-00005', 'Temperature sensor', datetime.datetime(2020, 8, 7, 4, 0), None, datetime.datetime(2020, 9, 21, 2, 0)], 80: ['PRS-001-00008', 'Pressure sensor', datetime.datetime(2020, 3, 18, 21, 0), datetime.datetime(2020, 12, 17, 15, 0), None], 81: ['PRS-001-00009', 'Pressure sensor', datetime.datetime(2020, 7, 20, 18, 0), datetime.datetime(2021, 4, 20, 12, 0), None], 82: ['MP2-001-00007', 'Motor pump type 2', datetime.datetime(2020, 4, 3, 12, 0), datetime.datetime(2021, 4, 3, 12, 0), None], 83: ['TPS-001-00006', 'Temperature sensor', datetime.datetime(2021, 5, 22, 6, 0), datetime.datetime(2022, 2, 20, 0, 0), None], 84: ['MP3-001-00012', 'Motor pump type 3', datetime.datetime(2021, 11, 19, 6, 0), None, datetime.datetime(2022, 4, 3, 7, 0)], 85: ['MP3-001-00013', 'Motor pump type 3', datetime.datetime(2018, 10, 2, 0, 0), datetime.datetime(2019, 10, 2, 0, 0), None], 86: ['SDV-001-00008', 'Shutdown valve', datetime.datetime(2019, 1, 19, 5, 0), None, datetime.datetime(2019, 10, 13, 10, 0)], 87: ['LGS-001-00008', 'Logic solver', datetime.datetime(2021, 10, 29, 2, 0), datetime.datetime(2022, 10, 29, 2, 0), None], 88: ['MP3-001-00014', 'Motor pump type 3', datetime.datetime(2017, 4, 1, 8, 0), None, datetime.datetime(2017, 6, 6, 23, 0)], 89: ['VBS-001-00015', 'Vibration sensor', datetime.datetime(2020, 2, 5, 1, 0), datetime.datetime(2020, 11, 4, 19, 0), None]," 
            +" 90: ['LGS-001-00009', 'Logic solver', datetime.datetime(2017, 3, 29, 11, 0), datetime.datetime(2018, 3, 29, 11, 0), None], 91: ['MP1-001-00007', 'Motor pump type 1', datetime.datetime(2019, 6, 21, 18, 0), datetime.datetime(2020, 6, 20, 18, 0), None], 92: ['LGS-001-00010', 'Logic solver', datetime.datetime(2021, 3, 21, 23, 0), datetime.datetime(2022, 3, 21, 23, 0), None], 93: ['MP3-001-00015', 'Motor pump type 3', datetime.datetime(2019, 4, 12, 0, 0), None, datetime.datetime(2019, 7, 4, 11, 0)], 94: ['SDV-001-00009', 'Shutdown valve', datetime.datetime(2018, 8, 13, 14, 0), datetime.datetime(2019, 8, 13, 14, 0), None], 95: ['LGS-001-00011', 'Logic solver', datetime.datetime(2018, 4, 13, 4, 0), datetime.datetime(2019, 4, 13, 4, 0), None], 96: ['SLV-001-00008', 'Solenoid valve', datetime.datetime(2018, 11, 6, 12, 0), None, datetime.datetime(2019, 4, 15, 19, 0)], 97: ['AQM-001-00009', 'Acquisition module', datetime.datetime(2021, 3, 1, 19, 0), datetime.datetime(2021, 11, 30, 13, 0), None], 98: ['SDV-001-00010', 'Shutdown valve', datetime.datetime(2017, 4, 4, 14, 0), datetime.datetime(2018, 4, 4, 14, 0), None], 99: ['MP3-001-00016', 'Motor pump type 3', datetime.datetime(2017, 2, 27, 2, 0), None, datetime.datetime(2018, 2, 13, 11, 0)], 100: ['PRS-001-00010', 'Pressure sensor', datetime.datetime(2019, 11, 27, 19, 0), datetime.datetime(2020, 8, 27, 13, 0), None], 101: ['TPS-001-00007', 'Temperature sensor', datetime.datetime(2017, 5, 24, 15, 0), datetime.datetime(2018, 2, 22, 9, 0), None]}") 
        

    def test_task3(self):
        
        # Test task 3
        print("\n")
        print("Task 3:")
    
        #Setting up two dates to test. Should be 48 hours
        date1 = dateFromString('2021-02-14  14:00:00')
        date2 = dateFromString('2021-02-16  14:00:00')

        self.assertEqual(str(diffDate(date1, date2)), '48.0') 
        
    
    
    def test_task4(self):

        #Test task 4:
        print('\n')
        print('Task 4:')
        database = DataBase('ReliabilityData')
        database.createDatabase()
        unit = database.getWorksheets()['Pressure sensor'][0]
        
        self.assertEqual(str(unit.getCode()), 'PRS-001-00001') 
        self.assertEqual(str(unit.getDescription()), 'Pressure sensor') 
        self.assertEqual(str(unit.getInDate()), '2021-02-14 14:00:00') 
        self.assertEqual(str(unit.getOutDate()), '2021-11-15 08:00:00') 
        self.assertEqual(str(unit.getFailureDate()), 'None') 

        date1 = dateFromString('2021-02-14  14:00:00')
        date2 = dateFromString('2021-02-16  14:00:00')
        unit2 = Unit("TEST", "TEST DEVICE",date1,date2,None )
        self.assertEqual(str(unit2.getCode()), 'TEST') 
        self.assertEqual(str(unit2.getDescription()), 'TEST DEVICE') 
        self.assertEqual(str(unit2.getInDate()), '2021-02-14 14:00:00') 
        self.assertEqual(str(unit2.getOutDate()), '2021-02-16 14:00:00') 
        self.assertEqual(str(unit2.getFailureDate()), 'None')

        #Testing set-methods
        unit2.setCode('TESTOK')
        self.assertEqual(str(unit2.getCode()), 'TESTOK')
        
        unit2.setDescription('TESTOK')
        self.assertEqual(str(unit2.getDescription()), 'TESTOK')

        unit2.setInDate(dateFromString('2021-02-10  14:00:00'))
        self.assertEqual(str(unit2.getInDate()), '2021-02-10 14:00:00') 

        unit2.setOutDate(dateFromString('2021-02-20  13:00:00'))
        self.assertEqual(str(unit2.getOutDate()), '2021-02-20 13:00:00') 

        unit2.setFailureDate(dateFromString('2021-02-25  15:00:00'))
        self.assertEqual(str(unit2.getFailureDate()), '2021-02-25 15:00:00')


'''
THE REST OF THE TESTS IS NOT RELEVANT TO USE ASSERTEQUAL SINCE IT PRODUCES FILES OF FORMAT .xlsx and .html
WE THEREFORE MOVE THEM OUT OF THE TEST CLASS
'''

def test_task5():
    #Test task 5:
    database = DataBase('ReliabilityData')
    database.createDatabase()
    database.printToExcel() #A new file should be created

def test_task678():

    #Test task 6, 7 and 8:
    
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

    kmeCalcRun()

def test_task9():
    #Test task 9:

    def reportGeneratorRun():

        database = DataBase('ReliabilityData')
        database.createDatabase()

        KME = kaplanMeierEstimator('Vibration sensor', database)
        calc = Calculator(KME)

        reportGenerator = ReportGenerator(database, KME, calc)
        reportGenerator.writeHTML()
        
    reportGeneratorRun()

test_task5()
test_task678()
test_task9()

if __name__ == "__main__":
    unittest.main()
