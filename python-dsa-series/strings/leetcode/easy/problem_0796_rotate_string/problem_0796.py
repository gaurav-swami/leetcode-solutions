
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and goal in s*2

# comparison takes O(n) then membership takes O(n) and the arithmatic takes O(n)
# s*2 takes O(2n) auxilary space

#time complexity = O(n)
#space complexity = O(n)
