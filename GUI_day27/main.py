import tkinter

window = tkinter.Tk()
window.title("Program GUI")
window.minsize(800, 700)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
my_label["text"] = "new text"

#Button

def button_clicked():
    val = input.get()
    my_label["text"] = val
    print("clicked")


button = tkinter.Button(text="clickme", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="button2", command=button_clicked)
button2.grid(column=3, row=0)

#Entry/Input

input = tkinter.Entry(background="red", cursor="hand2")
input.place(x=200, y=200)



window.mainloop()





