# A program that determines which award a person competing in a triathlon will receive

print("This is a program to determine the award you will receive. To terminate the program, type 'end' when input is requested.")

# defining function to request input
def request_time(event):
    time = input(f"Please enter the amount of time in minutes it took to complete the {event} section: ")
    # while statement to request input until valid
    while time.isdigit() == False:
        # if statement in case user request program termination
        if time.lower() == 'end':
            print("The program has been terminated as requested.")
            quit()
        print("Your input is invalid")
        time = input(f"Please enter the amount of time in minutes it took to complete the {event} section: ")
    
    return int(time)


# read the times (in minutes) for all three events of a triathlon
# swimming
swimming_time = request_time('swimming')

# cycling
cycling_time = request_time('cycling')

# running
running_time = request_time('running')

# calculate and display the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time

print(f"You completed your triathlon within {total_time} minutes in total.")

# The below section works out which award the person receives

# defining the award variable
award = ""

# firstly taking care of the event that the total time input is less than 0 minutes (This would be an error.)
if total_time < 0:
    print("Please restart this program, your input is below zero and therefore invalid.")
# if the total time taken is between 0-100 minutes, the award is Provincial Colours
elif total_time >= 0 and total_time <= 100:
    award = "Provincial Colours"
# if the total time taken is between 100 and 105 minutes, the award is Provincial Half Colours
elif total_time <= 105:
    award = "Provincial Half Colours"
# if the total time taken is between 105 and 110 minutes, the award is Provincial Scroll
elif total_time <= 110:
    award = "Provincial Scroll"
# if the total time taken is over 110 minutes, there is no award.
else:
    award = False

# if statement to print out the award
if award == "Provincial Colours" or award == "Provincial Half Colours" or award == "Provincial Scroll":
    print(f"Your award is {award}. Well done!")
elif award == False:
    print("You have unfortunately not received an award on this occasion, but well done for completing the triathlon and we hope you try again next time!")