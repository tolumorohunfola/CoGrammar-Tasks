# a program to calculate the total stock worth of a cafe with 4 menu items.

print("This is a program to calculate the total stock worth of a cafe with 4 menu items.")
#creating a list called menu for the cafe items
menu = ["ice-cream cake", "chocolate donut", "salmon sandwich", "jam sandwich"]
number_in_stock_list = [8, 30, 10, 5]
prices_of_stock_list = [3.85, 2, 4.99, 4.50]

# creating dictionary called stock using dictionary comprehension
stock = {item : number for (item, number) in zip(menu, number_in_stock_list)}

#creating dictionary called price using dictionary comprehension
price = {item: price for (item, price) in zip(menu, prices_of_stock_list)}

#calculating the total stock worth in the cafe using for loop
total_stock = 0
for item in menu:
    # multiply number in stock by price for item
    item_value = stock[item] *  price[item]
    total_stock +=item_value

# printing the result of the calculation as pounds.
print(f"The total worth of all the stock within the cafe is £{total_stock:.2f}")