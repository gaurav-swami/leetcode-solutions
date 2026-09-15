def printtillx(x):
    if x<=0:
        return 
    print(x)
    printtillx(x-1)

printtillx(int(input("Enter a number : ")))
