class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if (x<0):
                is_negative = True
                x*= -1
        catc = x
        rev = 0
        while catc>0:
            r = catc%10
            rev = (rev*10)+r
            catc = catc//10

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev * -1 if is_negative else rev
        