#Name: Saransh Kalra
#Course: 1411-505
#Date: 12/05/2017
#
#PROBLEM:
#Given the month and the year, write a program to determine the no of days
#that month has in that particular year
#
#GIVEN:
#The month and the year
#
#ANALYSIS:
#Input: the month and the year
#Output: the number of days in that month of that particular year
#
#METHOD/ALGORITHM
#Introduce the program
#Take the input_month from the user
#Take the input_year from the user
#Check whether the month is april/june/september/november or is it february or is it any other month of the year
#Check whether the year is a leap year or not
#Print the result

#MAIN PROGRAM:

#Introduce the program
print("This program prompts the month and year from the user")
print("and then gives the number of days in that month")
print("of that particular year")
print("         ")

#Take the input_month from the user
month=input("enter the month u want to find the number of days for: ")

#Take the input_year from the user
year=int(input("enter the year: "))

#Check whether the month is april/june/september/november or is it february or is it any other month of the year
if(month=="APRIL" or month=="JUNE" or month=="SEPTEMBER" or month=="NOVEMBER" or month=="april" or month=="june" or month=="september" or month=="november"):
    days=30
elif(month=="february" or month=="FEBRUARY"):
#Check whether the year is a leap year or not
    if((year%4==0 and year%100!=0) or year%400==0):
        days=29
    else:
        days=28
else:
    days=31

#Print the result
print("the no of days in ", month , year ,"is ", days)     










    
