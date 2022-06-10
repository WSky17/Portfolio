#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:23:09 2022

@author: warren
"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
plane_boat = input(" As you begin your adventure, you have a choice of transportation. \n There is a boat to the left or airplane to the right.\n\nDo you choose Right or Left?  ").lower()

if plane_boat == "right":
    print("\nThe plane ran out of fuel.\n")
    print('''  GAME OVER\n
*************************************************************************
                   ____       _
               | __\_\_o____/_|
               <[___\_\_-----< ........................
               |  o'                             ..
                                               ..
                                              .
                                             .
                                            .
                                           .
                                           .
                                          .
                                          .
                                         .
                                         .
                                        )/
                                      _@'
                                       o\\n
*************************************************************************
''') 
elif plane_boat == "left":
    print("\nGood choice!! Your journey continues.")
boat = input("You hear a waterfall ahead.  \nDo you take your chances in the boat or swim for shore?\nEnter Boat or Swim.\n")

if boat.lower() == "boat":
    print("\nCongratulations!! It took some pretty mean rowing, but you made it to safely to shore.")

elif boat.lower() == "swim":    
    print("You were eaten by piranha\n GAME OVER")

door = input("You have arrived at Blackbeard's lair.\nThere are three doors.  You must pick wisely or suffer the consequences.\n Which do you choose?\n Enter Red, Blue, Yellow\n")

if door.lower() =="yellow":
        print("You have located the treasrure. You win!!!\nProceed to live a grand life.\nGAME OVER")

elif door.lower() == "red":
    print("You have triggered a booby trap and succumbed to grievous wounds.\nGAME OVER")

elif door.lower() == "blue":
    print("A trap door opened under your feet and you have fallen to your death.\nGAME OVER")
    
    
    
      