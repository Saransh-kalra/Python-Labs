#introduce the program
print("welcome to the farheneit to celcius conversion program")
#ask the use for a farheneit temperature
degree_f=float(input("please enter a farheneit temperature: "))
#convert the user's input to celciuys by dividing it by 1.8 and subtracting 32
degree_c=float((degree_f - 32)/1.8)
#print out the result of the calculation
print(degree_f, "farheneit is ", degree_c, "celcius" )
