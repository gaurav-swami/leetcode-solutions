def fibonacci(n,i=0,prev=0,curr=1):
    if i==n:
        return prev
    prev,curr = curr, prev+curr
    
    return fibonacci(n, i+1, prev, curr )


print(fibonacci(7))
        
