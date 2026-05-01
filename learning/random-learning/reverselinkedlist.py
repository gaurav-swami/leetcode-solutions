# print linked list in reverse

class Node:
	def __init__ (self,val,next=None):
		self.val = val
		self.next = next
	def __str__ (self):
		return str(self.val)

def display(head):
	list1=[]
	curr = head
	while curr:
		list1.append(str(curr.val))
		curr = curr.next

	print(" -> ".join(list1), "-> None")

def reverse(head):
	if not head:
		return 
	reverse(head.next)
	print(head)

a = Node(10)
b = Node(20,a)
c = Node(30,b)
d = Node(40,c)

head = d

display(d)

reverse(head)