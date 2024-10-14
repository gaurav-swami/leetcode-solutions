from collections import deque

values = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
i=-1
count = 0

class Node:
	def __init__(self,val,left = None,right = None):
		self.val = val
		self.left = left
		self.right = right

def binary_tree(values: list)->Node:
	global i
	i+=1
	if values[i]==-1 or i>=len(values): 
		return None
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

def level_order(node):
    if not node: 
        return    
    q = deque([node])
    q.append(None)
    while q:
        node = q.popleft()
        if node is None:
        	print()
        	if q:
        		q.append(node)
        	continue

        print(node.val, end=" ")
        if node.left: 
            q.append(node.left)
        if node.right:
        	q.append(node.right)

def count_nodes(node):
	global count
	if not node:
		return
	count+=1
	count_nodes(node.left)
	count_nodes(node.right)


count_nodes(binary_tree(values))
print(count_nodes)


