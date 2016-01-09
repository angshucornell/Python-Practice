class node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def appendFirst(self, node):
	self.cur_node = node

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
    def split(self):
	odd = self.cur_node
	if (odd != None):
		even = odd.next
	o = odd
	e = even
	while (o != None and e != None and o.next != None and e.next != None):

		print 'o.data = ', o.data
		o = o.next.next

		print 'e.data = ', e.data
		e = e.next.next

	if (o != None ):
		o.next = None
	if (e != None) :
		e.next = None


	return odd, even
		
		

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next


ll = linked_list()
ll.add_front(3)
ll.add_front(2)
ll.add_front(1)
ll.add_end(4)

ll.list_print()

print '==========='

o,e = ll.split()
l1 = linked_list()
l1.appendFirst(o)
l1.list_print()

print '==========='

l2 = linked_list()
l2.appendFirst(e)
l2.list_print()


