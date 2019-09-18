#Name: Saransh Kalra
#Course: 1411-505
#Date: 10/17/2017
#
#PROBLEM:
#Write a recursive helper function called writeChars that accepts an integer parameter n and prints
#out a string returned by another recursive method that is called by writeChars 
#
#GIVEN:
#the string size 
#
#ANALYSIS:
#Input: the string size
#Output: the desired string consisting of stars and gretaer and less than signs
#
#ALGORITHM:
#The the desired strings is formed by greater than and less than signs with stars in between according to the
#length of string provided by user, if its odd one star is in between and if its even two stars are there in between the signs
#the number of greater than and less than signs are decided based on the string size given by thew user
#
#METHOD:
#program to return the desired string to the user as he/she wished
#according to his input
#if n is 0 or less, then return a blank string as its invalid
#if n is odd, then return a string with a single star
#if n is even, then return a string with double star
#introduction to program
#loop for asking if he wants to continue
#prompt user for string size
#validating the integer input
#calling fuction writeChars() with argument as users input
#asking the user if he wants to continue and validating the input
#
#TEST CASES:
#INPUT: -1
#OUTPUT: 
#
#INPUT: 0
#OUTPUT: 
#
#INPUT: 2
#OUTPUT: **
#
#INPUT: 5
#OUTPUT: <<*>>
#
#INPUT: 1
#OUTPUT: *
#
#INPUT: 4
#OUTPUT: <**>


#MAIN PROGRAM:
#program to return the desired string to the user as he/she wished
#according to his input
def writeChars(n):
    #if n is 0 or less, then return a blank string as its invalid
    if(n<=0):
        return ''
    #if n is odd, then return a string with a single star
    elif(n%2==1):
        if(n==1):
            return '*'
        elif(n<=0):
            return ''
        else:
            return '<' + writeChars(n-2) + '>'
    #if n is even, then return a string with double star    
    else:
        if(n==2):
            return '**'
        elif(n<=1):
            return ''
        else:
            return '<' + writeChars(n-2) + '>'

#introduction to program
print("Welcome to the string printing program")

#loop for asking if he wants to continue
ch='y'
while(ch=='y' or ch=='Y'):
    #prompt user for string size
    k=0
    c=1 #put c=1 for entering that loop
    k=input("Enter the integer for the string size: ")   
    #validating the integer input
    try:
        l=int(k)    
    except ValueError:
        print("this is not a valid integer input")
    #will work only if there is no exception
    else:
        #calling fuction writeChars() with argument as users input
        p=writeChars(l)
        print("The string is : ", p)

    #asking the user if he wants to continue and validating the input
    while(c==1):
        c=0
        try:
            ch=input("Do you want to enter another number?(Y/N): ")
        except ValueError:
            print("please enter y/n")
            c=1
    #every time the input is invalid c=1 so it asks again for input            
        else:    
            if(ch!='n' and ch!='N' and ch!='y' and ch!='Y'):
                print("please enter y/n")
                c=1
            if(ch=='n' or ch=='N'):
                print("Thank you!")
                    
            



    



        
