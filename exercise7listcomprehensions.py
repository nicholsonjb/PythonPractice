 #Author: James Nicholson
#Date: 6/10/2018
#Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

import random

a = [] #random numbers list
b = random.randint(5,15) #random numbers generated


while len(a) < b:
    a.append(random.randint(1,75))

even_list = [number for number in a if number % 2 == 0]

print(a)
print(even_list)
