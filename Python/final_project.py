#Name: Saransh Kalra
#Course: 1411-505
#Date: 11/30/2017
#
#PROBLEM:
# Write a menu-based program to allow the dietician to input clients and their information.
# The menu should allow the dietician to
# • enter client first and last name, body type, weight, height, age, and level of activity as described in the problem background
# • select a client
#    o determine daily calorie, fat calories, and fat grams needed
#    o choose a menu for breakfast, lunch, and dinner from a list of foods as in the problem background (you may add more to the list if desired) giving total daily food and fat        calories
#    o recommend a reduced calorie intake if the client wishes to lose weight of 10% less calories than the daily calorie need; the reduced fat calories and grams should be given as well
# • edit a client's data
# • remove a client's data
# • exit the program
#
#GIVEN:
# The file containing the clients data
#
#ALGORITHM:
# Dieticians help clients with their caloric intake in order to eat healthier and lose weight if desired.
# To help clients, they need to know
#   • Whether the body type of the client is male or female
#   • The weight of the client in pounds
#   • The height of the client in inches
#   • The age of the client in years
#   • The level of activity of the client as defined by the Harris Benedict Formula
# We use the English Basal Metabolic Rate Formula with the Harris Benedict Formula to determine a client’s daily calorie needs.  The daily fat needs would be 20% to 30% of the daily calorie need, such as if the daily calorie need is 2000 calories, the fat calorie needs would be 400 to 600 fat calories.
# English BMR (Basal Metabolic Rate) Formula
# Women: BMR = 655 + ( 4.35 x weight in pounds ) + ( 4.7 x height in inches ) - ( 4.7 x age in years )
# Men: BMR = 66 + ( 6.23 x weight in pounds ) + ( 12.7 x height in inches ) - ( 6.8 x age in year )
# Harris Benedict Formula (Daily Calorie Need) To determine your total daily calorie needs, multiply the BMR by the appropriate activity factor, as follows:
# 1. If sedentary (little or no exercise) : Calorie-Calculation = BMR x 1.2
# 2. If lightly active (light exercise/sports 1-3 days/week) : Calorie-Calculation = BMR x 1.375
# 3. If moderatetely active (moderate exercise/sports 3-5 days/week) : Calorie-Calculation = BMR x 1.55
# 4. If very active (hard exercise/sports 6-7 days a week) : Calorie-Calculation = BMR x 1.725
# 5. If extra active (very hard exercise/sports & physical job or 2x training) : Calorie-Calculation = BMR x 1.9
#
#METHOD:



#MAIN PROGRAM
import csv

#create a function to calculate calorie requirement
def calorie_req(sex,weight,height,age,activity,choice='0'):
    #calculate bmr according to the whether a person is male or female
    if(sex=='male' or sex=='Male' or sex=='MALE'):
        bmr=66.0+(6.23*float(weight))+(12.7*float(height))-(6.8*float(age))
    elif(sex=='female' or sex=='Female' or sex=='FEMALE'):
        bmr=655.0+(4.35*float(weight))+(4.7*float(height))-(4.7*float(age))
    #calculate calorie requirement according to activity level
    if(activity=='1'):
        cal_req=bmr*1.2
    elif(activity=='2'):
        cal_req=bmr*1.375
    elif(activity=='3'):
        cal_req=bmr*1.55
    elif(activity=='4'):
        cal_req=bmr*1.725
    elif(activity=='5'):
        cal_req=bmr*1.9
    #give user a choice to print the bmr calculated
    if(choice=='1'):
        print("\nBMR is: {:.3f}".format(bmr))
    return cal_req

#created a list to store the records read from the csv file and to store the changes happening
#within the program so that the file need not be read again
diet_data=[] 
valid='0'
#file opened for writing in append mode
a_file=open("diet_data.csv","a")
#file opened for reading in read mode
b_file=open("diet_data.csv","r")
#open csv reader to read from the file 
breader=csv.reader(b_file)
for row in breader:
    #attaching all the records one by one into a sigle list
    diet_data.extend(row)

