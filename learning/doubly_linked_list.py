class DoublyNode:
	def __init__(self, val, next = None, prev = None):
		self.val = val
		self.next = next
		self.prev = prev

	def __str__(self):
		return str(self.val)


head = tail = DoublyNode(1)

def display(head):
	curr = head
	elements = []
	while curr:
		elements.append(curr.val)
		curr = curr.next
	list_string = ' -> '.join(elements) + ' None'