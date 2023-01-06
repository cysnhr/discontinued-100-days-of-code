"""
features of linked list:
- append stuff to the end
- insert stuff
- deletion
- search for

20230106
"""

class Node():
  def __init__(self, val=None, next=None):
    # self.val is set to None because of self.head in the linked list later on
    self.val = val
    self.next = next
    # defines attributes of Node

class LinkedList:
	def __init__(self, head=None):
		self.head = None # initialization

	def __repr__(self):
		nodes = []
		node = self.head
		# will be in string form
    # self.head is None type, with the value None
		# the first value in the first node is head
		while node: # if the node isn't none
			nodes.append(str(node.val))
			print(f"you have appended this {node}, {node.val}, looking like this (still repr) {nodes}")
			node = node.next
		if nodes == []:
			return "No nodes present."
		else:
			return " -> ".join(nodes)
    
	def add(self, val):
		new_node = Node(val)
		print(f"da new node in add {new_node.val}")

		if self.head is None:
			print(f"self.head in add: {self.head}")
			self.head = new_node
			print(f"in add, new self.head node: {self.head.val}. the next time you do smth this is the self.head\n\n")
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
			print(f"last node: {last_node.val}")
		last_node.next = new_node

llist = LinkedList()
print(f"first try, the list: {llist} now imma start adding stuff\n\n")
llist.add("“A”")
print(f"The list after adding A: {llist}")
print(f"this is the current self.head, after adding 'A' {llist.head}")
print("a added\n\n")
llist.add("“B”")
print("b added")
print(llist)
