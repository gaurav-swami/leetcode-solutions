def printtillx(x):
    if x<=0:
        return 
    printtillx(x-1)
    print(x)

printtillx(int(input("Enter a number : ")))
