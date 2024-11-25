from typing import List

arr = [1,2,3,4,5]

	
def print_array(arr: List[int]):
	for st in range(0,len(arr)):
		for end in  range(st,len(arr)):
			for i in range(st,end+1):
				print(arr[i], end="")

			print(end = " ")
		print()



# least optimized with TM : n^3

def max_sum_bf_1(arr: List[int]):
	add	= 0
	sums = []
	for st in range(0,len(arr)):
		for end in range(st,len(arr)):
			for i in range(st,end+1):
				add += arr[i]
			sums.append([add,st,end])
			add = 0

	print( max(sums))

# slightly optimized bf with TM: n^2

def max_sum_bf_2 (arr:List[int]):
	add = 0
	sums = []
	maxi = 0
	for st in range(0,len(arr)):
		add=0	
		for end in range(st,len(arr)):
			add+= arr[end]
			maxi = max(maxi,add)
		
	print(maxi)

# kadane's algo with TM: n


def kadane(arr: List[int]):

	lar_sum=0
	curr_sum=0

	for i in range(0,len(arr)):
		curr_sum += arr[i]
		lar_sum = max(curr_sum,lar_sum)
		if curr_sum<0:
			curr_sum=0

	print(lar_sum)

kadane(arr)