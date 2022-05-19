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

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 ==0:
    if year % 100 >0:
        print ("no leap")
    if year % 400 == 0:
        print("A Leap year")  
    else:
        print("Not leeper")
else:
    print("Not a Leap Year")









