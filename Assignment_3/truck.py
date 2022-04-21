from multiprocessing.sharedctypes import Value
from sympy import ProductSet


class Truck:

    
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