city_flight = input("Enter the name of your airport: BHX, LHR or GTW").upper() #user input from three choises of airport. .upper() makes every input uppercase to allow it to work with dictionary
flight_price = {"BHX":70, "LHR":100, "GTW":110} #dictionary used to store price values of each airport. Values can be used as arguments to determine cost of a flight 
hotel_price = 50 #can be edited to show price of hotel per night
rental_cost = 45 #car rental cost per day

def plane_cost (city_flight, flight_price): #function to calculate the cost of flights from flight_price list.    
    if city_flight in flight_price:
        print (f"Your flight will cost £{flight_price[city_flight]}.") #user input from city_flight to access values from flight_price dictionary. flight_price{city_flight] finds the appropriate 
        #price from the airport code that is used prevents the need to produce a separate elif statement for each airport and allows more airports to be added to flight_price without the need to make new elif statements 
        return flight_price[city_flight] #returns integer value from the function call.  Stops the function provided the city_flight input matches a value from the dictionary
    elif city_flight not in flight_price: #if the input does not match one of the values from flight_price, the integer value for the calculation of total holiday price is 0
        return flight_price == 0
    
while city_flight not in flight_price: #if the correct code is not used in the city_flight, while statement allows user to re-enter correct code after informing that it is incorrect 
    print  ("This is an incorrect input. Please try again")
    city_flight = input("Enter the name of your airport: BHX, LHR or GTW").upper()

num_nights = int(input("How many nights are you staying?")) #Allows user to input teh number of nights in the hotel
def hotel_cost (num_nights, hotel_price):
    hotel_total = num_nights * hotel_price
    print (f"The hotel cost for {num_nights} nights is £{hotel_total}.") #prints the total of hotel cost x number of nights 
    return hotel_total

rental_days = int(input("How many days will you be hiring a car for?"))
def car_rental (rental_days, rental_cost):
    car_total = rental_days * rental_cost
    print (f"The cost of your car rental is £{car_total}.")#prints the cost of car rental based upon number of days required 
    return car_total
    

def holiday_cost (hotel_total,  car_total, plane_total): #provide total values for all 3 functions to calculate the total holiday cost
    holiday_total = (hotel_total +  car_total  + plane_total)
    print (f"The total costof your holiday is £{holiday_total}.")
    return holiday_total

plane_total = plane_cost(city_flight, flight_price) #These allow the programme to print the total cost for flight cost, hotel cost and car rental based on the functions above 
hotel_total = hotel_cost(num_nights, hotel_price)
car_total = car_rental(rental_days, rental_cost)

total_holcost = holiday_cost(hotel_total, car_total, plane_total) # Total holiday cost based upon addition of hote, car and flight total