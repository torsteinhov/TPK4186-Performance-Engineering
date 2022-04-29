'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from catalog import *
from cell import *
from client_order import *
from delivery import *
from printer import *
from product import *
from robot import *
from shelf import *
from truck import *
from warehouse import *

import unittest

class Test(unittest.TestCase): 
        
    def testGettersAndSetters(self):


        #Product
        product1 = Product('s', 4)
        product2 = Product('t', 4)
        product1.setSerialnr('SN007')
        product1.setWeight(7)
        product2.setSerialnr('SN008')
        product2.setWeight(10)
        self.assertEqual(product1.getSerialnr(),'SN007')
        self.assertEqual(product1.getWeight(), 7)
        self.assertEqual(product2.getSerialnr(),'SN008')
        self.assertEqual(product2.getWeight(), 10)

        #Catalog
        catalog = Catalog([product1, product2])
        catalog.setProducts([product1, product2])
        self.assertEqual(catalog.getProducts(),[product1, product2])

        #Robot
        robot1 = Robot('XX-1')
        self.assertEqual(robot1.getId(), 'XX-1')
        robot1.setCurrPos([4,8])
        self.assertEqual(robot1.getCurrPos(), [4,8])
        
        robot1.setRoute([[4,8],[5,8],[6,8]])
        robot1.getRoute()
        robot1.setCurrPos([4,8])
        self.assertEqual(robot1.getCurrPos(), [4,8])


        robot1.setCurrPos([4,8])
        robot1.setGoalPos([7,8])

        robot1.setRobotAvailability(False)
        self.assertEqual(robot1.isRobotAvailable(), False)
        robot1.setRobotAvailability(True)
        self.assertEqual(robot1.isRobotAvailable(), True)


        self.assertEqual(robot1.getMaxCarry(), 40)

if __name__ == "__main__":
    unittest.main()