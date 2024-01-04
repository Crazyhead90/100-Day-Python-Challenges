from tkinter import *

window = Tk()
window.title("Km to Mile Converter")
window.config(padx=20, pady=20)


def calculate_conversion():
    km = float(entry.get())
    miles = round(km * 0.621371192)
    label_C.config(text=f"{miles}")


entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(column=2, row=1)

label_K = Label(text="Km")
label_K.grid(column=3, row=1)

label_E = Label(text="is equal to")
label_E.grid(column=1, row=2)

label_C = Label(text="0")
label_C.grid(column=2, row=2)

label_M = Label(text="Miles")
label_M.grid(column=3, row=2)

button = Button(text="Calculate", command=calculate_conversion)
button.grid(column=2, row=3)



window.mainloop()