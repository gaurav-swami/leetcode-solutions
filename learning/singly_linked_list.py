class SinglyNode:
	def __init__(self,val,next=None):
		self.val = val
		self.next = next

	def __str__(self):
		return str(self.val)


def display(head):
	temp = head
	elements =  []
	while temp:
		elements.append(str(temp.val))
		temp = temp.next

	list_string = ' -> '.join(elements) + ' -> None'
	print( list_string )

def search(head,val):
	temp = head
	while temp:
		if temp.val == val:
			return True
		temp = temp.next
	return False

head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

head.next = A
A.next = B
B.next = C

print(search(head,4))
