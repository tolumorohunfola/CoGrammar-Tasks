# a program to calculate a user's total holiday cost, including place, hotel and car-rental
print("This is a program to calculate the total cost of your holiday. To exit, type 'end' anytime your input is requested.")

# defining the stable variables

# due to a special deal across these cities all hotels are now the same price per night
hotel_price_per_night = 45.85

# due to a special deal across these cities, all rental cars have the same daily price
car_price_per_day = 80.13


# defining the cost of flying to cities on a return trip.
return_flights = {
    "Mallorca" : 200.57,
    "Faro" : 149.24,
    "Edinburgh" : 50.34,
    "Dublin" : 130.26,
    "Tokyo" : 700.75
}


# function to quit the program if the user inputs 'end'
def check_end(user_input):
    if user_input.lower().strip() == 'end':
        print("The program has been terminated as requested.")
        quit()


# a function to check if user input is valid based on the type it should be (list or int)
def request_input(type, message):
    # input request
    user_input = input(message)

    # if the input has any non-letters or is not in the list
    if type == "list":
        # loops the below while the input is invalid
        while user_input.isalpha() == False or user_input.lower().capitalize() not in return_flights.keys():
            # checks if the user input was the end the program
            check_end(user_input)
            # print out the personal error message
            if user_input.isalpha() == False:
                print("Your input is invalid. It must only consist of letters.")
            else:
                print("Your input is invalid. Please check your spelling")
            # request input again
            user_input = input(message)

    elif type == "integer":
        # loops the below while the input is invalid
        while user_input.isdigit() == False or int(user_input) < 0:
            # checks if the user input was the end the program
            check_end(user_input)
            print("Your input is invalid. It must be a whole number and must be a positive number (0 or above).")
            # request input again
            user_input = input(message)
    # returns the user input once it is valid.
    return user_input


# requesting user input for where they plan to travel to
city_flight = request_input("list", "The options for cities you may travel are Mallorca (Spain), Faro (Portugal), Edinburgh (Scotland) or Dublin (Ireland) or Tokyo (Japan). \nPlease enter the name of the city you will be flying to: ").lower().capitalize()

# requesting user input for number of nights they will be staying at
num_nights = int(request_input("integer", f"Please enter the number of nights you'll stay at {city_flight}: ")) # number of nights they are staying - int

# requesting user input for the number of days they will be hiring a car
rental_days = int(request_input("integer", f"Please enter the number of days you would like to rent a car while you're in {city_flight}: ")) # number of days they will rent - int


# function to calculate the hotel cost
def hotel_cost(num_nights):
    # multiplies the price per night and number of nights the user will be staying
    total_price = num_nights * hotel_price_per_night
    return total_price

# a function to calculate the cost of the flight
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
    # adds all the costs together.
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost

print(f"The total cost of your holiday will be £{holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days)):.2f}.")