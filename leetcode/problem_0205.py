
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        c = 0

        for c in range(len(s)):
            if s[c] in mapping:
                if mapping[s[c]] != t[c]:
                    return False
            
            else:
                if t[c] in used:
                    return False
            
                used.add(t[c])
                mapping[s[c]] = t[c]
            
        return True
                 

# time complexity O(n) 
#space complxity O(2n) because of dictionary and map
            
