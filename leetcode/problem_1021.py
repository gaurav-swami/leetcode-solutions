
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        res = "" 
        for ch in s: # if count 1 that means its the opening bracket will be the outer part is already processed so we can add to the string 
            if ch == "(":    # as we are in the inner part 
                count+=1
                if count > 1:
                    res += ch
            else: #  if count  == 1
                count-=1 # if count is 0 that means the closing bracket is of the outer part so we don't have to add it to the string
                if count>0:
                    res += ch

        return res

# time complexity = O(n)
#auxilary space = O(n)
# space complexity = O(1)

