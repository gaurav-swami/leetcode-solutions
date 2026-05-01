from typing import List

def binary_search(arr: List[int], target: int)-> int:
	start = 0
	end = len(arr)-1

	while start<=end:
		mid = start + (end-start)//2

		if arr[mid] > target:
			end = mid-1
		elif arr[mid] < target:
			start = mid+1
		else:
			return mid

	return -1

def binary_search_recursive (arr: List[int],target: int, start: int, end: int  )-> int:
	if  start<=end:
		mid = start + (end-start)//2
		if arr[mid]> target:
			return binary_search_recursive(arr, target, start, mid-1)
		elif arr[mid] < target:
			return binary_search_recursive(arr,target,mid+1, end)
		else:
			return mid
	
	return -1

arr = [0,3,4,5,9,11,12,]
# arr = []
target = 9

print(binary_search(arr,target)) 
print(binary_search_recursive(arr,target,0,len(arr)-1))
