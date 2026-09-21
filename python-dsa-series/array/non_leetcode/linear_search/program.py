arr = [1,2,3,4,5,6,7]

def linear_search( arr, n ):
    for i in range(len(arr)):
        if arr[i] == n:
            return n
    return -1


print(linear_search(arr,8)) 
