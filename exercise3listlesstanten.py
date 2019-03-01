 #Author: James Nicholson
#Date: 5/30/2018
#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the 
# elements of the list that are less than 5.
 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Enter a number: "))

new_list = []

for i in a:
    if i < num:
        new_list.append(i)
print(new_list)

#End Script
