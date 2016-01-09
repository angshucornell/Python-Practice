class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_front(self, data):
        new_node = node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def add_end(self, data):
        new_node = node()
	new_node.data = data

	if self.cur_node == None:
		self.cur_node = new_node
	else:		
		n = self.cur_node
		while n.next != None:
			n = n.next
                n.next = new_node

    def reverse(self):
	head = self.cur_node
	self._reverse(head)

    def _reverse(self, node):
		if node == None:
			return node
		elif node.next == None:
			return node
		else:
			rest = node.next
			if rest == None:
				return None
			else:
				self._reverse(rest)
			node.next.next = node
			node.next = None
			return rest

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next


ll = linked_list()
ll.add_front(1)
ll.add_front(2)
ll.add_front(3)
ll.add_end(4)

ll.list_print()
ll.reverse()
print 'aaaaa'

ll.list_print()
