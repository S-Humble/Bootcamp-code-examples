city_flight = input("Enter the name of your airport: BHX, LHR or GTW").upper()
flight_price = {"BHX":70, "LHR":100, "GTW":110}
hotel_price = 50
rental_cost = 45

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

num_nights = int(input("How many nights are you staying?"))
def hotel_cost (num_nights, hotel_price):
    hotel_total = num_nights * hotel_price
    print (f"The hotel cost for {num_nights} nights is £{hotel_total}.")
    return hotel_total

rental_days = int(input("How many days will you be hiring a car for?"))
def car_rental (rental_days, rental_cost):
    car_total = rental_days * rental_cost
    print (f"The cost of your car rental is £{car_total}")
    return car_total
    

def holiday_cost (hotel_total,  car_total):
    holiday_total = (hotel_total +  car_total)
    print (f"The total of your holiday is £{holiday_total}")
    return holiday_total

plane_total = plane_cost(city_flight, flight_price)
hotel_total = hotel_cost(num_nights, hotel_price)
car_total = car_rental(rental_days, rental_cost)

total_holcost = holiday_cost(hotel_total, car_total,)