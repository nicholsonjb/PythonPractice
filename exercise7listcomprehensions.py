 #Author: James Nicholson
#Date: 6/10/2018
#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

import random

a = [] #random numbers list
b = random.randint(5,15) #random list size from 5 to 15


while len(a) < b: #Loop to generate random list of numbers from 1 to 75 and poplate a
    a.append(random.randint(1,75))

even_list = [number for number in a if number % 2 == 0] #even numbers from list

print(a) # prints list a
print(even_list) #prints list b
