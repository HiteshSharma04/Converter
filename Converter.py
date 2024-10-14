from tkinter import *

window = Tk()
window.title("Mile KM Converter")
window.minsize(300,300)
window.config(padx=100,pady=100)

label1 = Label(text="Miles", font=("Arial",25,"bold"))
label2 = Label(text="Equals To", font=("Arial",25,"bold"))
label3 = Label(text="", font=("Arial",25,"italic"))
label4 = Label(text="KiloMeters", font=("Arial",25,"bold"))
label1.grid(row=0,column=2)
label2.grid(row=1,column=0)
label3.grid(row=1,column=1)
label4.grid(row=1,column=2)

def cal():
    label = float(input.get())
    km = round(label * 1.609)
    label3.config(text= f"{km}")
button = Button(text="Calculate", command=cal)
button.grid(row=2,column=1)

input = Entry()
input.grid(row=0,column=1)

window.mainloop()