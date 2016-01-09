class Node:
	def __init__(self, val):
		self.l = None
		self.r = None
		self.v = val

class Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root
		
	def add(self, val):
		if (self.root == None):
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val < node.v:
			if node.l == None:
				node.l = Node(val)
			else:
				self._add(val, node.l)
		else
			if node.r == None
				node.r = Node(val)
			else:
				self._add(val, node.r)

	
	def find(self, val):
		if self.root != None:
			return self._find(val, self.node)
		else:
			return None
			

	def _find(self, val, node):
		if (node.v == val):
			return node
		elif (val < node.v and node.l != None):
			self._find(val, node.l)
		elif (val > node.v and node.r != None):
			self._find(val, node.r)


		

	
		
