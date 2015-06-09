from bikes import *


def customers_walkin():
    customer_1 = Customers("Jeff",50)
    customer_2 = Customers("Ryan",100)
    customer_3 = Customers("John",30)
    cust_list = [customer_1,customer_2,customer_3]
    for customers in cust_list:
        customers.display_customers()
        
customers_walkin()

def main():

    bike_1 = Bicycle("Xtreme",5, 20)
    bike_2 = Bicycle("Passive",5, 15)
    bike_3 = Bicycle("EcoRide", 5, 18)
    bike_4 = Bicycle("GreenGo",5,22)
    bike_5 = Bicycle("Gemini", 6, 25)
    bike_6 = Bicycle("Kidsgo",3, 10)
    bike_list = [bike_1, bike_2, bike_3, bike_4, bike_5, bike_6]

    store = Bike_Shop("Bobs Bike Shop")
    for bikes in bike_list:
        store.bike_inventory.append(bikes)

    print (store.bike_inventory)

    


if __name__ == '__main__':
    main()








