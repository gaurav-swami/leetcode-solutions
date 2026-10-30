class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        count = 0
        for i in s:
            if i=='(': 
                count += 1
                maxi= max(maxi,count)
            elif i==')':
                count -= 1
        
        return maxi 

#time complexity = O(n)
#space complexity = O(1)
