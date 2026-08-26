def printx(n):
    if n<=0:
        return 
    printx(n-1)
    print(n)

printx(4)
