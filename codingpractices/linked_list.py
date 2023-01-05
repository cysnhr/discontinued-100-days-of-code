# 20230105

"""
features of linked list:

- append stuff to the end
- insert stuff
- deletion
- search for

"""

class Node():
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


class LinkedList():
  # note that everything should be in the form of nodes before passing into this function
  def __init__(self, head=None):
    self.head = None # initialization


  def __repr__(self):
    nodes = []
    # will be in string form
    node = self.head
    print(node.val)
    # the first value in the first node is head
    while node: # if the node isn't none
      nodes.append(node)
      print(node)
      node = node.next

    if nodes == []:
      print("No nodes present.")
    else:
      print(nodes)
      return " -> ".join(nodes)


  def add(self, val):
    new_node = Node(val)
    last = self.head
    if last is None: # proceeds if curr is None
      self.head = new_node # the node becomes the head
      new_node.next = None # ends the list
      return

    while last.next: # if curr is not the last
      last = last.next
    last.next = new_node

llist = LinkedList()
# REMEMBER THIS or else there's no list
a = Node("HI")
llist.add(a)
print(llist)
