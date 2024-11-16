from typing import Optional

class Node:
	def __init__ (self,val,left = None, right = None):
		self.val = val
		self.left = left
		self.right = right 


def inorder(root: Optional[Node]):
	if not root:
		return

	inorder(root.left)
	print(root.val, end = " ")
	inorder(root.right)

def insert_node (root:Optional[Node], val: int) -> Node:
	if not root:
		root = Node(val)
		return root
	if val < root.val:
	 	root.left =  insert_node(root.left, val)
	else:
	 	root.right = insert_node(root.right,val)

	return root


list1 = [50,40,60,30,70,20,80,10,90]
root = None
for i in list1:
	root = insert_node(root,i)


inorder(root)
