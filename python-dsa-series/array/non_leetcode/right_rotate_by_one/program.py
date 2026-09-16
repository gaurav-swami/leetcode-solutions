arr = [1,2,3,4,5,6,7]
n = len(arr)
temp = arr[n-1]
for i in range(n-2,-1,-1):
    arr[i+1] = arr[i]

arr[0] = temp

print(arr)

#time complexity = O(n)
#space complexity = O(1) since we are using the same array 
