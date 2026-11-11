# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next: return None
        curr = new = head
        
        for _ in range(n):
            curr = curr.next

        if not curr:
            return head.next


        new = head

        while curr.next:
            new = new.next
            curr = curr.next

        new.next = new.next.next

        return head


#time complexity = O(n)        
#space complexit = O(1)
