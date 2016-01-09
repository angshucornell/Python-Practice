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
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def InOrder(self):
        if(self.root != None):
            self._printTreeIn(self.root)

    def _printTreeIn(self, node):
        if(node != None):
            self._printTreeIn(node.l)
            print str(node.v) + ' '
            self._printTreeIn(node.r)

    def PreOrder(self):
        if(self.root != None):
            self._printTreePre(self.root)

    def _printTreePre(self, node):
        if(node != None):
            print str(node.v) + ' '
            self._printTreePre(node.l)
            self._printTreePre(node.r)
    
    def PostOrder(self):
        if(self.root != None):
            self._printTreePost(self.root)

    def _printTreePost(self, node):
        if(node != None):
            self._printTreePost(node.l)
            self._printTreePost(node.r)
            print str(node.v) + ' '

    def getHeight(self):
	if (self.root == None):
		return 0

	else:
		return self._height(self.root)

    def _height(self, node):
	if (node == None):
		return 0
	else:
		lheight = self._height(node.l)
		rheight = self._height(node.r)
		if (lheight > rheight):
			return lheight + 1
		else:
			return rheight + 1

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
#tree.InOrder()
#print (tree.find(3)).v
#print tree.find(10)
#tree.deleteTree()
tree.InOrder()
print ' -- '
#tree.PreOrder()
print ' -- '
#tree.PostOrder()
print ' -- '
print tree.getHeight()

