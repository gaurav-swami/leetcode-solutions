def printx(i,n):
    if i>n:
        return 
    printx(i+1,n)
    print(i)

printx(1,4)
