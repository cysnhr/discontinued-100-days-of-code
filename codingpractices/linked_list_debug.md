20230107
### comparison

full code [here](./codingpractices/linked_list)
[debug 1](./codingpractices/linked_list_debug_1)
[debug 2](./codingpractices/linked_list_debug_2)

The `__repr__` function is where the problem occurred, but I couldn't figure out why.

How does this affect the add function, along with being able to alter the value of `self.head`?

#### ver.1
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

#### ver.2
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
