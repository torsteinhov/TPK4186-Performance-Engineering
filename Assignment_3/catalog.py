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

class Catalog:

    """
    A class used to represent a catalog 
    ...

    Attributes
    ----------
    products : product objects
        product objects in the catalog
    
    Methods
    -------
    __str__()
        prints out intresting information in a nice way
    getProducts()
        gets product objects from the catalog
    setProducts(products)
        sets product objects to the catalog
    """
    
    def __init__(self, products):

        self.products = products

    def __str__(self):

        string = 'The Catalog contains '+ str(len(self.products)) +' products: \n'

        for product in self.products:
            info = product.getSerialnr() + ' - ' + str(product.getWeight()) + 'kg \n'
            string += info

        return string
    
    def getProducts(self):
        return self.products

    def setProducts(self, products):
        self.products = products        