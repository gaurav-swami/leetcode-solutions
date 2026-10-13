class Solution:
    def firstUniqChar(self, s: str) -> int:
        records = {}
        for i in s:
            if i in records:
                records[i]+=1
            else:
                records[i]=1

        for i in s:
            if records[i] == 1:            
                return s.find(i)
        
        return -1

#time complexity = O(n)
#space complexity = O(1)
