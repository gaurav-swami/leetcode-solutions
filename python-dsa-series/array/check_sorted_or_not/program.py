
def isSorted( arr):
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return False 
    return True 

arr = [1,2,3,4,5]
arr2 = [1,2,1,4,2]

print(isSorted(arr))
print(isSorted(arr2))      
