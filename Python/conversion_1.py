#introduce the program
print("welcome to the celcius to farheneit conversion program")
#ask the use for a celcius temperature
degree_c=float(input("please enter a celcius temperature: "))
#convert the user's input to farheneit by mukltiplying it by 1.8 and adding 32
degree_f=float(degree_c*1.8 + 32)
#print out the result of the calculation
print(degree_c, "celcius is", degree_f, "farheneit")
