from typing import List

def mostwater(height: List[int])->int:
	water = []
	left = 0
	right = 0
	add = 0

	while right < len(height):
		if height[right] > height[left]:
			water.append(add)
			add = 0
			left = right
			right += 1 
			continue


		add = add + (height[left]-height[right])
	
		right += 1

	return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
height2 = [4,2,0,3,2,5]
height3 = []

print(mostwater(height3))


