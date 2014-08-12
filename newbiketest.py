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
	def __str__(self):
		return "bike brand is {} weight is {} cost is {}".format(self.name, self.total_weight(), self.cost())
	def cost(self):
		return self.front_wheel.cost+self.back_wheel.cost+self.frame.cost
	def total_weight(self):
		return self.front_wheel.weight+self.back_wheel.weight+self.frame.weight

class Manufacturer():
    def __init__(self, name, percentage):
        self.name = name
        self.percentage = percentage

    def get_name(self):
        return self.name

    def get_percentage(self):
        return self.percentage

    def __str__(self):
		return "bike brand is {} name is {} percentage is {}".format(self.generate_bikes(), self.name, self.percentage)

    def generate_bikes(self):
        bikeList = []
        frameList = [frame_1, frame_2, frame_3]
        wheelList = [wheel_1, wheel_2, wheel_3]

        for i in range(3):
            bb = Bike(self.name, i+1)
            bb.set_frame(frameList[i])
            bb.set_wheels(wheelList[i])
            bikeList.append(bb.generate_bike())

        return bikeList

class Shop():
	pass

class Customer():
	pass




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
manufact_1 = Manufacturer("Lexon",2)



# Bike 1 cost and weight "print bike_1.cost(), bike_1.total_weight() 

print bike_1
print bike_2
print manufact_1

