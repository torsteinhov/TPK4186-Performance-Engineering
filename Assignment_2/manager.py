import os
from openpyxl import load_workbook
from datetime import datetime


def listFilesInFolder(path):

    files = os.listdir(path)

    files_list = []

    for excel_file in files:
        #print(excel_file)
        files_list.append(str(excel_file))

    return files_list


def extractExcel(workbook):

    workbook_dict = {}

    workbook = load_workbook(workbook)
    for worksheet in workbook:
        for index, row in enumerate(worksheet.iter_rows()):
            content = [] 
            for cell in row:
                content.append(cell.value)
            workbook_dict[index+1] = content
    
    return workbook_dict


def dateFromString(string):
    '''
    Not really necessary since our extractExcel() function parses and returns the relevant cells
    in datetime format.
    '''

    date_time_object = datetime.strptime(string, '%Y-%m-%d  %H:%M:%S')

    return date_time_object

def diffDate(date1, date2):
    '''
    date1 : datetime_object
    date2 : datetime_object
    '''

    duration = date2 - date1
    duration_seconds = duration.total_seconds()
    hours = divmod(duration_seconds, 3600)[0]

    return hours


def testFunctions():

    listFilesInFolder('ReliabilityData')
    print(extractExcel('ReliabilityData/Plant1.xlsx'))
    print(dateFromString('14-02-2021  14:00:00'))

    date1 = dateFromString('14-02-2021  14:00:00')
    date2 = dateFromString('16-02-2021  14:00:00')
    print(diffDate(date1, date2))
    

#testFunctions()