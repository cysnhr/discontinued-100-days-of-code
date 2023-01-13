#### 20230113

okay so my brain is dead.

here. we have a linked list.
okay, more accurately, a list.

[7,0,8]
also they’re strings

they should be turned into list nodes.
but!
I can’t run them in for loops for god knows why.
without the for loops, they should be:
    
```python
f_res = ListNode(res[0])
f_res.next = ListNode(res[1])
f_res.next.next = ListNode(res[2])
```

so if I do this after the second assignment
f_res.next = f_res
it’d just be ListNode(res[0])
and?
no but it’s supposed to be in order
like, list node (7, next: list node(0, next: list node(8, next: none)))
but I can’t do next next.

what if I do them opposite

```python
f_res = ListNode(res[2])
f_res.next = ListNode(res[1])
f_res.next.next = ListNode(res[0])

f_res = ListNode(res[2])
f_res.next = f_res
f_res = ListNode(res[1])


f_res = ListNode(res[2])
f_res.next = f_res
f_res = ListNode(res[1])
f_res.next = f_res
f_res = ListNode(res[0])
```
        
the value gets reassigned?
yeah I guess
but I thought …
okay let’s see

```python
f_res.next = ListNode(res[2])
f_res = ListNode(res[1])
```

it tells me that f_res has value None
was it because that the original value was redefined? and everything that was built upon it crumbled away?

```python
f_res = ListNode(res[len(res)-1])
    for r in range(1,len(res)-1):
    k = len(res) - r - 1 
    f_res.next = ListNode(res[k])
    new_var = f_res
    f_res = new_var
```
    
k = 1, 0
f_res.next = ListNode(res[1])
new_var = ListNode(res[0], next res[1])
f_res = new_var = ListNode(res[0], next res[1])

can you even write like this

```python
        for r in range(1,len(res)):
            print(f_res, f_res.next)
            f_res.next = ListNode(res[r])
            f_res = new_var
```

okay it doesn’t work
it has all of the attributes of a list node


#### 20230112 

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1 = ""
        n2 = ""
        list1 = []
        list2 = []
        list1.append(l1.val)
        while l1.next is not None:
          l1 = l1.next
          list1.append(l1.val)

        list2.append(l2.val)
        while l2.next is not None:
          l2 = l2.next
          list2.append(l2.val)

        for i in range(0,len(list1)):
            i = len(list1) - i - 1 
            n1 += str(list1[i])
        
        for j in range(0,len(list2)):
            j = len(list2) - j - 1 
            n2 += str(list2[j])
        
        n1 = int(n1)
        n2 = int(n2)
        tmp = str(n1 + n2)
        res = []
        for r in range(0,len(tmp)):
            r = len(tmp) - r - 1 
            res.append(tmp[r])
        
        f_res = ListNode(res[0])
        print(f_res)
        o = 1
        
        """
        stuff is wrong here
        """
        
        while o < len(res) - 1:
            f_res.next = res[o]
            f_res.next = res[o+1]
            o += 1

        print(f_res)
```
