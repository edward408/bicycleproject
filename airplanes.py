"""
Exercise 5.1 Classes and Initialization
"""
# Part A

class Trip(object):
    """Define the destinations with respective dates"""
    
    def __init__(self,departCity,arriveCity,departTime,departDay,arriveTime,arriveDay):
        self.departCity = departCity
        self.arriveCity = arriveCity
        self.departTime = departTime
        self.departDay = departDay
        self.arriveTime = arriveTime
        self.arriveDay = arriveDay

    caribList = [ 'GCM', 'CUR' ]
    hawaiiList = [ 'ITO', 'HNL' ]

    
    def display_trip(self):
        return "Going from %s to %s" % (self.departCity, self.arriveCity)

    def isRoundTrip(self):
        if self.departCity == self.arriveCity:
            return True
        else:
            return False


    def isOvernight(self):
        if self.departDay != self.arriveDay:
            return True
        else:
            return False

    def isCarribean(self):
        if self.arriveCity in Trip.caribList:
            return True
        else:
            return False

    def isInterIsland(self):
        if self.arriveCity and self.departCity in Trip.hawaiiList:
            return True
        else:
            return False

class Flight(Trip):
    """Define information regarding to the flight"""
    def __init__(self,flightnum,cost, code,departCity,arriveCity,departTime,departDay,arriveTime,arriveDay):
        self.flightnum = flightnum
        self.cost = cost
        self.code = code
        #Trip.__init__(self,departCity,arriveCity,departTime,departDay,arriveTime,arriveDay)
        #use of super method
        super(Flight, self).__init__(departCity,arriveCity,departTime,departDay,arriveTime,arriveDay)

    def discount(self):
        discount = 1.00
        if self.isInterIsland():
            discount -= 0.05
        elif self.isCarribean():
            discount -= 0.15
        else:
            print "Sorry no discount for you!"
                
        return self.cost * discount

def nextId(n):
    n+=1

    return n

num = nextId(99)


    

class Reservation(object):
    """Customers make their reservations"""
    def __init__(self,name,flightData):
        self.name = name
        self.flightData = flightData
        self.reservationId = nextId(num)

    
        
trip_1 = Trip('CUR','HNL','12:00','Sunday','20:00','Sunday')

print trip_1.display_trip()
print trip_1.isRoundTrip()
print trip_1.isOvernight()

print Trip.caribList
print Trip.hawaiiList

print trip_1.isCarribean()
print trip_1.isInterIsland()


# Part B


trip1 = Trip("HNL","ITO","8:00","Monday","14:00","Monday")
trip2 = Trip("HKG","HNL","6:00","Monday","11:00","Monday")
trip3 = Trip("CDG","GCM","12:00","Monday","20:00","Monday")
trip4 = Trip("ARN","ARN","17:00","Tuesday","7:00","Wednesday")

tripList = [ trip1, trip2, trip3, trip4 ]
    
def printTrip(t):
    flight = "Trip from {} to {}\n".format(t.departCity,t.arriveCity)
    flight += "Departs at {} on {}\n".format(t.departTime,t.departDay)
    flight += "Arrives at {} on {}\n".format(t.arriveTime,t.arriveDay)
    return flight
    #return'Trip from', t.departCity, 'to', t.arriveCity, 'Departs at', t.departTime, 'on', t.departDay, 'Arrives at', t.arriveTime, 'on', t.arriveDay

for trips in tripList:
    if trips.isRoundTrip():
         print printTrip(trips)
         print 'is RoundTrip'
        
class Aircraft(object):
    def __init__(self,aircraftcode,name):
        self.aircraftcode= aircraftcode
        self.name = name
    
# Part C

# Sample Data for Aircraft
airplane = Aircraft("HNL","Canadian Regional Jet")


flight1=Flight("FL2304",500,"2",'CUR','HNL','12:00','Sunday','20:00','Sunday')
print flight1.discount()

reservation1 = Reservation("Bob Builder",flight1)
reservation2= Reservation("Lolo Bond",flight1)
print reservation1.flightData.departCity
print reservation1.reservationId
print reservation2.reservationId

# code is 1
# name is Canadian Regional Jet
#
# Sample Data for Airport
# code is HNL
# city is Honolulu

