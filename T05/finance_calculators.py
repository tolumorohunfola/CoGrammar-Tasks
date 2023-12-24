# A program to calculate monthly payments for a house or returns for an investment where the details are provided by the user

import math # importing the math module

# a function presenting the two types of calculations available to user and requesting their confirmation for which type they would like to do
# * Could try to do this by printing the two options as a table when I refactor to allow for better formatting in any font. *

user_menu_choice = "" # defining the user's menu choice before it is called in the if statement which confirms user's choice was valid.

def intro_and_choice_request():
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")

    user_menu_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip()
    # lowercase and strip methods used to ensure the user_menu_choice allows as many correct cases as possible - in case user adds spaces or uses upper and lowercases
    return user_menu_choice

# program intro being called and value returned being set as user's menu choice
user_menu_choice = intro_and_choice_request()

# confirms the user's choice was valid
if user_menu_choice == "bond" or user_menu_choice == 'investment':


    print(f"Thank you for choosing to see the calculation for your {user_menu_choice}.")

    #nested if statement to run the calculations based on inputs
    if user_menu_choice == "investment":
        # if the user input is investment

        # ask the user to input deposit amount, interest rate (%), number of years of investing planned, preference of simple or compound interest
        deposit_amount = float(input("Please type in the amount of money you will be depositing: "))
        interest_rate_invest = float(input("Please type in the interest rate in percent: "))
        number_of_years_of_investing = int(input("Please type in the number of years you plan to invest for: "))
        interest_choice = input("Please type your interest preference between simple or compound interest: ").lower().strip()

        # changing the interest rate input into the interest rate needed for the formula. - dividing it by 100
        interest_rate_invest_decimal = interest_rate_invest / 100

        if interest_choice == "simple":
            # simple interest formula
            total_amount = deposit_amount * (1 + interest_rate_invest_decimal * number_of_years_of_investing)
            print(f"As you have chosen simple interest, the total amount you can expect when you deposit £{deposit_amount} at a {interest_rate_invest}% interest rate for {number_of_years_of_investing} years is approximately £{total_amount:.2f}")
            # used :.2f to ensure the output is in 2 decimal places
        elif interest_choice == "compound":
            # compound interest formula
            total_amount = deposit_amount * math.pow((1 + interest_rate_invest_decimal), number_of_years_of_investing)
            print(f"As you have chosen compound interest, the total amount you can expect when you deposit £{deposit_amount} at a {interest_rate_invest}% interest rate for {number_of_years_of_investing} years is approximately £{total_amount:.2f}")
        else:
            print("Nothing was calculated as you didn't choose between simple or compound interest. Please restart the application.")


    if user_menu_choice == "bond":
        # if the user input is bond

        # ask the user to input the present value of the house (int), the interest rate in percent, the number of months they plan to take to repay the bond
        house_present_value = int(input("Please type in the current value of the house in pounds without commas or spaces: "))
        interest_rate_bond_yearly = float(input("Please type in the annual interest rate in percent: "))
        number_of_months_to_repay = int(input("Please type in the number of months you plan to take to repay the bond: "))

        # adjusting the interest rate to be monthly and dividing by 100
        interest_rate_bond_monthly = interest_rate_bond_yearly / 12 / 100

        # bond repayment formula
        repayment = (interest_rate_bond_monthly * house_present_value) / (1 - (1 + interest_rate_bond_monthly) ** (-number_of_months_to_repay))
        print(f"If the present value of the house is £{house_present_value}, the yearly interest rate is {interest_rate_bond_yearly}% and you plan to take {number_of_months_to_repay} months to repay, you will need to pay £{repayment:.2f} per month on the bond.")


else:
    # else statement in case the user didn't choose a bond or investment
    print(f"{user_menu_choice.capitalize()} is not one of the options, please start the program again and choose either 'investment' or 'bond'.")
