def containsDuplicate( nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i!=j:
                    return True

        return False

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]

print(containsDuplicate(nums1))
print(containsDuplicate(nums2))