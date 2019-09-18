def factorial(n):
    fact=0
    while(n>0):
        fact*=n
        factorial(n-1)
    print("factorial of a number ",n, "is: ", fact)

factorial(5)
