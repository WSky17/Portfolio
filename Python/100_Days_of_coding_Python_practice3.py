#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 07:56:27 2022

@author: warren
"""


#Exercise 3.1 Odd or even

# 🚨 Don't change the code below 👇
# =============================================================================
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# 
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")
#     
# =============================================================================

#practice if/else/ elif
# =============================================================================
# print ("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# 
# if height >= 120:
#     print("You can ride the rollercoaster! ")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# =============================================================================

# Exercise 3.2 BMI 2.0

# =============================================================================
# 
# =============================================================================


# Exercise 3.3 Leap Year Exercise 

# =============================================================================
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# 
# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print ("Not leap year.")  
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
# =============================================================================

#Exercise 3.4 Pizza Order 

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill +=1

print (f"Your final bill is ${bill}")






















