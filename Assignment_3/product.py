from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Product:

    def __init__(self, serialnr, weight):

        self.serialnr = serialnr

        # premise: 40kg >= weight >= 2kg
        if weight <= 40 and weight >= 2:
            self.weight = weight
        
        else:
            raise ValueError("Weight does not have a valid value")
        
    def getSerialnr(self):
        return self.serialnr
        
    def setSerialnr(self, serialnr):
        self.serialnr = serialnr
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight