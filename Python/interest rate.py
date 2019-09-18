def interest(bal, rate, time):
    interest=(bal*(1+(rate/1200))**(12*time))
    print("the interest on " , bal, "at ", rate,"% per annum for ",time, "years is ", interest)

interest(6500,2.36,5)
    
