'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''


from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Product:

    """
    A class used to represent a single product.
    ...

    Attributes
    ----------
    serialnr : str
        a string with the serial number of the product
    weight: int 
        integer describing the weight of the product(in kilogram)
    
    Methods
    -------
    getSerialnr()
        gets the serial number
    setSerialnr(serialnr)
        sets the serial number 
    getWeight()
        gets the weight of the product
    setWeight(weight)
        sets the weight of the product
    """

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