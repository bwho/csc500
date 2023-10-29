'''
Code prompt:
Write a program that calculates the total amount of a meal purchased at a restaurant.
The program should ask the user to enter the charge for the food and then calculate
the amounts with an 18 percent tip and 7 percent sales tax. Display each of these amounts
and the total price.
'''

#Set initial tip and sales tax percentages
percent_tip = 0.18
percent_sales_tax = 0.07

#Gather the food cost from the user
print("Enter cost of food: $", end='')
food_cost = float(input())

#Calculate the tip and sales tax amounts, rounding them off to 2 decimal places
# NOTE: We tip on the total amount of the meal BEFORE sales tax
amount_tip = round(food_cost * percent_tip, 2)
amount_sales_tax = round(food_cost * percent_sales_tax, 2)

#Then determine the total price by summing the food cost, tip amount, and sales tax amount
total_price = food_cost + amount_tip + amount_sales_tax

#Print out the values for all three computed values: tip amount, sales tax, and total price
#adding a newline prior to the outputs and after them to make it easier to read
print("\nTip amount: ${:.2f}".format(amount_tip), end='')
print("\nSales tax amount: ${:.2f}".format(amount_sales_tax), end='')
print("\nTotal price: ${:.2f}".format(total_price), end='')
print()