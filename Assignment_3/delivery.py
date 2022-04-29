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

class Delivery:

    """
    A class used to represent the delivery of products
    ...

    Attributes
    ----------
    date : datetime object
        datetime object corresponding to the delivery
    products: dictionary 
        dictionary containing product and amount(client order). Product is key and amount is value
    
    Methods
    -------
    __str__()
        prints out intresting information in a nice way
    getWeight()
        gets the total weight of the delivery
    getDate()
        gets the date and time when the delivery is completed/created
    getProducts()
        gets product objects from the delivery
    setProducts(products)
        sets product objects to the delivery
    """

    def __init__(self, products):

        self.date = datetime.today()
        self.products = products # {product: amount}
    
    def __str__(self):

        string = 'Delivery: \n produced - ' + str(self.date) +'\n'

        for product, amount in self.products.items():
            info = product.serialnr + ' - ' + str(floor(amount)) + ' units\n'
            string += info
        
        string += 'The total weight of the delivery: ' + str(self.getWeight()) + ' kg'

        return string
    
    def remove(self, product, amount):
        pass
    
    def add(self, product, amount):
        pass

    def getWeight(self):
        weight = 0
        for product in self.products.keys():
            weight += product.getWeight() * self.products[product]
        
        return weight
    
    def getDate(self):
        return self.date
    
    def getProducts(self):
        return self.products

    def setProducts(self, products):
        self.products = products