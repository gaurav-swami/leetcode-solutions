arr = [2,3,1,6,4,9,8]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        is_swap = False # for better best case optimization` 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swap = True 
        if not is_swap:
            return arr 
    return arr

print(bubble_sort(arr))
