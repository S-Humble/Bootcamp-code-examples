Original plane_cost code:
def plane_cost (city_flight, flight_price):      
        if city_flight == "BHX":
            print (f"Your flight will cost £{flight_price['BHX']}.")
        elif city_flight == "LHR":
            print (f"Your flight will cost £{flight_price['LHR']}.")
        elif city_flight == "GTW":
            print (f"Your flight will cost £{flight_price['GTW']}.")
        return flight_price[city_flight]   
while city_flight not in flight_price:
        print ("This is an incorrect input. Please try again")
        city_flight = str(input("Enter the name of your airport: BHX, LHR or GTW")).upper()

Allowed me to access the dictionary, flight_price to produce the string
"Your flight will cost £{flight_price['GTW']}." inputing the cost from each airport

It also allowed for an error message if an incorrect code used. But it did not allow me to use the integer value from the flight_cost dict. 

New code: 
def plane_cost (city_flight, flight_price):   
    if city_flight in flight_price:
        print (f"Your flight will cost £{flight_price[city_flight]}.")
        return flight_price[city_flight]
    elif city_flight not in flight_price:
        return flight_price == 0
    
while city_flight not in flight_price:
    print  ("This is an incorrect input. Please try again")
    city_flight = input("Enter the name of your airport: BHX, LHR or GTW").upper()

city_flight user input used to access value from flight_price.
