#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 09.30.22
# This program calculates the price of a pizza with user input.

pizza_size = float((input("What is the pizza siza?(cm) ")))
order_amount = float((input("How many pizzas would you like to order? ")))
print("")

HST = 13 / 100
ingredients_toppings_price = 1.50 * pizza_size
labor_cost = 2.00 * order_amount
rental_cost = 2.25 * order_amount
total_cost = ingredients_toppings_price + labor_cost + rental_cost

print("Ingredients and Topings = ${:.2f} ".format(ingredients_toppings_price))
print("Labor cost cost = ${:.2f}".format(labor_cost))
print("The rental = ${:.2f}".format(labor_cost))

print("The total price + tax is ${:.2f}".format(total_cost + (HST * total_cost)))
