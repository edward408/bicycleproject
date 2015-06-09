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
        self.bike_inventory = []
        

    def display_bikes(self):
        print "The store is called %s and it has %s" % (self.store_name,self.bike_inventory)
        
        
    
class Customers(object):
    
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget
        self.shopping_cart ={}

    def purchase(self):
        pass 

    def display_customers(self):
        print "Customer is %s and with a budget of %s dollars" % (self.name, self.budget)
    

