from typing import Optional

class Node:
	def __init__(self,val,left = None,right = None):
		self.val = val
		self.left = left
		self.right = right


i=0

def inorder(root: Optional[Node]):
	if not root:
		return
	inorder(root.left)
	print(root.val, end = ' ')
	inorder(root.right)



def insert(root: Optional[Node],val)->Node:
	if not root:
		root = Node(val)
		return root	
	if (root.val>val):
		root.left = insert(root.left,val)
	else:
		root.right = insert(root.right,val)
	return root

root = None
values = [5,1,3,4,2,7]
for i in values:
	root = insert(root,i)

inorder(root)

def search (root: Optional[Node],val: int)->bool:
	if not root: 
		return False

	if root.val> val: 
		return search(root.left,val)
	elif root.val==val:
		return True
	else:
		return search(root.right,val)

print()
print(search(root,8))