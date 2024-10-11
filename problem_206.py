# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# this is the solution using the iteration method (using stack)
class Solution(object):
    def reverseList(self, head):
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        i=len(stack)-1
        while curr:
           curr.val = stack[i]
           i -= 1
           curr = curr.next

        return head 