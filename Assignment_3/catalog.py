from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Catalog:

    """
    A class used to represent the catalog 
    ...

    Attributes
    ----------
    products : product objects
        product objects in the catalog
    
    Methods
    -------
    getProducts()
        gets the products in the catalog
    setProducts(products)
        sets the products to the catalog
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