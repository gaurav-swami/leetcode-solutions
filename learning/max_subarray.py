from typing import List

arr = [1,2,3,4,5]

	
def print_array(arr: List[int]):
	for st in range(0,len(arr)):
		for end in  range(st,len(arr)):
			for i in range(st,end+1):
				print(arr[i], end="")

			print(end = " ")
		print()


def max_sum_bf(arr: List[int])->int:
	add	= 0
	sums = []
	for st in range(0,len(arr)):
		for end in range(st,len(arr)):
			for i in range(st,end+1):
				add += arr[i]
			sums.append([add,st,end])
			add = 0

	return max(sums)

print(max_sum_bf(arr))