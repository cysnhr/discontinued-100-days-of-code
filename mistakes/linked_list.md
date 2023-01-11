full code [here](./codingpractices/linked_list.py) <br>
[debug 1](./codingpractices/linked_list_debug_1.py) <br>
[debug 2](./codingpractices/linked_list_debug_2.py) <br>

### 20230105

```python
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
      return " -> ".join(nodes)

  def add(self, val):
    new_node = Node(val)
    last = self.head
    if last is None: # proceeds if last is None
      self.head = new_node # the node becomes the head
      new_node.next = None # ends the list
      return

    while last.next: # if last is not the last
      last = last.next
    last.next = new_node

llist = LinkedList()
# REMEMBER THIS or else there's no list
a = Node("HI")
llist.add(a)
print(llist)
```
1. Should be `nodes.append(str(node.val))`, because lists don't really get to append objects.

### 2023 01 07

The `__repr__` function is where the problem occurred, but I couldn't figure out why.

How does this affect the add function, along with being able to alter the value of `self.head`?

##### ver.1
```python
def __repr__(self):
	nodes = []
	while self.head: # if the node isn't none
		node = self.head
		nodes.append(str(node.val))
		self.head = node.next
	if nodes == []:
		return "No nodes present."
	else:
		return " -> ".join(nodes)
```
`self.head` is None even after appending "A" to the list. 
$\rightarrow$ **`node` is `self.head`, and if it is a `NoneObject` it'd have no `val` attribute. Basically wrong in variable assignment.**

##### ver.2
```python
def __repr__(self):
	nodes = []
  node = self.head
	while node: # if the node isn't none
		nodes.append(str(node.val))
		self.head = node.next
	if nodes == []:
		return "No nodes present."
	else:
		return " -> ".join(nodes)
```
The value to append gets added over and over again with the while loop. Meaning the node isn't None at the first place, hence self.head wasn't None
$\rightarrow$ **Not altering the value of node, so it was always unchanged, and it happens to be of a value in the first place, because you added something.**

#### ver.3
```python
	def __repr__(self):
		nodes = []
		node = self.head
			nodes.append(str(node))
			node = node.next
		if nodes == []:
			return "No nodes present."
		else:
			return " -> ".join(nodes)
```
`self.head` has the value "A", while node is None. HOW JUST HOW IS THIS POSSIBLE


Upon testing some of these codes, Node(A) does become the new self.head after the add function. So what went wrong?

I actually have no idea and for days I've been working on this but argh. Sometimes self.head is None but sometimes it isn't. I don't know what to do.
$\rightarrow$ **You didn't change the self.head in this code.**
