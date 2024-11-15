from typing import List

list1 = [1,3,4,5,6,7,8,9]

def binary_search(arr: List[int],target:int)->int:
	start = 0
	end = len(arr)-1

	while start<=end:
		mid = (start + end)//2

		if target< arr[mid]:
			end = mid-1
		elif target > arr[mid]:
			start = mid+1
		else:
			return mid

	return -1



print(binary_search(list1,8))

