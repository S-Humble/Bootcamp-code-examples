#city_flight = str(input("Enter the name of your airport: BHX, LHR, GTW or HRW")).upper()
num_nights = int(input("How many nights are you staying?"))
#rental_days = int(input("How many days will you be hiring a car for?"))

def hotel_cost (num_nights, hotel_price):
    total_hotel = num_nights * hotel_price
    #return (f"The hotel cost for {num_nights} is £{total_hotel}.")
    print (f"The hotel cost for {num_nights} is £{total_hotel}.")

def plane_cost (city_flight, ):
    total = city_flight
    if city_flight == "BHX":
        print (f"Your flight will cost £ {BHX}")
    elif city_flight == "LHR":
        print (f"Your flight will cost £ {LHR}")

def car_rental (rental_days, rental_cost):
    total = rental_days * rental_cost
    return (f"The cost of your rental is {car_rental}")

def holiday_cost (hotel_cost, plane_cost, car_rental):
    total = hotel_cost + plane_cost + car_rental
    return 


#Flight cost
BHX = 70
LHR = 100
GTW = 110
HRW = 200

#Hotel price per night
hotel_price = int(50)
hotel_cost = (hotel_price)
#Car price per day
car_price = 45