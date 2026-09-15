def merge_sort(arr,l,r):
    if l>=r:
        return 
    mid = (l+r)//2   #r is the last index not the length so mid+1
    merge_sort(arr,l,mid)
    merge_sort(arr,mid+1,r)
    merge(arr,l,mid,r)

def merge(arr,l,mid,r):
    result = []
    i,j = l,mid+1 #since r is not the length and l = 0 so m+1 

    while i<=mid and j<=r:
        if arr[i]<=arr[j]:
            result.append(arr[i])
            i+=1
        else:
            result.append(arr[j])
            j+=1
    
    while i<=mid:
        result.append(arr[i])
        i+=1
    while j<=r:
        result.append(arr[j])
        j+=1

    for i in range(len(result)):
        arr[l+i] = result[i]   #because we are changing the original array and l might not be 0

arr = [2,3,53,3,7,86,5,54,75,34,65,54,63,22,1]
merge_sort(arr,0,len(arr)-1) 
print(arr) 
