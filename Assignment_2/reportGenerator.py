from manager import *
from database import *
from kaplanMeierEstimator import *
import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, database, KME, calculator):
        self.database = database
        self.KME = KME
        self.calculator = calculator

    def getDatabase(self):
        return self.database

    def getKME(self):
        return self.KME

    def getCalculator(self):
        return self.calculator

    def componentToFile(self, component):
        return ""

        
    def writeHTML(self):

        components = self.getDatabase().getWorksheets().keys()
        f = open('reliability_data.html','w')

        text = """<html>
        <head></head>
        <style>
        h1 {text-align: center;}
        p {text-align: center;}
        div {text-align: center;}
        img {text-align: center;}
        .center {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
            }
        </style>
        <body><h1>
                <p>Overview of the different Kaplan-Meier estimate associated with components from the """ + self.getDatabase().folder + """</p>
            </h1>
        """

        for component in components:
            text += """\n  <h2><p>Kaplan-Meier estimate associated with component: """ + component + """</p></h2>"""
            text += """\n  <img src=""" + """'KME_analysis/survival_analysis_""" + component + """.png' class="center">"""
        
        text += """\n </body> </html>"""
        
        f.write(text)
        f.close()

def reportGeneratorRun():

    database = DataBase('ReliabilityData')
    database.createDatabase()
    
    KME = kaplanMeierEstimator('Vibration sensor', database)
    calc = Calculator(KME)

    reportGenerator = ReportGenerator(database, KME, calc)
    reportGenerator.writeHTML()

reportGeneratorRun()