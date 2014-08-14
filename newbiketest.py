from copy import deepcopy

class Wheel():
	def __init__(self, wheel_type, weight, cost):
		self.wheel_type = wheel_type
		self.weight = weight
		self.cost = cost
	def __repr__(self):
		return "wheel {} {} {}".format(self.wheel_type,self.weight, self.cost)

class Frame():
	def __init__(self, material, weight, cost):
		self.material = material
		self.weight = weight
		self.cost = cost
	def __repr__(self):
		return "frame {} {} {}".format(self.material, self.weight, self.cost)


class Bike ():
	def __init__(self,front_wheel, back_wheel, frame, name):
		self.front_wheel = front_wheel
		self.back_wheel = back_wheel
		self.frame = frame
		self.name = name
	def __repr__(self):
		return "bike brand is {} weight is {} cost is {}".format(self.name, self.total_weight(), self.cost())
	def cost(self):
		return self.front_wheel.cost+self.back_wheel.cost+self.frame.cost
	def total_weight(self):
		return self.front_wheel.weight+self.back_wheel.weight+self.frame.weight

class Manufacturer():
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage
        self.inventory = []
        

    def __repr__(self):
		return " name is {} percentage is {}".format(self.name, self.percentage)


    def get_name(self):
        return self.name

    def get_percentage(self):
        return self.percentage
    
    def add_bikeinventory(self,bike):
    	self.inventory.append(bike)

    def print_inventory(self):
    	for bike in self.inventory:
    		print bike
    def get_inventory(self):
    	return self.inventory


class Shop():

	def __init__(self, name, inventory, price, profit):
		self.name = name
		self.inventory = inventory
		self.price = price
		self.profit = profit

	def __repr__(self):
		return "bike brand is {} name is {} percentage is {}".format(self.name, self.inventory, self.cost, self.profit, self.bike_inventory())

	def bike_inventory(self):
		pass


	

class Customer():
	pass
			
		



if __name__ == '__main__':

	wheel_1= Wheel("large", 3, 10.00)
	wheel_2 = Wheel("medium",2, 6.00)
	frame_1 = Frame ("steel",3, 100.00)
	bike_1 = Bike(wheel_1, wheel_2, frame_1, "Xtreme")
	wheel_3= Wheel("small", 1, 4.00)
	wheel_4 = Wheel("small",1, 4.00)
	frame_2 = Frame ("aluminum",3, 70.00)
	frame_3 = Frame("carbon",2, 65.00)
	bike_2 = Bike(wheel_3, wheel_4, frame_2, "Kid")
	bike_3 = Bike(wheel_2, wheel_1, frame_1, "Pro")

	manufact_1 = Manufacturer("Max", 0.05)
	manufact_1.add_bikeinventory(bike_1)
	manufact_1.add_bikeinventory(bike_2)
	manufact_2 = Manufacturer("Lennon", 0.03)

	#shop = Shop("GreenRide",[manufact_1, manufact_2],350)

	#customer_1 = Customer("Jeff", 1000)
	#customer_2 = Customer("Mark", 300)
	#customer_3 = Customer("Rob", 600)

	#customer_line = [customer_1, customer_2, customer_3]





	# Bike 1 cost and weight "print bike_1.cost(), bike_1.total_weight() 

	print bike_1
	print bike_2
	manufact_1.print_inventory()
	print manufact_1.get_inventory()
	for bike in manufact_1.get_inventory():
		print bike.name









