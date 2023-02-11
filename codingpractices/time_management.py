from tkinter import *
from tkinter import filedialog

# initialization
root = Tk()
root.title("Time Management")

# functions


# prints instructions
def help():
    # okay how do I print out the contents in README.md
    r = open("README.md", "r")
    r = r.read()
    help_win = Entry(root)
    help_win.pack()
    help_win.insert(END, r)

def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()

def close():
    root.quit()

# layout
help_button = Button(root, text="Help", padx=50, pady = 25, command=help)
exit_button = Button(root, text="Exit", padx=50, pady=25, command=close)

help_button.grid(row=0, column=0, sticky=E)
exit_button.grid(row=0, column=1, sticky=E)

# execution
root.mainloop()

