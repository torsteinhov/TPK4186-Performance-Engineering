from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Catalog:
    
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