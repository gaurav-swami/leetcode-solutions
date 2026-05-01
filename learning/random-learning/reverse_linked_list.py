# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        while head:
            stk.append(head.val)
            head = head.next
        head_node = ListNode()
        prev_node = head_node
        while stk:
            node = ListNode(stk.pop)
            prev_node.next = node
            prev_node = node
        
        return head_node.next
            

