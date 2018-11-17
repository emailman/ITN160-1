#Assignment 3
#v1.0
#POS

import physense_emuX
import time


# create sensor connection
sensor = physense_emuX.Sensor()

colorLED = "rled"

# Welcome message
print("POS Booting Up")
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print(".")
time.sleep(.5)
print()

print("POS System Online and Ready to Process Orders")
#prompt user to enter meal names and prices
bevName = input("Enter the beverage ordered(soda, juice, coffee, water):")            #beverage name
bevPrice = float(input("Enter the beverage price:$"))                                   #beverage price

print()
mealName = input("Enter food ordered(sandwich, salad, steak, tacos):")            #food name
mealPrice = float(input("Enter the food price:$"))                                  #food price


#display receipt
print()
print()
print()
print()
print()
print()
print()
print()

print("                Order #3651")
#print("\n")
print("----------Food and Beverages Ordered----------")
print()
print("Beverage:     " + str(bevName) + " $" + str(bevPrice))
print("Food:         " + str(mealName) + " $" + str(mealPrice))
print("Total:               $" + str(bevPrice + mealPrice))
print("----------------------------------------------")

#Notify Kitchen
sensor.output(colorLED, "on")
time.sleep(1)
sensor.output(colorLED, "off")
