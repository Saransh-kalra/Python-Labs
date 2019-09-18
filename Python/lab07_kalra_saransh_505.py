#Name: Saransh Kalra
#Course: 1411-505
#Date: 10/24/2017
#
#PROBLEM:
#Write a program to prompt the user for his answers to the The Myers-Briggs personality
#test which has 70 questions that determine a person’s personality in 4 dimensions.
#Each question has 2 answer choices that we’ll call the “A” and “B” answers.
#Then give the result on the basis of a's or b's in each dimension. 
#
#GIVEN:
#The answers to the personality analysis test entered by the user
#
#ANALYSIS:
#Input: the answers to the personality test
#Output: The result of the personality analysis according to the answers i.e. a string representing that 
#
#ALGORITHM:
#the result is determined by taking out the percentage of b options chosen if its less than
#50% in that dimension option 1 otherwise option 2 
#
#METHOD:
#Function to take in a list and return the percentage of b characters in it
#Function to take a string wich has the
#seventy answers and breaking them into 7 as needed
#and them compiling them into 4 categories and
#returning a string with percentages of b in each of the category
#Loop to slice the 70 answers into groups of 7
#Loop to make individual list of dimensions as needed
#Making a list of all percentages of b in all dimensions and returning it
#Function to return the result of the personality analysis according
#to the percentage of b characters in each of the ten sets of answers
#Introduction of the program
#Prompt the user for entering the string of answers he entered for the test
#Calling the percent function with the string of answers as the argument
#The result being the result function passed with the string of
#percentages returned by percent function 
#
#TEST CASES:
#INPUT: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#OUTPUT: ISTJ
#
#INPUT: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
#OUTPUT: EIFP
#
#INPUT: ababababababababababababababababababababababababababababababababababab
#OUTPUT: EIFP

#MAIN PROGRAM:
#function to take in a list and return the percentage of b characters in it
def b_counter(list):
    count=0
    for item in list:
        if item=='B':
            count+=1
    b_percent=(count/len(list))*100
    return b_percent

#function to take a string wich has the
#seventy answers and breaking them into 7 as needed
#and them compiling them into 4 categories and
#returning a string with percentages of b in each of the category
def percent(str):
    list_of_ans=[]
    answer7=''
    i=0

#loop to slice the 70 answers into groups of 7
    while(i<70):
        answer7=str[i:i+7]
        list_of_ans.append(answer7)
        i+=7

    Dim1_list=[]
    Dim2_list=[]
    Dim3_list=[]
    Dim4_list=[]

#loop to make individual list of dimensions as needed 
    for group in list_of_ans:
        Dim1_list.append(group[0])
        Dim2_list.append(group[1])
        Dim2_list.append(group[2])
        Dim3_list.append(group[3])
        Dim3_list.append(group[4])
        Dim4_list.append(group[5])
        Dim4_list.append(group[6])

#making a list of all percentages of b in all dimensions and returning it
    b_list=[]
    b_list.append(b_counter(Dim1_list))
    b_list.append(b_counter(Dim2_list))
    b_list.append(b_counter(Dim3_list))
    b_list.append(b_counter(Dim4_list))
    
    return b_list

#function to return the result of the personality analysis according
#to the percentage of b characters in each of the ten sets of answers
def result(list1):

    p_list=[] #list to store the result
#if b is less than 50% then option 1
    if list1[0]<50:
        p_list.append('I')
    else:
        p_list.append('E')
    if list1[1]<50:
        p_list.append('S')
    else:
        p_list.append('I')
    if list1[2]<50:
        p_list.append('T')
    else:
        p_list.append('F')    
    if list1[3]<50:
        p_list.append('J')
    else:
        p_list.append('P')
    return ''.join(p_list) 

#introduction of the program
print("Welcome To The Personality Analysis System")

#prompt the user for entering the string of answers he entered for the test
str1=input("Enter the string to be tested: ")

#calling the percent function with the string of answers as the argument
a = percent(str1)

#the result being the result function passed with the string of
#percentages returned by percent function 
print("Your result is: ", result(a))
    
        




