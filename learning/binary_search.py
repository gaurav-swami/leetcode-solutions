from typing import List

def binary_search(arr: List[int], target: int)-> int:
	start = 0
	end = len(arr)-1

	while start<=end:
		mid = (start+end)//2

		if arr[mid] == target:
			return mid

		elif arr[mid]> target:
			end = mid-1
		elif arr[mid]<target:
			start = mid+1


	return -1

arr = [0,3,4,5,9,11,10,]
target = 12

print(binary_search(arr,target)) 