#open csv writer to write into a csv file with line terminator newline so that every record goes in different line
#and delimiter as comma so as to store all elements of a record as separate
bwriter=csv.writer(a_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

#Will only exit when the exit option i.e. 6 will be entered in option as valid will be 1
while(valid=='0'):
    #created a list to store the new record to be entered to the file
    input_lst=[]
    #declared a list to hold a record read from a file to print it on screen
    lst1=[]
    valid1='1'
    valid2='0'
    valid3='0'
    valid5='0'
    count1='0'
    #counter to count till 7 i.e the length of a record so that all records can be printed separately
    count=int(count1)
    option=0
    option1=0
    
    #Displaying the main menu
    print("\nWELCOME TO THE DIETICIAN SERVICES SYSTEM")
    print("-----------------------------------------")
    print("SELECT ONE OF THE OPTIONS BELOW: ")
    print("1. View the existing client's database ")
    print("2. Enter a client's data")
    print("3. Select a client")
    print("4. Edit a client's data")
    print("5. Delete a client's data")
    print("6. Exit the program")

    #prompt the user for his/her choice in the menu
    option=input("\nEnter your choice: ")
    print('')

    #if option is 1 print all the existing data read from the file
    if(option=='1'):
        print("LIST OF ALREADY EXISTING CLIENTS WITH THEIR DATA")
        print("-------------------------------------------------")
        #iterating through the whole list after 7 terms i.e. a record, line changes so that new record in newline
        for item in diet_data:
            lst1.append(item)
            count=count+1
            if(count%7==0):
                print(lst1)
                lst1=[]

    #if option is 2 prompt the user for the data of a new client to be input into the file as a new record
    elif(option=='2'):
        #will only break the the loop when all of the inputs are valid and the bmr is not negative its a valid record
        while(valid1=='1'):
            val1='0'
            val2='0'
            val3='0'
            val4='0'
            val5='0'
            val6='0'
            val7='0'

            #will only break the loop when the first name enetered is valid
            while(val1!='1'):
                first_name=input("What is the client's first name?: ")
                #if the first_name has anything else other than letters print error
                if(not first_name.isalpha()):
                    print("\nThe first name should only contains alphabets\n")
                #if its correct break the loop
                else:
                    val1='1'

            #will only break the loop when the last name enetered is valid
            while(val2!='1'):
                last_name=input("What is the client's last name?: ")
                #if the last_name has anything else other than letters print error
                if(not last_name.isalpha()):
                    print("\nThe last name should only contains alphabets\n")
                #if its correct break the loop
                else:
                    val2='1'

            #will only break the loop when the sex enetered is valid
            while(val3!='1'):                            
                sex=input("What is client's sex? (male/female): ")
                #if sex is anything other than male or female give an error
                if((sex!='male' and sex!='Male' and sex!='MALE' and sex!='female' and sex!='Female' and sex!='FEMALE')):
                    print("\nThe sex can only be male/female\n")
                #if its correct break the loop
                else:
                    val3='1'

            #will only break the loop when the weight enetered is valid and in range
            while(val4!='1'):
                weight=input("What is the client's weight? (in 0 to 400 pounds): ")
                #validate the weight if its a float value or not
                try:
                    weight1=float(weight)
                #if its not print an error
                except ValueError:
                    print("\nThe weight can only be decimal values\n")
                else:
                    #if it is then validate it for the value being in range if its not print an error
                    if(float(weight)<0.0 or float(weight)>400.0):
                        print("\nWeight can only be between 0 to 400 pounds\n")
                    #if its valid and in range break the loop
                    else:
                        val4='1'

            #will only break the loop when the height enetered is valid and in range
            while(val5!='1'):                    
                height=input("What is the client's height? (in 0 to 120 inches): ")
                #validate the height if its a float value or not
                try:
                    height1=float(height)
                #if its not print an error
                except ValueError:
                    print("\nThe height can only be decimal values\n")
                else:
                    #if it is then validate it for the value being in range if its not print an error
                    if(float(height)<0.0 or float(height)>120.0):
                        print("\nHeight can only be between 0 to 120 inches\n")
                    #if its valid and in range break the loop
                    else:
                        val5='1'

            #will only break the loop when the age enetered is valid and in range
            while(val6!='1'):
                age=input("What is the client's age? (in 0 to 120 years): ")
                #validate the age if its a float value or not
                try:
                    age1=float(age)
                #if its not print an error
                except ValueError:
                    print("\nThe age can only be decimal values\n")
                else:
                    #if it is then validate it for the value being in range if its not print an error
                    if(float(age)<0.0 or float(age)>120.0):
                        print("\nAge can only be between 0 to 120 years\n")
                    #if its valid and in range break the loop
                    else:
                        val6='1'

            #will only break the loop when the activity enetered is valid and in range
            while(val7!='1'):                   
                activity=input("On a scale of 1 to 5 how active is the client?: ")
                #validate the activity if its a integer value or not
                try:
                    activity1=int(activity)
                #if its not print an error
                except ValueError:
                    print("\nThe activity can only have integer values\n")
                else:
                    #if it is then validate it for the value being in range if its not print an error
                    if(int(activity)<1 or int(activity)>5):
                        print("\nActivity can only be between 1 to 5\n")
                    #if its valid and in range break the loop
                    else:
                        val7='1'

            #validate bmr to be positive for male
            if(sex=='male' or sex=='Male' or sex=='MALE'):
                #if bmr comes out to be negative give error message
                if (66.0+(6.23*float(weight))+(12.7*float(height))-(6.8*float(age))<0.0):
                    valid1='1'
                    print("\nThe data you entered is wrong, a man with those data can't exist, bmr comes out to be negative")
                    print("\nPlease input the data again! \n")
                #if its positive then data is valid break out of the final loop after writing the data to the file
                else:
                    valid1='0'

            #validate bmr to be positive for male
            elif(sex=='female' or sex=='Female' or sex=='FEMALE'):
                #if bmr comes out to be negative give error message
                if (655.0+(4.35*float(weight))+(4.7*float(height))-(4.7*float(age))<0.0):
                    valid1='1'
                    print("\nThe data you entered is wrong, a woman with those data can't exist, bmr comes out to be negative")
                    print("\nPlease input the data again! \n")
                #if its positive then data is valid break out of the final loop after writing the data to the file
                else:
                    valid1='0'

            #if valid1 is zero means everything is valid then write the data in the list keeping record in progra and to the file
            if(valid1=='0'):
                input_lst.append(first_name)
                input_lst.append(last_name)
                input_lst.append(sex)
                input_lst.append(weight)
                input_lst.append(height)
                input_lst.append(age)
                input_lst.append(activity)

                bwriter.writerow(input_lst)
                diet_data.extend(input_lst)

            
    #if option is 3 give the user chance to select a client and then select an action for it from another sub menu
    elif(option=='3'):
        calories1='0'
        valid4='0'
        val12='0'
        valid10='0'
        #variable to store the final index of the record found
        index_found2=int(x=0)
        count1='0'
        count2=int(count1)
        count6='0'
        count7=int(count6)
        # variable which stores calories in the food menu
        calories=int(calories1)
        #variable for checking if a record has been found or not
        found='0'
        #variable acting as a temp variable to store indexes of records found during the iters\ation
        index_found=-1
        #list for storing the food items chosen by the user for the food menu
        lst=[]
        #list for storing indexs of the records found during iteration
        index_lst=[]
        #variable for storing the serial number
        ch=''

        #loop runs until the record is not found
        while(found=='0'):
            #validates the last name entered by the user to not contain anything other than characters
            while(valid10=='0'):
                name_search=input("Enter the last name of the client whose information you want: ")
                if(not name_search.isalpha()):
                    print("\nThe last name can only contains alphabets\n")
                else:
                    valid10='1'
            #iterating through the records to find the last name
            for name1 in diet_data:
                if(name1==name_search):
                    index_found=count7
                    #condition to not count the records whose first name is the last name searched as one index before it would have some number
                    if(diet_data[index_found-1].isalpha()):
                        index_lst.append(index_found)
                        #using the counter count2 to keep record of records found with that last name
                        count2+=1
                        found='1'
                #using the counter count7 to determine the index of the current record during iteration
                count7+=1
            length=len(index_lst)

            #if found is still zero means client was not found indicate that to the user
            if(found=='0'):
                print("\nno such client found\n")
                found='1'

            #if found check the length of the index_str to deteremine if we have more than one records found with thw same last name
            else:
                #if length is greater than 1 give the user the choice to choose the one he/she wants
                if(length>1):
                    print("\nThere are ",count2," clients found in the system with the last name you entered\n")
                    count3='0'
                    count4=int(count3)
                    #print all the client's found with all their data for letting the user make an informed choice
                    for n in index_lst:
                        count4+=1
                        print(count4,".")
                        print("First name: ",diet_data[n-1])
                        print("Last_name: ",diet_data[n])
                        print("Sex: ",diet_data[n+1])
                        print("Weight: ",diet_data[n+2])
                        print("Height: ",diet_data[n+3])
                        print("Age: ",diet_data[n+4])
                        print("Activity",diet_data[n+5])
                        print("\n")

                    #the loop will break only when the serial number entered is an integer and in range
                    while(val12!='1'):                
                        ch=input("Enter the client's serial number in the list to indicate which one u want to select: ")
                        #if the serial number entered is not an integer give an error
                        try:
                            ch1=int(ch)
                        except ValueError:
                            print("the serial number must be an integer, please try again! ")
                        #if it is check if its in range
                        else:
                            #if the serial number entered is greater than the length of the index list i.e. greater than the records found gives an error
                            if(int(ch)>length):
                                print("Serial number is out of range [1 to",count4,"], Try again!")
                            #else breaks out of the loop
                            else:
                                index_found2=int(index_lst[int(ch)-1])
                                val12='1'
                #if not no need to enter serial number or display data just put the first index stored into the variable which stores final index
                else:
                    index_found2=int(index_lst[0])

                #loop doesn't break until the user presses the exit option in the sub menu
                while(valid2=='0'):
                    lst=[]
                    valid3='0'
                    valid4='0'
                    calories=0
                    #variable for storing the fat grams the food menu provides
                    fatgram=int(x=0)
                    #print the sub menu
                    print("\nSELECT ONE OF THE OPTIONS BELOW FOR \"{} {}\":".format(diet_data[index_found2-1].upper(),diet_data[index_found2].upper()))
                    print("1. Determine daily calorie need, fat colories and fat grams needed ")
                    print("2. Choose a menu for breakfast, lunch and dinner ")
                    print("3. Recommend a reduced calorie intake if weight loss desired ")
                    print("4. Back to main menu ")

                    option1=input("\nEnter your choice: ")
                    
                    #if option1 is 1 display the fat grams needed, daily calorie need and the daily fat calorie need
                    if(option1=='1'):
                        #store calorie requirement in cal_req by passing the sex, weight,height,age,acticity of the record selected
                        #to get its calculated calorie need and '1' is passed to show the bmr calculated
                        cal_req=calorie_req(diet_data[index_found2+1],diet_data[index_found2+2],diet_data[index_found2+3],diet_data[index_found2+4],diet_data[index_found2+5],'1')
                        print("\nThe daily calorie need is: {:.3f}".format(cal_req))
                        print("Daily fat calorie need is from 20% ({:.3f}) to 30% ({:.3f}) of the daily calorie need".format(0.2*cal_req,0.3*cal_req))
                        print("In fat grams from {:.3f} to {:.3f} grams daily".format((0.2*cal_req)/9,(0.3*cal_req)/9))

                    #if option1 is 2 then provide the user a menu for choosing a food menu for the client selected
                    elif(option1=='2'):
                        #loop doesn't break until it gets yes or no as an answer from the user
                        while(valid4=='0'):
                            cal_req=calorie_req(diet_data[index_found+1],diet_data[index_found+2],diet_data[index_found+3],diet_data[index_found+4],diet_data[index_found+5])
                            #ask the user if the client wishes to lose weight
                            ch=input("\nDoes the patient want to lose weight? (y/n): ")
                            #if yes the calorie requirement becomes 90%
                            if(ch=='y' or ch=='Y'):
                                cal_req1=0.9*cal_req
                                valid4='1'
                            #if not the calorie requirement remains as calculated for the record
                            elif(ch=='n' or ch=='N'):
                                cal_req1=cal_req
                                valid4='1'
                            #print an error if its not a yes or no
                            else:
                                print("\nInvalid choice, try again!")

                        #loop does not break until the user is done with list and presses 11 and the calorie requirement is met
                        while(valid3=='0'):
                            #print the menu containing the food, calories it provides and fat grams it has
                            print("\nCHOOSE FROM THE LIST BELOW")
                            print("---------------------------")
                            print("FOODS (TOTAL CALORIES, FATS IN GRAMS)")
                            print("1. French Fries, 570 ,30")
                            print("2. Onion Rings, 350, 16")
                            print("3. Hamburger, 670, 39")
                            print("4. Cheeseburger, 760, 47")
                            print("5. Grilled Chicken Sandwich, 420, 10")
                            print("6. Egg Biscuit, 300, 12")
                            print("7. Mozzarella Sticks, 849, 56")
                            print("8. Cheese Pizza, 300, 11")
                            print("9. Macroni and Cheese, 300, 7")
                            print("10. Glazed Chicken and Veggies, 497, 7")
                            print("11. Done with the list")
                            
                            option2=input("\nEnter item number: ")

                            #corresponding to the number in the menu whichever option the user enters, the corresponding food item
                            #gets added to the food list and the calories it provides get added to variable calories and the fat grams
                            #it has gets added to the variable fatgram to indicate the calories and fatgrms the menu provides
                            
                            if(option2=='1'):
                                lst.append("French Fries")
                                calories+=570
                                fatgram+=30
                                
                            elif(option2=='2'):
                                lst.append("Onion Rings")
                                calories+=350
                                fatgram+=16
                                
                            elif(option2=='3'):
                                lst.append("Hamburger")
                                calories+=670
                                fatgram+=39
                                
                            elif(option2=='4'):
                                lst.append("Cheeseburger")
                                calories+=760
                                fatgram+=47
                                
                            elif(option2=='5'):
                                lst.append("Grilled Chicken Sandwich")
                                calories+=420
                                fatgram+=10
                                
                            elif(option2=='6'):
                                lst.append("Egg Biscuit")
                                calories+=300
                                fatgram+=12
                                
                            elif(option2=='7'):
                                lst.append("Mozzarella Sticks")
                                calories+=849
                                fatgram+=56
                                
                            elif(option2=='8'):
                                lst.append("Cheese Pizza")
                                calories+=300
                                fatgram+=11
                                
                            elif(option2=='9'):
                                lst.append("Macroni and Cheese")
                                calories+=300
                                fatgram+=7
                                
                            elif(option2=='10'):
                                lst.append("Glazed Chicken and Veggies")
                                calories+=497
                                fatgram+=7

                            #if option2 is 11 print the menu prepared till now
                            elif(option2=='11'):
                                print("\nHere is the menu you prepared\n")
                                for item in lst:
                                    print(item)

                                #print the number of calories and fat grams the menu provides and the calorie and fat grams the client selected need
                                print("\nThe number of calories this menu provides is: {:} and the patient needs: {:.3f} calories".format(calories, cal_req1))
                                print("\nThe Fat grams this menu provides is: {:} and patient needs fat grams between {:.3f} to {:.3f} grams daily".format(fatgram,(0.2*cal_req1)/9,(0.3*cal_req1)/9))

                                #if calorie requirement is met exit the loop
                                if(calories>=cal_req1):
                                    valid3='1'

                                #if its not met give an error that it doesn't meet the calorie need add something else to the menu in order to meet the calorie need
                                else:
                                    print("\nThis list doesn't meet the requirements add something else")

                            #if the option2 entered is other than the 11 give the user an error message
                            else:
                                print("\nInvalid choice, try again!")

                            #if the option2 is not 11 and the calorie requirement is already met give a warning to the user that the calorie need is already fulfilled
                            #adding anything else exceeds the calorie need
                            if(calories>=cal_req1 and option2!='11'):
                                print("\nWARNING: If you add something else to the menu, the calorie need is already fulfilled, those would count as extra calories")

                    #if the option1 chosen is 3 print the calorie requirement if the client needs to lose weight i.e 90% of the daily need
                    #and print the fat calories needed daily and fat grams needed daily in order to lose weight
                    elif(option1=='3'):
                        cal_req=calorie_req(diet_data[index_found2+1],diet_data[index_found2+2],diet_data[index_found2+3],diet_data[index_found2+4],diet_data[index_found2+5],'1')
                        print("\nThe daily calorie need if the patient needs to lose weight is: {:.3f}".format(cal_req*0.9))
                        print("Daily calorie need is from 20% ({:.3f}) to 30% ({:.3f}) of the daily calorie need".format(0.2*0.9*cal_req,0.3*0.9*cal_req))
                        print("In fat grams from {:.3f} to {:.3f} grams daily".format((0.2*0.9*cal_req)/9,(0.3*0.9*cal_req)/9))

                    #if option1 chosen is 4, exit the loop
                    elif(option1=='4'):
                        valid2='1'
                    #if any other option1 give error nessage
                    else:
                        print("\nInvalid choice, try again!")

    #if option is 4 ask the user which record he wants to edit
    elif(option=='4'):
        # variable being used for validating all the modified entries
        valid34='0'
        val1='0'
        #a list for storing all the elements of the edited record
        new_lst=[]
        valid1='1'
        valid10='0'
        #variable to store the final index of the record found
        index_found2=int(x=0)
        count1='0'
        count2=int(count1)
        count6='0'
        count7=int(count6)
        #variable for checking if a record has been found or not
        found='0'
        #variable for checking if a record has been found or not
        index_found=-1
        val12='0'
        #list for storing indexs of the records found during iteration
        index_lst=[]
        #variable for storing the serial number
        ch=''

        #loop runs until the record is not found
        while(found=='0'):
            #validates the last name entered by the user to not contain anything other than characters
            while(valid10=='0'):
                name_search=input("Enter the last name of the client whose information you want: ")
                if(not name_search.isalpha()):
                    print("\nThe last name can only contains alphabets\n")
                else:
                    valid10='1'
            #iterating through the records to find the last name
            for name1 in diet_data:
                if(name1==name_search):
                    index_found=count7
                    #condition to not count the records whose first name is the last name searched as one index before it would have some number
                    if(diet_data[index_found-1].isalpha()):
                        index_lst.append(index_found)
                        #using the counter count2 to keep record of records found with that last name
                        count2+=1
                        found='1'
                #using the counter count7 to determine the index of the current record during iteration
                count7+=1
            length=len(index_lst)

            #if found is still zero means client was not found indicate that to the user
            if(found=='0'):
                print("\nno such client found\n")
                found='1'

            #if found check the length of the index_str to deteremine if we have more than one records found with the same last name
            else:
                #if length is greater than 1 give the user the choice to choose the one he/she wants
                if(length>1):
                    print("\nThere are ",count2," clients found in the system with the last name you entered\n")
                    count3='0'
                    count4=int(count3)
                    #print all the client's found with all their data for letting the user make an informed choice
                    for n in index_lst:
                        count4+=1
                        print(count4,".")
                        print("First name: ",diet_data[n-1])
                        print("Last_name: ",diet_data[n])
                        print("Sex: ",diet_data[n+1])
                        print("Weight: ",diet_data[n+2])
                        print("Height: ",diet_data[n+3])
                        print("Age: ",diet_data[n+4])
                        print("Activity",diet_data[n+5])
                        print("\n")
                        
                    #the loop will break only when the serial number entered is an integer and in range
                    while(val12!='1'):                
                        ch=input("Enter the client's serial number in the list to indicate which one u want to select: ")
                        #if the serial number entered is not an integer give an error
                        try:
                            ch1=int(ch)
                        except ValueError:
                            print("the serial number must be an integer, please try again! ")
                        #if it is check if its in range
                        else:
                            #if the serial number entered is greater than the length of the index list i.e. greater than the records found gives an error
                            if(int(ch)>length):
                                print("Serial number is out of range [1 to",count4,"], Try again!")
                            #else breaks out of the loop
                            else:
                                index_found2=int(index_lst[int(ch)-1])
                                val12='1'
                #if not no need to enter serial number or display data just put the first index stored into the variable which stores final index
                else:
                    index_found2=int(index_lst[0])         

                #now variable ch is used to store yes or no for changing the value
                ch=''

                #loop doesn't break until the selected record gets edited correctly and is valid
                while(valid1=='1'):
                    val1='0'
                    val2='0'
                    val3='0'
                    val4='0'
                    val5='0'
                    val6='0'
                    val7='0'
                    print("\nENTER THE NEW DETAILS OF THE PERSON YOU SELECTED")
                    print("------------------------------------------------")

                    #loops to validate each entry (refer option 1 same as it was) like first and last name should be strings height,weight,age should be float and activity
                    #should be integer
                    #ensured height,weight,age,activity are in range
                    #show recorded value
                    #ask the user if he wants to change this value
                    #if yes then take valid input and append it in new_lst
                    #if no then append the old value in new_lst
                    #if anything other than yes or no error message printed
                    
                    while (valid34=='0'):
                        print("\nThe recorded first name is: ",diet_data[index_found2-1])
                        ch=input("\nDo you wish to change this value? (yes/no): ")
                        if(ch=='yes'):
                            while(val1!='1'):
                                first_name=input("\nWhat is the client's modified first name?: ")
                                if(not first_name.isalpha()):
                                    print("\nThe first name should only contains alphabets\n")
                                else:
                                    val1='1'
                            valid34='1'
                            new_lst.append(first_name)
              
                        elif(ch=='no'):
                            new_lst.append(diet_data[index_found2-1])
                            valid34='1'

                        else:
                            print("\nInvalid choice, try again!")
                            valid34='0'

                    valid34='0'
                    ch=''

                    while (valid34=='0'):
                        print("\nThe recorded last name is: ",diet_data[index_found2])
                        ch=input("\nDo you wish to change this value? (yes/no): ")
                        if(ch=='yes'):
                            while(val2!='1'):
                                last_name=input("\nWhat is the client's modified last name?: ")
                                if(not last_name.isalpha()):
                                    print("\nThe last name should only contains alphabets\n")
                                else:
                                    val2='1'
                            new_lst.append(last_name)
                            valid34='1'
              
                        elif(ch=='no'):
                            new_lst.append(diet_data[index_found2])
                            valid34='1'
              
                        else:
                            print("\nInvalid choice, try again!")
                            valid34='0'

                    valid34='0'
                    ch=''

                    while (valid34=='0'):
                        print("\nThe recorded sex is: ",diet_data[index_found2+1])
                        ch=input("\nDo you wish to change this value? (yes/no): ")
                        if(ch=='yes'):
                            while(val3!='1'):                            
                                sex=input("\nWhat is client's modified sex? (male/female): ")
                                if((sex!='male' and sex!='Male' and sex!='MALE' and sex!='female' and sex!='Female' and sex!='FEMALE')):
                                    print("\nThe sex can only be male\/female\n")
                                else:
                                    val3='1'
                            new_lst.append(sex)
                            valid34='1'
                            
                        elif(ch=='no'):
                            new_lst.append(diet_data[index_found2+1])
                            valid34='1'
                            sex=diet_data[index_found2+1]

                        else:
                            print("\nInvalid choice, try again!")
                            valid34='0'
            
                    valid34='0'
                    ch=''
              
                    while (valid34=='0'):
                        print("\nThe recorded weight is: ",diet_data[index_found2+2])
                        ch=input("\nDo you wish to change this value? (yes/no): ")
                        if(ch=='yes'):
                            while(val4!='1'):
                                weight=input("\nWhat is the client's modified weight? (in 0 to 400 pounds): ")
                                try:
                                    weight1=float(weight)
                                except ValueError:
                                    print("\nThe weight can only be decimal values\n")
                                else:
                                    if(float(weight)<0.0 or float(weight)>400.0):
                                           print("\nWeight can only be between 0 to 400 pounds\n")
                                    else:
                                       val4='1'
                            new_lst.append(weight)
                            valid34='1'
                           
                        elif(ch=='no'):
                            new_lst.append(diet_data[index_found2+2])
                            valid34='1'
                            weight=diet_data[index_found2+2]

                        else:
                            print("\nInvalid choice, try again!")
                            valid34='0'

                    valid34='0'
                    ch=''
              
                    while (valid34=='0'):
                        print("\nThe recorded height is: ",diet_data[index_found2+3])
                        ch=input("\nDo you wish to change this value? (yes/no): ")
                        if(ch=='yes'):
                            while(val5!='1'):                    
                                height=input("\nWhat is the client's modified height? (in 0 to 120 inches): ")
                                try:
                                    height1=float(height)
                                except ValueError:
                                    print("\nThe height can only be decimal values\n")
                                else:
                                    if(float(height)<0.0 or float(height)>120.0):
                                        print("\nHeight can only be between 0 to 120 inches\n")
                                    else:
                                        val5='1'
                            new_lst.append(height)
                            valid34='1'
                            
                        elif(ch=='no'):
                            new_lst.append(diet_data[index_found2+3])
                            valid34='1'
                            height=diet_data[index_found2+3]

                        else:
                            print("\nInvalid choice, try again!")
                            valid34='0'

                    valid34='0'
                    ch=''
              
                    while (valid34=='0'):
                        print("\nThe recorded age is: ",diet_data[index_found2+4])
                        ch=input("\nDo you wish to change this value? (yes/no): ")
                        if(ch=='yes'):
                            while(val6!='1'):
                                age=input("\nWhat is the client's modified age? (in 0 to 120 years): ")
                                try:
                                    age1=float(age)
                                except ValueError:
                                    print("\nThe age can only be decimal values\n")
                                else:
                                    if(float(age)<0.0 or float(age)>120.0):
                                        print("\nAge can only be between 0 to 120 years\n")
                                    else:
                                        val6='1'
                            new_lst.append(age)
                            valid34='1'
                            
                        elif(ch=='no'):
                            new_lst.append(diet_data[index_found2+4])
                            valid34='1'
                            age=diet_data[index_found2+4]

                        else:
                            print("\nInvalid choice, try again!")
                            valid34='0'

                    valid34='0'
                    ch=''
              
                    while (valid34=='0'):
                        print("\nThe recorded activity is: ",diet_data[index_found2+5])
                        ch=input("\nDo you wish to change this value? (yes/no): ")
                        if(ch=='yes'):
                            while(val7!='1'):                   
                                activity=input("\nOn a scale of 1 to 5 what is the modified activity of the client?: ")
                                try:
                                    activity1=int(activity)
                                except ValueError:
                                    print("\nThe activity can only have integer values\n")
                                else:
                                    if(int(activity)<1 or int(activity)>5):
                                        print("\nActivity can only be between 1 to 5\n")
                                    else:
                                        val7='1'
                            new_lst.append(activity)
                            valid34='1'
                            
                        elif(ch=='no'):
                             new_lst.append(diet_data[index_found2+5])
                             valid34='1'

                        else:
                            print("\nInvalid choice, try again!")
                            valid34='0'

                    #if for male sex the bmr comes out to be negative error message given and asked to input whole data again
                    if(sex=='male' or sex=='Male' or sex=='MALE'):
                        if (66.0+(6.23*float(weight))+(12.7*float(height))-(6.8*float(age))<0.0):
                            valid1='1'
                            print("\nThe data you entered is wrong, a man with those data can't exist, bmr comes out to be negative")
                            print("\nPlease input the data again! \n")
                        else:
                            valid1='0'

                    #if for female sex the bmr comes out to be negative error message given and asked to input whole data again
                    elif(sex=='female' or sex=='Female' or sex=='FEMALE'):
                        if (655.0+(4.35*float(weight))+(4.7*float(height))-(4.7*float(age))<0.0):
                            valid1='1'
                            print("\nThe data you entered is wrong, a woman with those data can't exist, bmr comes out to be negative")
                            print("\nPlease input the data again! \n")
                        else:
                            valid1='0'
                    #if everything is valid then final step
                    if(valid1=='0'):
                        #closed the file which was opened in append mode
                        a_file.close()
                        #opened the file in write mode so it wipes all data and write the file again with the edited record
                        a_file=open("diet_data.csv","w")
                        #declare csv writer again as it file mode has been changed
                        bwriter=csv.writer(a_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

                        #edit the record in the main list of the program keeping the records as this would be written to the file
                        diet_data[index_found2-1]=new_lst[0]
                        diet_data[index_found2]=new_lst[1]
                        diet_data[index_found2+1]=new_lst[2]
                        diet_data[index_found2+2]=new_lst[3]
                        diet_data[index_found2+3]=new_lst[4]
                        diet_data[index_found2+4]=new_lst[5]
                        diet_data[index_found2+5]=new_lst[6]

                        #print the modified record
                        print("Now the modified record is: ",new_lst)

                        #temporary list declared to keep one record during iteration
                        lst1=[]
                        count2=0

                        #loop to read through elements of the list and after reading 7 elements using the counter print write that as one record to the file
                        for item in diet_data:
                            lst1.append(item)
                            count2=count2+1
                            if(count2%7==0):
                                bwriter.writerow(lst1)
                                lst1=[]

                        #close the file which was opened in write mode
                        a_file.close()
                        #open the file again in append mode for further opperations
                        a_file=open("diet_data.csv","a")
                        #declare csv writer again as it file mode has been changed
                        bwriter=csv.writer(a_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                        count2=0

    #if option chosen is 5 then delete a clients data
    elif(option=='5'):
        valid10='0'
        val='1'
        #declare a list to store the new updated list without the deleted record
        diet_data2=[]
        #variable to store the final index of the record found
        index_found2=int(x=0)
        count1='0'
        count2=int(count1)
        count6='0'
        count7=int(count6)
        #variable for checking if a record has been found or not
        found='0'
        #variable for checking if a record has been found or not
        index_found=-1
        val12='0'
        #list for storing indexs of the records found during iteration
        index_lst=[]
        #variable for storing the serial number
        ch=''

        #loop runs until the record is not found
        while(found=='0'):
            #validates the last name entered by the user to not contain anything other than characters
            while(valid10=='0'):
                name_search=input("Enter the last name of the client whose information you want: ")
                if(not name_search.isalpha()):
                    print("\nThe last name can only contains alphabets\n")
                else:
                    valid10='1'
            #iterating through the records to find the last name
            for name1 in diet_data:
                if(name1==name_search):
                    index_found=count7
                    #condition to not count the records whose first name is the last name searched as one index before it would have some number
                    if(diet_data[index_found-1].isalpha()):
                        index_lst.append(index_found)
                        #using the counter count2 to keep record of records found with that last name
                        count2+=1
                        found='1'
                #using the counter count7 to determine the index of the current record during iteration
                count7+=1
            length=len(index_lst)

            #if found is still zero means client was not found indicate that to the user
            if(found=='0'):
                print("\nno such client found\n")

            #if found check the length of the index_str to deteremine if we have more than one records found with the same last name
            else:
                #if length is greater than 1 give the user the choice to choose the one he/she wants
                if(length>1):
                    print("\nThere are ",count2," clients found in the system with the last name you entered\n")
                    count3='0'
                    count4=int(count3)
                    #print all the client's found with all their data for letting the user make an informed choice
                    for n in index_lst:
                        count4+=1
                        print(count4,".")
                        print("First name: ",diet_data[n-1])
                        print("Last_name: ",diet_data[n])
                        print("Sex: ",diet_data[n+1])
                        print("Weight: ",diet_data[n+2])
                        print("Height: ",diet_data[n+3])
                        print("Age: ",diet_data[n+4])
                        print("Activity",diet_data[n+5])
                        print("\n")
                        
                    #the loop will break only when the serial number entered is an integer and in range
                    while(val12!='1'):                
                        ch=input("Enter the client's serial number in the list to indicate which one u want to select: ")
                        #if the serial number entered is not an integer give an error
                        try:
                            ch1=int(ch)
                        except ValueError:
                            print("the serial number must be an integer, please try again! ")
                        #if it is check if its in range
                        else:
                            #if the serial number entered is greater than the length of the index list i.e. greater than the records found gives an error
                            if(int(ch)>length):
                                print("Serial number is out of range [1 to",count4,"], Try again!")
                            #else breaks out of the loop
                            else:
                                index_found2=int(index_lst[int(ch)-1])
                                val12='1'
                #if not no need to enter serial number or display data just put the first index stored into the variable which stores final index
                else:
                    index_found2=int(index_lst[0])

            ch=''
            val2='1'

            #print the record chosen by the user
            print("\nThe record you choose is:")
            print("\nFirst Name: ",diet_data[index_found2-1])
            print("Last Name: ",diet_data[index_found2])
            print("Sex: ",diet_data[index_found2+1])
            print("Weight: ",diet_data[index_found2+2])
            print("Height: ",diet_data[index_found2+3])
            print("Age: ",diet_data[index_found2+4])
            print("Activity: ",diet_data[index_found2+5])

            #loop breaks when it recieves yes or no as an answer
            while(val2=='1'):
                #confirm whether he wants to delete it or not surely
                ch=input("\nAre you sure you want to delete this? (yes/no): ")

                #if no then tell user record not deleted and exit
                if(ch=='no'):
                    print("\nThe record is not deleted....")
                    val2='0'

                #if yes then delete the record
                elif(ch=='yes'):
                    count4=int(x=0)
                    #iterating through the elements of the list
                    for item in diet_data:
                        #except the deleted record everything else gets written to a new list
                        if(count4!=index_found2-1 and count4!=index_found2 and count4!=index_found2+1 and count4!=index_found2+2
                           and count4!=index_found2+3 and count4!=index_found2+4 and count4!=index_found2+5):
                            diet_data2.append(item)
                        count4+=1
                    val2='0'
                    print("\nThe record deleted....")
                    #closed the file which was opened in append mode
                    a_file.close()
                    #opened the file in write mode so it wipes all data and write the file again with the edited record
                    a_file=open("diet_data.csv","w")
                    #declare csv writer again as it file mode has been changed
                    bwriter=csv.writer(a_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

                    #temporary list declared to keep one record during iteration
                    lst1=[]
                    count2=0

                    #loop to read through elements of the list and after reading 7 elements using the counter write that as one record to the file
                    for item in diet_data2:
                        lst1.append(item)
                        count2=count2+1
                        if(count2%7==0):
                            bwriter.writerow(lst1)
                            lst1=[]

                    #close the file which was opened in write mode
                    a_file.close()
                    #open the file again in append mode for further opperations
                    a_file=open("diet_data.csv","a")
                    #declare csv writer again as it file mode has been changed
                    bwriter=csv.writer(a_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
                    count2=0
                    #for further use of program update the old list with the new list
                    diet_data=diet_data2[:]
                #if not yes or no print error message
                else:
                    print("Invalid choice, Try again!")
                    val2='1'
                    

    #if the option chosen is 6 give the closing message and exit the loop
    elif(option=='6'):
        print("Thank you for using this system! ")
        valid='1'

    #if any other option give eroor message
    else:
        if(option!='1' or option!='2' or option!='3' or option!='4' or option!='5' or option!='6'):
            print("Invalid choice, Try again! ")

#close both the file in reading and append mode
a_file.close()
b_file.close()

