from typing import List

list1 = [1,3,5,6]

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


def binary_search_recursive (arr:List[int], target: int,start:int,end:int)->int:
	if start<=end:
		mid = (start + end)//2

		if target < arr[mid]:
			return binary_search_recursive(arr,target,start,mid-1)

		elif target > arr[mid]:
			return binary_search_recursive(arr,target,mid+1,end)

		else:
			return mid
	return -1





def binary_search_recursive2 (arr: List[int],target: int, start:int, end:int)->int:
	mid = start + (end-start)//2

	if start<=end:
			# if start == end and target != arr[mid]:
			# if target > arr[mid]:
			# 	return mid+1
			# else:
			# 	return mid

		if arr[mid] > target:
			if mid-1 == -1:
				return mid
			elif arr[mid-1]<target:
				return mid
			else:
				return binary_search_recursive2(arr,target,start,mid-1)
		
		elif arr[mid]<target:
			if mid+1 >= len(arr):
				return mid+1
			elif arr[mid+1] >target:
				return mid+1
			else:
				return binary_search_recursive2(arr,target,mid+1,end)
		
		else:
			return mid

	return -1



print(binary_search_recursive2(list1,7,0,len(list1)-1))

