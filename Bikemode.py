class bikeindustry(object):




class wheels():
	
	def __init__(self,weight,cost,name):  
		self.weight = weight
		self.cost = cost
		self.name = name
	

type_1 = wheels(5,2.50,"disc break")   # Types of Wheels
type_2 = wheels(4,2.25,"rim brakes")
type_3 = wheels(4.50, 3, "tubeless")

class frames():
	def __init__(self,weight,cost,material):
		self.weight = weight
		self.cost = cost
		self.material = material

alum = frames(3,5,"aluminunum")   # Types of Frames
carb = frames(2,6,"carbon")
steel_frame = frames(1.50, 4.50, "steel")


class models():

class manufacturers():


class shops()



class customers():
	budget = 2000      #Total Customer Budget for purchasing bikes
	shop_cart ={}		#Customers wishlist
	purchase_amount = {i}		#Amount of Bike Purchase

	def __init__(self, customer_name):
		self.customer_name = customer_name

	def budget_count(self):
		for i in self.budget:
			self.budget -=self.purchase_amount{i}
		return "The total amount of money left is {}".format(self.budget)

		if self.purchase_amount >= self.budget:
			return # Attempting to return a null transaction request
		else:
			return "Not enough money to purchase bike"




