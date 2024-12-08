class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits)-1

        while last>=0:
            sum = digits[last]+1 
            if sum<10:
                digits[last] = sum
                return digits
                
            digits[last] = 0
            last -= 1

        return [1]+digits