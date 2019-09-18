def mystery (n):
    if n <= 1:
        print(n,end='')
    else:
        mystery(n//2)
    print(',',n,end='')

mystery(1)
mystery(4)
mystery(100)
