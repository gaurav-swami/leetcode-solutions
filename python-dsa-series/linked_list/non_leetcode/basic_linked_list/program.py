class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Singly:
    def __init__(self):
        self.head = None

    def append(self,val):
        n = Node(val)
        
        if not self.head: 
            self.head = n 
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = n
    def traverse(self):
        if not self.head:
            print("Linked List Empty")
        else:
            curr = self.head
            while curr:
                print(curr.val, end = "->")
                curr = curr.next
            print('None')

    def insert_pos(self,val,pos):
        n = Node(val) 
        count = 0
        curr = self.head
        if count == 0:
            n.next = self.heazz
        while count < pos:
            curr = curr.next
        
        



s = Singly()

s.append(1)
s.append(2)
s.append(3)
s.traverse()
