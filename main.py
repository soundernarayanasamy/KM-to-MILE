from tkinter import *
import tkinter

def cal():
    got = ip.get()
    calculated = int(got) * 1.6
    txt4.config(text=calculated)

window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title("Mile to KM")

ip = Entry(width=7)
ip.grid(column=1, row=0)

txt1 = Label(text="Miles")
txt1.grid(column=2, row=0)

txt2 = tkinter.Label(text="is equal to")
txt2.grid(column=0, row=1)

txt3 = tkinter.Label(text="KM")
txt3.grid(column=2, row=1)

txt4 = tkinter.Label(text="0")
txt4.grid(column=1, row=1)

button = tkinter.Button(text="Calculate", command=cal)
button.grid(column=1, row=2)
window.mainloop()