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
                res.append(" ")
            res.extend(words[i])

        return "".join(res)
