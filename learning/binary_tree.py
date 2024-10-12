values = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]

class Node:
	def __init__(self,val,left = None,right = None):
		self.val = val
		self.left = left
		self.right = right

i=-1

def binary_tree(values: list)->Node:
	global i
	i+=1
	if values[i]==-1:
		return 
	node = Node(values[i])
	node.left = binary_tree(values)
	node.right = binary_tree(values)
	return node
	

def display_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(   str(root.val),end = " ")
        if root.left: display_tree(root.left, level + 1) 
        if root.right: display_tree(root.right, level + 1)

display_tree(binary_tree(values))