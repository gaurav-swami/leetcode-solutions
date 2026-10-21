class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = list(s)
        vowels = set("aeiouAEIOU")
        l,r = 0, len(ls)-1

        while l<r:
            while l<r and ls[l].lower() not in vowels:
                l+=1

            while l<r and ls[r].lower() not in vowels:
                r-=1

            ls[l],ls[r] = ls[r], ls[l]

            l+=1
            r-=1

        return "".join(ls)        
        
#time complexity = O(n)
#space complexity = O(n)
