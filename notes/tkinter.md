I'm putting all the optional attributes of these functions because I don't think I'll be able to remember them so quickly.

### Setup

```python
from tkinter import *

root = Tk()

# stuff
# remember to pack

root.mainloop()
```

### Label

```python
a_label = Label(root, text="", fg=color, bg=color)
# the color thing works with everything with text
a_label.pack()
```

### Grid

```python
# do this before packing
a_label.grid(row=0, column=0)
```

### Button

```python
a_button = Button(root, text="", state=DISABLED, padx=10, pady=15, command=function)
a_button.pack()

# quit: root.destroy
```

### Input

```python
e = Entry(root, text="", width=10, borderwidth=5)
e.grid(row=0, column=0, columnspan=10, padx=5, pady=5)
e.pack()
e.get()
# now you can use the input
```






