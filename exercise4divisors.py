#Author: James Nicholson
#Date: 5/31/2018
#Create a program that asks the user for a number and
#  then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number 
# that divides evenly into another number. For example,
#  13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Enter a number: ")) #input number

listRange = list(range(1,num+1)) #List range for numbers

divisorList = [] #divisor list

for number in listRange: #Loop to do math
    if num % number == 0:
        divisorList.append(number)
5
print(divisorList) #prints divisor list

#End Script
