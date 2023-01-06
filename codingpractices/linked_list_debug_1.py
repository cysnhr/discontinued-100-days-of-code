"""
features of linked list:

- append stuff to the end
- insert stuff
- deletion
- search for

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
		# will be in string form
    # self.head is None type, with the value None
		# the first value in the first node is head
		while self.head: # if the node isn't none
			node = self.head
			print(f"What is self.head? {self.head.__class__}, and the value? {node.val}. the node? {node}\n\n")
			nodes.append(str(node.val))
			print(f"you have appended this {node}, {node.val}, looking like tihs {nodes}")
			self.head = node.next
		if nodes == []:
			return "No nodes present."
		else:
			return " -> ".join(nodes)
    
	def add(self, val):
		new_node = Node(val)
		print(f"da new node {new_node.val}")

		if self.head is None:
			print(f"self.head: {self.head}")
			self.head = new_node
			print(f"new self.head node: {self.head.val}. the next time you do smth this is the self.head\n\n")
      
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
print(LinkedList.head)
print("a added\n\n")
llist.add("“B”")
print("b added")
print(llist.__repr__())


"""
I’m going to try writing this as if I were reporting something. 
first we create a linked list object in llist = LinkedList().
next, for __repr__, we jump into that function, and since self.head is None (see __init__ of LinkedList), the whole while loop doesn’t get executed. Nothing is in nodes list, and it returns “No nodes present.”
The next order, we add “A”. Head to the add function. “A” is passed into Node(), which is then assigned to new_node.
self.head is still None, which gets everything in the if condition moving. Node(“A”), new_node, becomes the new self.head, which grants self.head the value “A” and the attributes of a node. The function returns, and the next order is for printing out the linked list again. We go to the __repr__ function. 
Self.head is not None this time, so the while loop gets executed. It’s actually a Node object, with the value “A”, basically just the thing we had added to the list earlier.
The thing gets appended to nodes list as a string, as specified.
But self.head later becomes node.next, which is None, set as default in the initialization. There’s only one thing in the list, so printing it you don’t get an arrow. At least that’s how I imagine the join function to work.
Alright, we have added “A” successfully, and getting that return value by printing it, then moving on to the next command “an added,” we know for sure.
Next on, add “B”. Let’s go to the add function yet again. new_node has a value “B”.

WAIT. The problem is. Why does the value of self.head not get saved? is it not global? It tells me that LinkedList has no attribute “head.”

"""
