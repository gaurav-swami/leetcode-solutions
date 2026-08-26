def summ(i,n,total=0):
    if i>n:
        print(total)
        return

    summ(i+1, n, total+i)

summ(1,int(input("Enter a number : ")))
