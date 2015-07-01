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
        

    def display_bikes(self):
        print "The store is called %s and it has %s" % (self.store_name,self.bikes)

    def bikes_under(self, budget):
        affordable_bikes = []
        for bike in self.store_inventory:
            if bike.retail_cost <= budget:
                affordable_bikes.append(bike)
                
        return affordable_bikes
        
        
    
class Customers(object):
    
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
        


from main import *


def main():
    
    #Customer instances
    customer_1 = Customers("Jeff",50)
    customer_2 = Customers("Ryan",100)
    customer_3 = Customers("John",30)
    cust_list = [customer_1,customer_2,customer_3]
    def customers_walkin():
        for customers in cust_list:
            customers.display_customers()
        
    customers_walkin()

    #Bicycle instances
    bike_1 = Bicycle("Xtreme",5, 20)
    bike_2 = Bicycle("Passive",5, 15)
    bike_3 = Bicycle("EcoRide", 5, 18)
    bike_4 = Bicycle("GreenGo",5,22)
    bike_5 = Bicycle("Gemini", 6, 25)
    bike_6 = Bicycle("Kidsgo",3, 10)
    bike_list = [bike_1, bike_2, bike_3, bike_4, bike_5, bike_6]

    #Shows the inventory of Bobs Bike Shop
    store = Bike_Shop("Bobs Bike Shop")
    for bikes in bike_list:
        store.store_inventory.append(bikes)

    print "This is the available shop inventory"    
    print store.store_inventory

    for customers in cust_list:
            print customers.name
            print store.bikes_under(customers.budget)
            customers.purchase(store.store_inventory,store.bikes_under(customers.budget))

    print "This is the remaining shop inventory"
    print store.store_inventory
            

    
