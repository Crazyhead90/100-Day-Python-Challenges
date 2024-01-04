from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    text = entry.get()
    my_label.config(text=text)

# Label


my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text!")
my_label.grid(column=0, row=0)

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click Me 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry

entry = Entry(width=10)
entry.grid(column=3, row=3 )

# Text





window.mainloop()