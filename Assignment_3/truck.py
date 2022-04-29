'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from multiprocessing.sharedctypes import Value
from sympy import ProductSet


class Truck:

    """
    A class used to represent a truck.
    ...

    Attributes
    ----------
    deliveries : delivery object
        a string with the serial number of the product
    weight: int 
        integer describing the weight loaded on the truck(in kilogram)
    max_weight: int
        integer describing the maximum weight the truck can take(in kilogram)
    

    Methods
    -------
    __str__()
        prints out intresting information in a nice way
    getWeight()
        gets the weight loaded on the truck
    addProduct(product, amount)
        add amount of a product to the truck
    removeProduct(product, amount)
        remove amount of a product off the truck
    notFull(product)
        check(true/false) if the truck are going to be full if you add a product
    """
    
    def __init__(self, deliveries):
        self.deliveries = deliveries
        self.weight = 0
        self.max_weight = 20000

    def __str__(self):
        
        string = 'Truck: \n'
        

        for delivery in self.deliveries:

            # Making sure that the truck does not load another delivery if it can not manage the weight
            while self.weight + delivery.getWeight() <= self.max_weight:
                for product, amount in delivery.getProducts().items():
                    string += 'Product: ' + str(product.getSerialnr()) + ' - Amount: ' + str(amount) +'\n'
            
                self.weight += delivery.getWeight()
        
        string += 'Total weight: ' + str(self.weight) + ' kg'
        return string
    
    def getWeight(self):
        return self.weight
    
    def addProduct(self, product, amount):
        if product not in self.products.keys():
            self.products[product] = amount
        else:
            self.products[product] = self.products[product] + amount
        print('The product is added to the truck \n' + self)
    
    def removeProduct(self, product, amount):
        if amount < self.products[product]:
            self.products[product] = self.products[product] - amount
        if amount == self.products[product]:
            del self.products[product]
        else:
            raise ValueError('Removing more products, than actually in the delivery')
        
    def notFull(self, product):
        notFull = self.getWeight() + product.getWeight() <= self.max_weight
        return notFull