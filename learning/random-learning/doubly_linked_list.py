class DoublyNode:
	def __init__(self, val, next = None, prev = None):
		self.val = val
		self.next = next
		self.prev = prev

	def __str__(self):
		return str(self.val)


head = tail = DoublyNode(1)

def insert_at_beginning(head,tail,val):
	new_node = DoublyNode(val,next=head)
	head.prev = new_node
	return new_node,tail

def insert_at_end(head,tail,val):
	new_node = DoublyNode(val,prev=tail)
	tail.next = new_node
	return head,new_node

def display(head):
	curr = head
	elements = []
	while curr:
		elements.append(str(curr.val))
		curr = curr.next
	print('None <-> ' + ' <-> '.join(elements) + ' <-> None')

display(head)

head, tail = insert_at_beginning(head,tail,3)
display(head)
head, tail = insert_at_beginning(head,tail,5)
display(head)
head, tail = insert_at_end(head,tail,3)
display(head)
head, tail = insert_at_end(head,tail,5)
display(head)
