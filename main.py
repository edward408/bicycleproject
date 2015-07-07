from bikes import *


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
            

    
        
            
    

if __name__ == '__main__':
    main()





