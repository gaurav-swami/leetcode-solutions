nums = [5,7,8,4,1,6,9,2]

def selection_sort(arr):
  for i in range(len(nums)-1):
    k = i 
    for j in range(i+1, len(nums)):
      if arr[j] < arr[k]:
        k = j
    arr[i],arr[k] = arr[k],arr[i]

  return arr

print(selection_sort(nums))                
