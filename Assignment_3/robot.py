from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

from product import Product
from shelf import *

class Robot:
    # Max 40kg, can carry products of only one type at a time.

    """
    A class used to represent the robots
    ...

    Attributes
    ----------
    route : 2D list
        a 2D list of the coordinates with its projected path
    curr_pos: list
        a list with the x and y coordinate of the robots' current position
    next_pos: list 
        a list with the x and y coordinate of the robots' next position
    last_pos: list 
        a list with the x and y coordinate of the robots' last position
    goal_pos: list 
        a list with the x and y coordinate of the robots' goal position
    goingHome: boolean
        true if the robot is going back to the delivery loading ramp. Otherwise false
    going2Shelf: boolean
        true if the robot is going to a shelf to load a product. Otherwise false
    loadtime: int
        time(in seconds) that the robot use to load a product from a shelf
    movetime: int
        time(in seconds) that the robot use to move from a cell to another cell
    id: str
        string with the robots' id
    products: list
        list with serial number of the product as well as the amount
    maxCarry: int
        determines the maximum weight the robot can carry (in kg)
    isAvailable: boolean
        true if the robot available to collect products. Otherwise, false
    

    Methods
    -------
    getId()
        gets the id
    getGoingHome()
        gets true if the robot is going back to the delivery loading ramp. Otherwise false
    getGoing2Shelf()
        gets true if the robot is going to a shelf to load a product. Otherwise false
    getRoute()
        gets the coordinates that the route consists of
    getProducts()
        gets the product object the robot carry
    getMaxCarry()
        gets the maximum weight the robot can carry
    getLastPos()
        gets list with the x and y coordinate of the robots' last position
    getCurrPos()
        gets list with the x and y coordinate of the robots' current position
    getNextPos()
        gets list with the x and y coordinate of the robots' next position
    getGoalPos()
        gets list with the x and y coordinate of the robots' goal position
    isRobotAvailable()
        gets the robot's status, ie whether it is busy or not
    setGoingHome(goingHome)
        sets the status of goingHome to true/false
    setGoing2Shelf(going2Shelf)
        sets the status of going2Shelf to true/false
    setRoute(route)
        sets the robots' route
    setLastPos(last_pos)
        sets the robots' last position
    setCurrPos(curr_pos)
        sets the robots' current position
    setGoalPos(goal_pos)
        sets the robots' goal position
    setNextPos(next_pos)
        sets the robots' next position    
    setProducts(products)
        sets the products the robot carries
    setRobotAvailability(availability)
        sets the robots' status
    loadRobot(serialNr, amount)
        load the robot with a product(serialNr) and amount of the product
    loadShelf(shelf,serialNr, amount)
        l
    
    
    
    
    

    
    
    """

    def __init__(self, id, products=None):
        self.route = None # A 2D list of the coordinates with its projected path
        self.curr_pos = None
        self.next_pos = None
        self.goal_pos = None
        self.last_pos = None
        self.goingHome = False
        self.going2Shelf = False
        self.loadtime = 120
        self.movetime = 10
        self.id = id
        self.products = products # list [serialNr, amount]
        self.maxCarry = 40

        if self.route == None:
            self.isAvailable = True

        self.type = None
        # This will never happen, taken care of in warehouse
        '''type = product[0].getType()
        for product in products:
            if product.getType() != type:
                raise ValueError('The products are not the same type!')'''


    def __str__(self):

        string = 'Robot: ' + str(self.id) + ' current position: ' + str(self.getCurrPos()) + ' goal position: ' + str(self.getGoalPos()) + ' \n'

        for product in self.products:
            info = product.getSerialnr() + ' - ' + str(product.getWeight()) + 'kg \n'
            string += info

        return string

    def getId(self):
        return self.id
    
    def getGoingHome(self):
        return self.goingHome
    
    def setGoingHome(self, goingHome):
        self.goingHome = goingHome
    
    def getGoing2Shelf(self):
        return self.going2Shelf
    
    def setGoing2Shelf(self, going2Shelf):
        self.going2Shelf = going2Shelf
    
    def getRoute(self):
        return self.route
    
    def setRoute(self, route):
        self.route = route
        self.setLastPos(route[-1])
    
    def getProducts(self):
        return self.products
    
    def getMaxCarry(self):
        return self.maxCarry
    
    def setProducts(self, products):
        self.products = products
    
    def getLastPos(self):
        return self.last_pos
    
    def setLastPos(self, last_pos):
        self.last_pos = last_pos

    def getCurrPos(self):
        return self.curr_pos
    
    def setCurrPos(self, curr_pos):
        self.curr_pos = curr_pos
    
    def getNextPos(self):
        return self.next_pos

    def getGoalPos(self):
        return self.goal_pos
    
    def setGoalPos(self, goal_pos):
        self.goal_pos = goal_pos

    def setNextPos(self, next_pos):
        self.next_pos = next_pos
    
    def isRobotAvailable(self):
        return self.isAvailable
    
    def setRobotAvailability(self, availability):
        self.isAvailable = availability
    
    def loadRobot(self, serialNr, amount):
        
        self.setProducts([serialNr, amount])
    
    def loadShelf(self, shelf, serialNr, amount):

        # This is checked twice, but nice etiquette.
        if serialNr == shelf.getProductSerialNr():
            # Fills the shelf
            shelf.setAmount(shelf.getAmount() + amount)
            # The robot has loaded the shelf and we remove the products from the robot.
            self.setProducts(None)
    
    def unloadShelf(self, shelf, serialNr, amount):

        # This is checked twice, but nice etiquette.
        if serialNr == shelf.getProductSerialNr():
            # Retrieve products from the shelf
            shelf.setAmount(shelf.getAmount() - amount)
            # The robot has unloaded the shelf and we remove the products from the robot.
            self.setProducts(None)


    def moveRobot(self, goal):
        # goal is in the format [x,y] of the goal position
        pass