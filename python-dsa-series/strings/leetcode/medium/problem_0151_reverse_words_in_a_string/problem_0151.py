
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = []
        for ch in s:
            if ch != " ":
                word.append(ch)
            elif word:
                    words.append(word)
                    word = [] 
        if word: words.append(word)
        res = [] 
        for i in range(len(words) - 1, -1, -1):
            if res:
                res.append(" ") # adding space if there is a word in res already 
            res.extend(words[i]) #extending in result because our words are elements in a list 

        return "".join(res)
# time complexity = O(n)
# space complexity = O(n) 


