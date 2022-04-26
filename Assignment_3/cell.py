from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Cell:

    def __init__(self, x, y, type, shelf1=None, shelf2=None, route=None, product_type=None, containRobot=False):
        self.x = x
        self.y = y
        self.type = type
        self.shelf1 = shelf1 # only for storage cells
        self.shelf2 = shelf2 # only for storage cells
        self.route = route # route direction for route cells
        self.product_type = product_type # only for storage cells
        self.containRobot = containRobot
    
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x
    
    def getY(self):
        return self.y
    
    def setY(self, y):
        self.y = y
    
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type
    
    def getShelf1(self):
        return self.shelf1
    
    def setShelf1(self, shelf1):
        self.shelf1 = shelf1
    
    def getShelf2(self):
        return self.shelf2
    
    def setShelf2(self, shelf2):
        self.shelf2 = shelf2
    
    def getRoute(self):
        return self.route
    
    def setRoute(self, route):
        self.route = route
    
    def getContainRobot(self):
        return self.containRobot
    
    def setContainRobot(self, containRobot):
        self.containRobot = containRobot