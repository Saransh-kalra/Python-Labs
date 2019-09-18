file1=input("enter the file to be opened: ")
try:
    my_file = open(file1,'r')
except IOError:
    print("this file doesn't exist")

my_file.seek(0)
print(my_file.readline())


