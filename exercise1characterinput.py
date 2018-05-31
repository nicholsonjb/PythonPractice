#Author: James Nicholson
#Date: 5/30/2018
#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them
# the year that they will turn 100 years old.

import datetime

now = datetime.datetime.now()

name = input("Please enter your name: ")
print("Hello, " + name)

age = int(input("Enter your age: "))

year = str((now.year - age)+100)

print(name + " will be 100 years old in the  year " + year)
