
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = []
        k = len(strs[0])
        j = 0
        while j<k:
             
            curr = strs[0][j] # then current char that we will compare  
            for i in strs:
                if j>=len(i) or i[j]!=curr: #if the current index is already greated then length of the current i
                    return "".join(prefix) # then return prefix or also when curr doens't match to current words char
            
            prefix.append(curr)
            j += 1

        return "".join(prefix)
# time complexity = O(m*n)
# space complexity = O(1) but if the the whole word is prefix then, O(m) where m is the length of the longest word
