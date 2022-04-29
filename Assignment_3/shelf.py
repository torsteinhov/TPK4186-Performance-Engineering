from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Shelf:

    """
    A class used to represent the shelves
    ...

    Attributes
    ----------
    productSerialNr : str
        a string with the serial number of the product
    amount: int 
        integer describing the amount of the product
    max_weight: int
        integer describing the maximum weight of the shelves(in kilogram)
    shelf_weight: int
        integer describing the current weight in the shelves(in kilogram)
    

    Methods
    -------
    getShelfWeight()
        gets the weight in the shelves
    getAmount()
        gets the amount of products in a shelf
    getMax_weight()
        gets the maximum weight a shelf can carry
    getProductSerialNr()
        gets the products' serial number
    setAmount(amount)
        sets the amount of a product in a shelf
    setProductSerialNr(productSerialNr)
        sets what product a shelf are going to store
    """

    def __init__(self, productSerialNr = None, amount=0):

        # Each shelf can only contain one type of product, identified with serialNr
        self.productSerialNr = productSerialNr
        self.amount = amount
        self.max_weight = 100
        self.shelf_weight = 0

    def getShelfWeight(self):

        for product in self.products:

            self.shelf_weight += product.getWeight()

        return self.shelf_weight
    
    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount = amount
    
    def getMax_weight(self):
        return self.max_weight
    
    def getProductSerialNr(self):
        return self.productSerialNr
    
    def setProductSerialNr(self, productSerialNr):
        self.productSerialNr = productSerialNr