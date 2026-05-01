class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapping = {')':'(',']':'[','}':'{'}

        for c in s:
            if c in mapping:
                if stk and stk[-1]==mapping[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        return not stk

        