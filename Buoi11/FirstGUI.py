from tkinter import *

# Khai báo màn hình cha
root = Tk()
root.title("Tiêu đề")
root.geometry("300x150")

# Khai báo và gắn widget lên màn hình cha
Label(root, text="HELLO").pack()
Label(root, text="PYTHON 22BITV01", font="Arial 18").pack()

Entry(root).pack()
Button(root, text="Click me").pack()

# Hiện màn hình cha
root.mainloop()