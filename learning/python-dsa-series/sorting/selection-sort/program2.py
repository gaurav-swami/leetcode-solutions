def sort(nums):
    n = len(nums)

    for i in range(n):
        maxx = i
        for j in range(i+1, n):
            if nums[j] >   nums[i]:
                maxx = j
        nums[i],nums[maxx] = nums[maxx], nums[i]
    return nums

print(sort([1,2,3,4,5 ]))
