#Name: Saransh Kalra
#Course: 1411-505
#Date: 09/05/2017
#
#PROBLEM:
#Given a number,add 2, multiply by 3, subtract 6,
#and divide by 3 to get the number with which you started
#
#GIVEN:
#An integer
#
#ANALYSIS:
#Input: the number
#Output: the number we get adding 2, multiplying 3,
#        subtracting 6 and dividing by 3 which is the same number we started with
#
#METHOD/ALGORITHM
#Introduce the program
#Take the imput_number from the user
#Do the calculations according to the problem
#Print the result

#PROGRAM:
#Introduce the program
print ('This program inputs the number from the user and adds 2,')
print ('multiplies by 3, subtracts 6, and divide by 3')
print ('outputs the number we started with back ')

#Take the input_number from the user
user_no=int(input('enter the number: '))

#Do the calculations according to the problem
print('adding 2 : ' , user_no+2)
print('multiplying 3 : ' ,(user_no+2)*3)
print('subtracting 6 : ' ,(user_no+2)*3-6)
print('dividing by 3 : ' ,((user_no+2)*3-6)/3)

#Print the result
print('The end result is : ',((user_no+2)*3-6)/3)
