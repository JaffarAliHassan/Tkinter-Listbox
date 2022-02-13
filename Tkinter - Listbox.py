from tkinter import *

root = Tk()
root.geometry('300x300')
root.title("Tkinter - Listbox")

List1 = Listbox(root)
List1.insert(1, "Python")
List1.insert(2, "C")
List1.insert(3, "PHP")

List1.pack()

mainloop()