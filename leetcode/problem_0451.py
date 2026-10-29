class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        record = {}
        for i in s:
            freq[i] = freq.get(i,0) + 1
        
        sorted_char = sorted(freq.items(), key = lambda x: x[1], reverse = True)

        strr = ""
        for i,j in sorted_char:
            strr += i*j
        return strr

#time complexity = O(nlogn) + O(n) = O(nlogn)
#space complexity = O(1) or O(52)

