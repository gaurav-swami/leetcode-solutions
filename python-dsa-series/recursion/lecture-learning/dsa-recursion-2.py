def printx(x,n):
    if n<=0:
        return 
    print(x)
    printx(x,n-1)
    
printx(input("Enter a string :"), int(input("Enter the numbers of time : ")))
