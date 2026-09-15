arr = [23,2,32,4,34,5434,4,345,3,234]

def second_largest(arr):
    sec = float("-inf") 
    maxx = float("-inf") 

    for i in arr:
        if i > maxx:
            sec = maxx
            maxx = i 
        elif i > sec and i != maxx:
            sec = i
    return sec,maxx

print(second_largest(arr))
