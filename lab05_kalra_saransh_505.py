#Name: Saransh Kalra
#Course: 1411-505
#Date: 10/10/2017
#
#PROBLEM:
#Write a program to enable a user to create a web page By asking for the desired inputs
#and inputing the corresponding html code in the file.
#The user will be prompted for the name of the web page file and its title.
#
#GIVEN:
#INPUTS FROM THE USER FOR CREATING HIS/HER DESIRED WEBPAGE
#
#ANALYSIS:
#Input: the elements of the webpage
#Output: the webpage in html syntax is stored and the webpage is stored
#
#METHOD:
#introduce the program
#creating a function for converting the new line entered to its html code
#creating a function for converting the image to its html code
#creating a function for converting the bold new line entered to its html code
#creating a function for converting the new colored text entered to its html code
#initialising the variable body to be written into the webpage
#check the file validation code
#menu creation
#completing the html code and writing it in the html file

#MAIN PROGRAM
#introduce the program
print("WELCOME TO THE WEBPAGE CREATION SYSTEM")
#creating a function for converting the new line entered to its html code
def option1(string):
    str1=string + "<br/>" + '\n'
    return str1

#creating a function for converting the image to its html code
def option2(string):
    a='0'
    try:
        my_file=open(string, "r")                                                 #file opened to check even if it exists
    except:
        print("this file does not exist")       
    else:                
        a='1'                                                                     #if the file exists a becomes 1 otherwise it remains zero
    if(a=='1'):
        str1="<img src=\""+ string +"\"><br/>" + '\n'                       #if the file exists then only convert it into its html code and return it
        return str1
    else:
        return ''                                                                 #otherwise return a null value

#creating a function for converting the bold new line entered to its html code
def option3(string):
    str1="<b>" + string + "</b><br/>" + '\n'
    return str1

#creating a function for converting the new colored text entered to its html code
def option4(string,color):
    str1="<font color=\"" + color + "\">" + string + "</font><br/>" + '\n'
    return str1

#initialising the variable body to be written into the webpage
body = "<html>\n<head>\n<title>"

#check the file validation code
c='1'
while(c=='1'):
    file1=input("enter the name of the html file u want to create a webpage in: ")
    try:
        my_file= open(file1, "r")
        print("this file already exists try again")
        continue
    except:
        my_file= open(file1, "w")
        c='2'
title=input("enter the title of the webpage: ")
body = body + title + "</title>" + "\n" + "</head>" + "\n"

#menu creation
print("WEBPAGE ADDITION MENU CHOICES: ")
print("1. Text Line")
print("2. Image")
print("3. Bold Text Line")
print("4. Color Text Line")
print("5. Exit")

ch=''
ch=input("enter menu choice: ")
while(ch!='5'):
    
    if(ch=='1'):
        str12=input("enter the text line to be inserted: ")
        strf=option1(str12)
        body+=strf
    elif(ch=='2'):
        str23=input("enter the image file name to be inserted: ")
        strf1=option2(str23)
        if(strf1==''):
            ch='2'
            continue
        else:    
            body+=strf1
    elif(ch=='3'):
        str34=input("enter the bold text line that you want to insert: ")
        strf2=option3(str34)
        body+=strf2
    elif(ch=='4'):
        str45=input("enter the coloured text line that you want to insert: ")
        str51=input("enter the color: ")
        strf3=option4(str45,str51)
        body+=strf3
    elif(ch=='5'):
        print("you quit the menu")
        break    
    else:
        print("invalid choice try again")

    print("WEBPAGE ADDITION MENU CHOICES: ")
    print("1. Text Line")
    print("2. Image")
    print("3. Bold Text Line")
    print("4. Color Text Line")
    print("5. Exit")
    ch=input("enter menu choice: ")

#completing the html code and writing it in the html file
body+="</body>\n</html>"
my_file.write(body)
my_file.close()

    
    
