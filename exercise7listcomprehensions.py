 #Author: James Nicholson
#Date: 6/10/2018
#Write a program that creates a list of 5 to 15 numbers from 1 to 75.
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

import random

a = [] #random numbers list
b = random.randint(5,15) #random list size


while len(a) < b: #Loop to generate random list of numbers
    a.append(random.randint(1,75))

even_list = [number for number in a if number % 2 == 0]

print(a)
print(even_list)
