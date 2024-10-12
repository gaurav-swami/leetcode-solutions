from collections import deque

values = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
i=-1

class Node:
	def __init__(self,val,left = None,right = None):
		self.val = val
		self.left = left
		self.right = right

def binary_tree(values: list)->Node:
	global i
	i+=1
	if values[i]==-1: 
		return 
	node = Node(values[i])
	node.left = binary_tree(values)
	node.right = binary_tree(values)
	return node
	
def preorder(node):
	if not node: return 
	print (node.val, end=" ")
	preorder(node.left)
	preorder(node.right)

def inorder(node):
	if not node: return
	inorder(node.left)
	print(node.val, end = " ")
	inorder(node.right)

def postorder(node):
	if not node: 
		return
	postorder(node.left)
	postorder(node.right)
	print(node.val, end = " ")

def  breadth_first_search(node):
	if not node: 
		return	
	q = deque([node])
	while q:
		node = q.popleft()
		print(node.val, end = " ")
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)
		
	

breadth_first_search(binary_tree(values))



