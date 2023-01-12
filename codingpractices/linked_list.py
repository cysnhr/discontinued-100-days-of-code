# 20230110

class Node():
    def __init__(self, val, next=None):
      self.val = val
      self.next = next

class ListNode(object):
    def __init__(self, head=None):
      self.head = None

    def __repr__(self):
      ls = []
      node = self.head
      if node is None:
        return "No nodes present."
      while node is not None:
        ls.append(str(node.val))
        print(f"{node} is appended. Pending: {node.next}")
        node = node.next
        continue
        print(ls)
      return "->".join(ls)

    # append to the end
    def add(self, val):
      new_node = Node(val)
      print(f"This is the node you entered: {new_node}: {new_node.val}")
      node = self.head
      print(f"This is self.head: {self.head}, and the node appointed to it: {node}")
      if node is None: # if self.head is None
        self.head = new_node
        new_node.next = None
        print(f"The new self.head is {self.head}!")
        print(f"New node {new_node} added.")
      else:
        while node.next: # while it's not end
          node = node.next
        node.next = new_node
        print(f"Without None self.head, new node {node.next} added, {node.next.val}.")

    # reverse
    def backwards(self):
      node = self.head
      node.prev = None
      backlist = []
      if node is None:
        return "No nodes present."
      while node.next is not None:
        node.next.prev = node # is this how prev was defined?
        node = node.next
      backlist.append(str(node.val))
      while node.prev is not None:
        node = node.prev
        backlist.append(str(node.val))
      return "->".join(backlist)
        
    # clear up everything
    def clear(self):
      node = self.head
      while node.next is not None:
        node = node.next
        node.prev = None
      self.head = None
    
 
llist = ListNode()
llist.add("A")
llist.add("B")
print(llist)
print(llist.backwards())
