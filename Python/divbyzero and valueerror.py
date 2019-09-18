try: 
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    c=int(input("enter the third number: "))
    d=a/b+c
except ValueError:
    print("this is not a valid integer input")
except ZeroDivisionError:
    print("you did a division by zero which is invalid")
