from collections import deque

values = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
# values = [1, 2, 4, 7, -1, -1, -1, 5b, -1, 8, -1, -1, 3, -1, -1]

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
	if not node:
		return 0
	return count_nodes(node.left) + count_nodes(node.right) + 1

def sum_nodes(node):
	if not node:
		return 0
	return sum_nodes(node.left) + sum_nodes(node.right)  + node.val


def height(node):
	if not node:
		return 0
	left_height = height(node.left)
	right_height = height(node.right)
	return max(left_height,right_height)+1

def max_diameter(node):
	if not node:
		return 0
	left_diameter = max_diameter(node.left)
	right_diameter = max_diameter(node.right)
	own_diameter = height(node.left) + height(node.right)+ 1
	return max(left_diameter,right_diameter,own_diameter)

class TreeInfo:
	ht = 0
	diam = 0

	def __init__(self,ht,diam):
		self.ht = ht
		self.diam = diam


#max diameter

def diameter(node):
	if not node:
		return 0,0

	left_height,left_diameter = diameter(node.left)
	right_height, right_diameter = diameter(node.right)
	own_diameter = left_height + right_height + 1

	return max(left_height,right_height)+1,  max(left_diameter, right_diameter,own_diameter)


print(diameter(binary_tree(values)))


