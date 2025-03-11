nums = [2, 1, 5, 1, 3, 2]
k = 3

window_1 = 0
for i in range(k):
	window_1+=nums[i]
print(window_1)

max_sum = window_1
for i in range(1,len(nums)-k+1):
	window_0 = window_1+nums[i+k-1]-nums[i-1]
	print('window 0 : ',window_0)
	max_sum = max(window_1,max_sum)
	window_1 = window_0

print(max_sum)

