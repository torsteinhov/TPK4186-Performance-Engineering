from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Shelf:

    def __init__(self, productSerialNr = None, amount=None):

        # Each shelf can only contain one type of product, identified with serialNr
        self.productSerialNr = productSerialNr
        self.amount = amount
        self.max_weight = 100
        self.shelf_weight = 0

    def getShelfWeight(self):

        for product in self.products:

            self.shelf_weight += product.getWeight()

        return self.shelf_weight

    def getProducts(self):
        return self.products
    
    def getMax_weight(self):
        return self.max_weight
    
    def getProductSerialNr(self):
        return self.productSerialNr
    
    def setProductSerialNr(self, productSerialNr):
        self.productSerialNr = productSerialNr