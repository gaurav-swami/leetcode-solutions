class HashTable:
	def __init__(self):
		self.MAX = 100
		self.arr = [[] for i in range(self.MAX)]


	def get_hash(self,key):
		h = 0
		for char in key:
			h+=ord(char)
		return h % self.MAX

	def __setitem__(self,key,val):
		h = self.get_hash(key)
		self.arr[h].append((key,val))
		for idx, element in enumerate(self.arr[h]):
			if len(element) == 2 and element[0] == key:
				self.arr[h][idx]=(key,val)
				found = True
				break
		if not found:
			self.arr[h].append((key,val))
				element[1] = value

	def __getitem__(self,key):
		h = self.get_hash(key)
		return self.arr[h]

	def __delitem__(self,key):
		h = self.get_hash(key)
		self.arr[h] = None

t = HashTable()
t['march 6'] = 120
t['march 7'] = 110
t['march 8'] = 100
print(t.arr)
del t['march 6']
print(t.arr)

