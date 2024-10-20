from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    perm = []
    def permuting(num: List[int], curr:List[int]):
        if len(num)==0:
            perm.append(curr)
            return

        for i in range (len(num)):
            
            remaining =  num[:i]+ num[i+1:]
            permuting(remaining, curr+[nums[i]] )

    permuting(nums,[])
    return perm

print(permute([1,2,3]))