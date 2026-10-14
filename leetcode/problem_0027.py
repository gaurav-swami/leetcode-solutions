
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k] = nums[i]
                k+=1
        
        return k

#explanation : Just use one pointer to assign the different items than value to array using k pointer while skipping
#the items which are equal to value

#time complexity = O(n)
#space complexity = O(1)
