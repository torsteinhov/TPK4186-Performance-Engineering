'''
Assignment 2 - TPK4186

Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from manager import *
from database import *
from kaplanMeierEstimator import *
import matplotlib.pyplot as plt

class ReportGenerator:

    """
    The ReportGenerator class takes in a database, a kaplanMeierEstimator and a calculator class and produces HTML reports of the survival analysis results calculated,
    in a representable, and easy to read format.
    ...

    Attributes
    ----------
    database : Database_object
        A database object with all the reliability data stored in a convenient format, with management functions.
    KME : kaplanMeierEstimator_object
        An object of the kaplanMeierEstimator class.
    calculator : Calculator_object
        A calculator with functionality to calculate values for plotting of survivability analysis, plotting the analysis aswell as storing pictures of the plot.

    Methods
    -------
    getDatabase(self):
        returns database object.
    getKME(self):
        returns kaplanMeierEstimator object.
    getCalculator(self):
        returns the calculator object.
    writeHTML(self):
        takes in the component names and their associated survival analysis plots and creates a HTML report based on the results.
    """

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
                <p>Survival Analysis of components in: """ + self.getDatabase().folder + """</p>
            </h1>
        """

        for component in components:
            text += """\n  <h2><p>Kaplan-Meier estimate: """ + component + """</p></h2>"""
            text += """\n  <img src=""" + """'KME_analysis/survival_analysis_""" + component + """.png' class="center">"""
        
        text += """\n </body> </html>"""
        
        f.write(text)
        f.close()