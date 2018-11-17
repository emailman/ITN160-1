from tkinter import *
window = Tk()
window.title("Welcome to ITN160 - Programming I")
window.geometry('400x150')

lbl = Label(window, text="Hello",font=('times',50), bg = 'black', fg='orange')
lbl.grid(column=0, row=0)
lbl.pack(expand=YES, fill=BOTH)
window.mainloop()