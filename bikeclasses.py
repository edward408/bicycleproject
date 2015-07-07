#Modeling the bicycle industry
#Classes layout
#Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to design applications and computer programs.
#Methods are essential in encapsulation concept of the OOP paradigm
class Bicycle(object):
    def __init__(self,model,weight,production_cost):
        self.model = model
        self.weight = weight
        self.production_cost = production_cost
        self.retail_cost = self.production_cost * 1.20
        

class Bike_Shop(object):
    """Defines the bike shop with its respective inventory"""
    def __init__(self,store_name):
        self.store_name = store_name
        self.store_inventory = []
        self.affordable_bikes = []
        

    def display_bikes(self):
        print "The store is called %s and it has %s" % (self.store_name,self.bikes)

    def bikes_under(self, budget):
        for bike in self.store_inventory:
            if bike.retail_cost <= budget:
                self.affordable_bikes.append(bike)

    def getAffordableBikes(self):
        return self.affordable_bikes
        
        
        
class Customers(Bike_Shop):
    
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget
        self.shopping_cart ={}

    def purchase(self,store_inventory,affordable):

        for bike in store_inventory:
            if bike in affordable:
                self.shopping_cart[bike.model]=bike.retail_cost
                self.budget -=bike.retail_cost
                store_inventory.remove(bike)
                
        
    def display_customers(self):
        print "Customer is %s and with a budget of %s dollars" % (self.name, self.budget)




