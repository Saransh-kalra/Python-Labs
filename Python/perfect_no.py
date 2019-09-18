num=int(input("enter the number: "))
sum=0
for i in range(1, (num//2)+1):
    if num%i==0:
        sum+=i
if sum==num:
    print("perfect")
elif  sum<num:
    print("deficient")
else:
    print("abundant")
