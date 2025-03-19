# recursive approach


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def create_linked_list(l1:Optional[ListNode], l2: Optional[ListNode], carry_val:int)-> Optional[ListNode]:
            if not l1 and not l2 and not carry_val :
                return None

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0     
            new_val = l1_val+l2_val+carry_val
            carry_val = new_val//10
            set_val = new_val%10
            curr_node = ListNode(set_val)
            
            curr_node.next = create_linked_list (
                l1.next if l1 else None,
                l2.next if l2 else None,
                carry_val
            )
            return curr_node          

        return create_linked_list(l1,l2,0)


#iterative Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry_val = 0
        curr_node = dummy

        while l1 or l2 or carry_val:    
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            new_val = l1_val + l2_val + carry_val
            carry_val = new_val // 10
            set_val = new_val % 10
            curr_node.next = ListNode(set_val)
            curr_node = curr_node.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None

        return dummy.next    


def addTwoNumbers(self,l1: Optional[ListNode], l2: Optional[ListNode])->Optional[ListNode]:
    