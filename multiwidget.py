from tkinter import *

window = Tk()
window.title("Converter")
#window.geometry("430x100")


def converter():
    t1.delete(1.0,END)
    t2.delete(1.0,END)
    t3.delete(1.0,END)
    try:
        grams = float(e1_value.get())*1000
        pounds = round((float(e1_value.get())*2.20462),4)
        ounces = round((float(e1_value.get())*35.274),4)
        t1.insert(END, grams)
        t2.insert(END, pounds)
        t3.insert(END, ounces)
    except ValueError:
        t1.insert(END, "numbers only")
        e1.delete(0,END)
        pass


l0 = Label(window, text="Kg:")
l0.grid(row=0,column=0,sticky="e")

l1 = Label(window, text="grams:")
l1.grid(row=1,column=0,sticky="w")

l2 = Label(window, text="pounds:")
l2.grid(row=1,column=1,sticky="w")

l3 = Label(window, text="ounces:")
l3.grid(row=1,column=2,sticky="w")

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height = 1,width = 20)
t1.grid(row=2,column=0)

t2 = Text(window,height=1,width=20)
t2.grid(row=2,column=1)

t3 = Text(window,height=1,width=20)
t3.grid(row=2,column=2)

b1 = Button(window,text="Convert", command=converter)
b1.grid(row=0,column=2)

window.mainloop()
