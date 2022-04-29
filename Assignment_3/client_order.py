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

class ClientOrder:

    """
    A class used to represent the client order
    ...

    Attributes
    ----------
    date : datetime object
        datetime object corresponding to the client order
    order: dictionary 
        dictionary containing product and amount(client order). Product is key and amount is value
    
    Methods
    -------
    __str__()
        prints out intresting information in a nice way
    getOrder()
        gets the order
    setOrder(order)
        sets the order 
    getWeight()
        gets the total weight of the order
    getDate()
        gets the date and time when the order is placed/created
    """
    
    def __init__(self, order):

        self.date = datetime.today()
        self.order = order # {product: amount}
    
    def __str__(self):

        string = 'Client order: \n produced - ' + str(self.date) +'\n'

        for product, amount in self.order.items():
            info = product.serialnr + ' - ' + str(floor(amount)) + ' units\n'
            string += info
        
        string += 'The total weight of the client order: ' + str(self.getWeight()) + ' kg'

        return string
    
    def getOrder(self):
        return self.order
    
    def setOrder(self, order):
        self.order = order

    def getWeight(self):
        weight = 0
        for product in self.order.keys():
            weight += product.getWeight() * self.order[product]
        
        return weight
    
    def getDate(self):
        return self.date