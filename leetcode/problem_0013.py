
class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {
            "I": 1, 
            "V": 5, 
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        count = 0
        prev = -1
        for i in range(len(s)-1,-1,-1):
            val = mapp[s[i]]
            if val < prev: count -= val
            else: count+=val

            prev = val

        return count 

#time complexity = O(n)
#space complexity = O(1)
