#Name: Saransh Kalra
#Course: 1411-505
#Date: 9/26/2017
#
#PROBLEM:
#Write a program to prompt the user for a message that the program will encrypt
#and then decrypt (reverse the encryption process) 
#
#GIVEN:
#the message to be encrypted
#
#ANALYSIS:
#Input: the message to be encrypted
#Output: the encrypted code i.e. ciphertext and the decrypted message
#
#ALGORITHM:
#The ciphertext is formed by the even letters followed by the odd letters in the message
#
#METHOD:
#Introduce the program
#Add whether to continue or not condition with validation
#Take the message from the user
#Now store the even letters in one string
#Now store the odd letters in another string
#Print the result i.e the encrypted message and the decrypted message
#
#TEST CASES:
#INPUT: abcdef
#OUTPUT: The cyphertext is:  bdface
#        The decrypted message is:  abcdef
#
#INPUT: there is a dog
#OUTPUT: The cyphertext is:  hr sadgteei  o
#        the decrypted message is:  there is a dog
#
#INPUT: burst out laughing
#OUTPUT: The cyphertext is:  us u agigbrtotluhn
#        the decrypted message is:  burst out laughing

#MAIN PROGRAM:
#INTRODUCE THE PROGRAM
print("WELCOME TO THE MESSAGE ENCRYPTION SYSTEM: ")
ch='y'

#ADD WHETHER TO CONTINUE OR NOT CONDITION WITH INPUT VALIDATION
while((ch=='y' or ch=='Y') and (ch!='n' or ch!='N')):
    

    #TAKE THE MESSAGE FROM USER
    str3=input("Enter the message to be encrypted: " )

    #NOW STORE THE EVEN LETTERS IN ONE STRING
    str1=str3[::2]

    #NOW STORE THE ODD LETTERS IN ANOTHER STRING
    str2=str3[1::2]

    #PRINT THE RESULT I.E THE ENCRYPTED MESSAGE AND THE DECRYPTED MESSAGE
    print("The cyphertext is: ",str2 + str1)
    print("the decrypted message is: ",str3)

    ch=input("do you want to continue: ")
    while(ch!='y' and ch!='Y' and ch!='N'and ch!='n'):
            ch=input("INVALID INPUT, ENTER Y/N: ")
            continue
        
print("end of program")    

    
        







    
