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

class Cell:

    """
    A class used to represent a cell in the warehouse 
    ...

    Attributes
    ----------
    x : int
        an integer that keeps track of the column number in the warehouse layout
    y : int
        an integer that keeps track of the row number in the warehouse layout  
    type : str
        string that describes what type of cell we are looking at. For example: loading cell, storage cell, transport cell, etc. 
    shelf1 : shelf object
        a shelf object from the shelf class
    shelf2 : shelf object
        a shelf object from the shelf class
    route : 2D list
        a 2D list of the coordinates with its projected path
    product_type: product object
        a product object from the products class
    containRobot: boolean
        True if the cell contains a robot. Otherwise False 
    
    
    Methods
    -------
    getX()
        gets the x coordinate
    getY()
        gets the y coordinate
    getType()
        gets the cell-type
    getShelf1()
        gets the shelf1 object
    getShelf2()
        gets the shelf2 object
    getRoute()
        gets the coordinates that the route consists of
    getProductType()
        gets the product type in storage cells
    getContainRobot()
        gets true/false depending on whether the cell contains a robot
    setX(x)
        set the x coordinate
    setY(y)
        sets the y coordinate
    setType(type)
        sets the cell-type
    setShelf1(shelf1)
        sets the shelf1 object
    setShelf2(shelf2)
        sets the shelf2 object
    setRoute(route)
        sets the coordinates that the route consists of 
    setProductType(product_type)
        sets the product type in storage cells
    setContainRobot()
        sets true/false depending on whether the cell contains a robot
    
    """

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
    
    def getProductType(self):
        return self.product_type
    
    def setProductType(self, product_type):
        self.product_type = product_type
    
    def getContainRobot(self):
        return self.containRobot
    
    def setContainRobot(self, containRobot):
        self.containRobot = containRobot

