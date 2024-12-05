from typing import List

arr = [2,6,7,11]

def pair_sum_brute(arr: List[int],target: int)->List[int]:

	for i in range(0,len(arr)):
		for j in range(i,len(arr)):
			if arr[i]+arr[j] == target:
				print(i,j)

def pairsum(arr: List[int],target: int):
	i = 0
	j = len(arr)-1
	ps=0
	while i<j:
		ps = arr[i]+arr[j]

		if ps < target:
			i += 1
		elif ps > target:
			j -= 11
		else:
			return i,j
			

print(pairsum(arr,9))
