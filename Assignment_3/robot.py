from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Robot:
    # Max 40kg, can carry products of only one type at a time.

    def __init__(self, id, curr_pos, goal_pos, products=None):
        self.route = None # A list with tuples of the coordinates with its projected path
        self.loadtime = 120
        self.movetime = 10
        self.id = id
        self.products = products

        # Make sure that all the products are of the same type.
        type = product[0].getType()
        for product in products:
            if product.getType() != type:
                raise ValueError('The products are not the same type!')

        self.products = products
    
    def __str__(self):

        string = 'Robot: ' + str(self.id) + ' current position: ' + str(self.getCurrPos()) + ' goal position: ' + str(self.getGoalPos()) + ' \n'

        for product in self.products:
            info = product.getSerialnr() + ' - ' + str(product.getWeight()) + 'kg \n'
            string += info

        return string

    def getRoute(self):
        return self.route
    
    def setRoute(self, route):
        self.route = route
    
    def getProducts(self):
        return self.products
    
    def setProducts(self, products):
        self.products = products
    
    def loadRobot(self, delivery):
        