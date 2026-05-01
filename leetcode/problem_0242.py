# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         t_dict = {}
#         s_dict = {}
#         for i in s:
#             if i in s_dict:
#                 s_dict[i]+=1
#             else:
#                 s_dict[i] = 1
#         for j in t:
#             if j in t_dict:
#                 t_dict[j]+=1
#             else:
#                 t_dict[j]=1
#         return (t_dict==s_dict)
#         

# above is my own code
'''
this is using hashmaps
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_char = {}
        for i in range(len(s)):
            count_char[s[i]] = count_char.get(s[i],0) + 1
            count_char[t[i]] = count_char.get(t[i],0) - 1

        return all(not count for count in count_char.values())

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        count_char = [0]*26
        for i in range(len(s)):
            count_char[ord(s[i]) - ord('a')] += 1
            count_char[ord(t[i]) - ord('a')] -= 1


        return all(not count for count in count_char)

