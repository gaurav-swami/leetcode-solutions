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
            new_node = Node(val)

            if pos == 0:
                new_node.next = self.head
                self.head = new_node

            elif pos>0:
                curr = self.head
                prev = None
                count = 0
                while count < pos and curr:
                    prev = curr
                    curr = curr.next
                    count += 1
                
                prev.next = new_node
                new_node.next = curr
            
            else:
                print('Invalid Position')

    def delete(self,val):
        if not self.head:
            print("Out of bounds")
            return 
        
        : 
        




s = Singly()


s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.append(5)
s.append(6)
s.traverse()

s.insert_pos(69,3)

s.traverse()
s.delete(6)
s.traverse()
