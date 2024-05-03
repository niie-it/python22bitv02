from tkinter import *
from tkinter.messagebox import showinfo

# Khai báo màn hình cha
root = Tk()
root.title("Say hello")
root.geometry("300x150")

full_name = StringVar() # Biến kiểu string

# Khai báo và gắn widget lên màn hình cha
Label(root, text="SAY HELLO", font="Arial 18").grid(column=0, row=0)

Label(root, text="Input name").grid(column=0, row=1)
Entry(root, textvariable=full_name).grid(column=1, row=1)

Button(root, text="Click me",
    command=lambda : showinfo('Infor', 'Hello ' + full_name.get())
).grid(column=0, row=2)

# Hiện màn hình cha
root.mainloop()