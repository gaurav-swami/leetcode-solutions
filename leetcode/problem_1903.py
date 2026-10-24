class Solution:
    def largestOddNumber(self, num: str) -> str:
        r = len(num)-1
        for i in range(r,-1,-1):
            if num[i] in "13579":
                return num[0:i+1]
            
        return ""
       
