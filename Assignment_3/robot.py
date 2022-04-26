from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

from product import Product

class Robot:
    # Max 40kg, can carry products of only one type at a time.

    def __init__(self, id, products=None):
        self.route = None # A 2D list of the coordinates with its projected path
        self.loadtime = 120
        self.movetime = 10
        self.id = id
        self.products = products # dictionary {serialNr: amount}
        self.maxCarry = 40

        if self.route == None:
            self.isAvailable = True

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
    
    def getMaxCarry(self):
        return self.maxCarry
    
    def setProducts(self, products):
        self.products = products
    
    def isRobotAvailable(self):
        return self.isAvailable
    
    def loadRobot(self, serialNr, amount):
        
        self.setProducts({serialNr, amount})

    def moveRobot(self, goal):
        # goal is in the format [x,y] of the goal position

        self.route[-1] = goal