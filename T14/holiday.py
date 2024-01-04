# a program to calculate a user's total holiday cost, including place, hotel and car-rental
print("This is a program to calculate the total cost of your holiday. To exit, type end anytime your input is requested.")

return_flights = {
    "Mallorca" : 200.57,
    "Faro" : 149.24,
    "Edinburgh" : 50.34,
    "Dublin" : 130/26,
    "Tokyo" : 700.75
}

#***
# # requesting user input for city they are flying to
# print("The options for cities you may travel are Mallorca Spain, Faro Portugal, Edinburgh Scotland or Dublin Ireland or Tokyo Japan.")

# try:
#     city_flight = int(input("Please enter the name of the city you will be flying to: "))
# except ValueError as e:
#     print(str(e))

# while city_flight.lower().strip() not in cities:
#     if city_flight.lower().strip() == "end":
#         print("This program has been terminated as requested.")
#         quit()
#     print(f"{city_flight} is not a valid city. Please ensure that your input is one word.")
#     print("The options for cities you may travel are Mallorca Spain, Faro Portugal, Edinburgh Scotland or Dublin Ireland or Tokyo Japan.")
#     city_flight = input("Please enter the name of the city you will be flying to: ")

#***

# requesting user input for number of nights they will be staying at

# requesting user input for the number of days they will be hiring a car

city_flight = "Mallorca"
num_nights = 5
rental_days = 4


# due to a special deal across these cities all hotels are now the same price per night 
hotel_price_per_night = 45.85 

# due to a special deal across these cities, all rental cars have the same daily price
car_price_per_day = 80.13 

# function to calculate the hotel cost
def hotel_cost(num_nights):
    # multiplies the price per night and number of nights the user will be staying
    total_price = num_nights * hotel_price_per_night
    return total_price

# a function to calculare the cost of the flight 
def plane_cost(city_flight):
    cost = return_flights[city_flight]
    return cost

def car_rental(rental_days):
    # multiplies the price per day and the number of days the car is needed
    total_price = rental_days * car_price_per_day
    return total_price

# define function to calculate total cost of the holiday
def holiday_cost(hotel_cost, plane_cost, car_rental):
    # prints out information regarding the total cost of the hotel
    print(f"The total cost of the hotel will be £{hotel_cost:.2f} for {num_nights} nights at £{hotel_price_per_night:.2f} per night.")
    # prints out information regarding the flight cost
    print(f"The cost of your flight to {city_flight} will be £{plane_cost:.2f} in total.")
    # prints out the information regarding the car rental
    print(f"The car rental will cost £{car_rental:.2f} in total for {rental_days} days at £{car_price_per_day:.2f} per day.")
    # adds all the costs totgether.
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost

print(f"The total cost of your holiday will be £{holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days)):.2f}.")