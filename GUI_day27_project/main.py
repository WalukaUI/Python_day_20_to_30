from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,100)
window.config(padx=20, pady=20)

def calculate():
    val = int(inputbox.get())
    answer = round(val*1.609)
    txt3["text"]=answer


inputbox = Entry(background="pink")
inputbox.grid(column=2, row=0)

button1 = Button(text="Calculate", command=calculate)
button1.grid(column=2, row=2)


txt1 = Label(text="Miles")
txt1.grid(column=3, row=0)
txt2 = Label(text="is equal to")
txt2.grid(column=0, row=1)
txt3 = Label(text="0")
txt3.grid(column=2, row=1)
txt4 = Label(text="Km")
txt4.grid(column=3, row=1)
window.mainloop()