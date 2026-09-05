def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2 
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)
    
def merge(left,right):
    i,j = 0,0
    n,m = len(left), len(right)
    result = []

    while i<n and j <m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i<n:
        result.append(left[i])
        i+=1
    while j<m:
        result.append(right[j])
        j+=1
    return result

arr = [3,5,4,6,6,8,76,9,97,5,4,6,8,9]
print(merge_sort(arr)) 
