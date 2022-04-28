from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class ClientOrder:
    
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
    
    def remove(self, product, amount):
        pass
    
    def add(self, product, amount):
        pass

    def getWeight(self):
        weight = 0
        for product in self.order.keys():
            weight += product.getWeight() * self.order[product]
        
        return weight
    
    def getDate(self):
        return self.date