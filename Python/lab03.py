#Name: Saransh Kalra
#Course: 1411-505
#Date: 9/19/2017
#
#PROBLEM:
#Given two numbers, implement the Russian Peasant or Ancient Egyptian method for multiplication.
#We repeatedly multiply first number by 2 and divide second number by 2 until second no. becomes zero.
#To figure out the product of the two numbers, we keep a running total where we add first no.
#every time the result of dividing second no. by 2 is an odd number.
#
#GIVEN:
#the two numbers whose product is neede to be found
#
#ANALYSIS:
#Input: the two numbers that are +ve
#Output: the product of the two numbers
#
#TEST CASES:
#INPUT: 1 AND 2
#OUTPUT: 2
#
#INPUT: 10 AND 0
#OUTPUT: 0
#
#INPUT: 22 AND 20
#OUTPUT: 440
#
#METHOD/ALGORITHM:
#Introduce the program
#Take the numbers from the user
#Multiply first no. to 2 and divide second no. by 2 repeatedly until no. 2 becomes 0
#And add first no. to product every time B comes out to be odd
#Print the result i.e the result of the two numbers

#MAIN PROGRAM:

#INTRODUCE THE PROGRAM
print("This program takes two numbers from the user, repeatedly multiply first number by 2 and divide second number")
print("by 2 until second no. becomes zero.To figure out the product of the two numbers, we keep a running total where")
print("we add first no.every time the result of dividing second no. by 2 is an odd number.")

#TAKE THE NUMBERS FROM THE USER
num1= int(input("enter the first number:"))
num2= int(input("enter the second number:"))
product=0

#MULTIPLY FIRST NUM BY 2 AND DUVIDE SECOND NUMBER BY 2 REPEATEDLY UNTIL NUM 2 BECOMES 0
#AND ADD FIRST NUM TO THE PRODUCT EVERY TIME SECOND NUMBER COMES OUT TO BE ODD
if(num2%2!=0):
    product=product + num1
while(num2!=0):
    num1= num1*2
    num2= num2//2
    if(num2%2!=0):
        product+=num1

#PRINT THE RESULT I.E THE RESULT OF THE TWO NUMBERS
print("The product of the two numbers is: ", product)        
        
    
    
    
    
    
