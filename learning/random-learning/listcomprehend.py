# from typing import List

# def groupAnagrams( strs: List[str]) -> List[List[str]]:
        
#         list2 = []
#         list3 = []
#         dick = {}
#         idx = 0
#         for i in strs:
#             list2.append("".join(sorted(i)))
#         for n,i in enumerate(list2):
#             if i not in dick:
#                 dick[i] = idx
#                 list3.append([strs[n]])
#                 idx+=1
#             else:
#                 list3[dick[i]].append(strs[n])

        


# strs = ["eat","tea","tan","ate","nat","bat"]
# groupAnagrams(strs)



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(i)

        return list(res.values()) 
            

