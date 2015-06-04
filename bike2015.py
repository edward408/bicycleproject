#Modeling the bicycle industry

class Bicycle(object):

    def __init__(self,model,weight,production_cost):
        self.model = model
        self.weight = weight
        self.production_cost = production_cost

class Bike_Shops(Bicycle):
    bike_inventory ={}
    #a dictionary that has every shop and a list of models for each?
    def __init__(self,name,retail_cost,profit):
        self.name = name
        self.retail_cost = retail_cost
        self.profit = self.production_cost - self.retail_cost

class Customers(Bike_Shops):
    shopping_cart ={}
    def __init__(self,name,budget):
        self.name = name
        self.budget = budget

    def purchase(self):
        if 

    def display_customers(self):
        print "Customer is %s and with a budget of %s dollars" % (self.name, self.budget)
    

customer_1 = Customers("Jeff",200)
customer_2 = Customers("Ryan",500)
customer_3 = Customers("John",1000)

customer_1.display_customers()
customer_2.display_customers(
