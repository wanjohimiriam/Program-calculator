from tkinter import *

def Exit():
    root.destroy()

def addnum():
    ans =int(e1.get()) +int(e2.get())
    additions.set(ans)

def subnum():
    ans = int(e1.get()) - int(e2.get())
    subtractions.set(ans)

def multnum():
    ans = int(e1.get()) * int(e2.get())
    multiplications.set(ans)

def divnum():
    ans = int(e1.get()) / int(e2.get())
    divisions.set(ans)

root = Tk()
additions = StringVar()
subtractions = StringVar()
multiplications = StringVar()
divisions = StringVar()

root.geometry("1700x1000")
root.title("Welcome to Calculator Basics")
root. configure(bg="brown")

f_num = Label(root, text="Number1", font="arial 20").place(x=50, y=20)
s_num = Label(root, text="Number2", font="arial 20").place(x=50, y=80)
add = Label(root, text="Addition", font="arial 20").place(x=50, y=140)
sub = Label(root, text="Subtration", font="arial 20").place(x=50, y=200)
mult = Label(root, text="Multiplication", font="arial 20").place(x=50, y=260)
div =Label(root, text="Division", font="arial 20").place(x=50, y=320)

e1 = Entry(root, font="arial 20")
e1.place(x=280, y=20)
e2 = Entry(root, font="arial 20")
e2.place(x=280, y=80)
add1= Entry(root, font="arial 20", textvariable=additions)
add1.place(x=280, y=140)
sub1 = Entry(root, font="arial 20", textvariable=subtractions)
sub1.place(x=280, y=200)
mult1 = Entry(root, font="arial 20", textvariable=multiplications)
mult1.place(x=280, y=260)
div1 = Entry(root, font="arial 20", textvariable=divisions)
div1.place(x=280, y=320)

exit = Button(root, text="Exit", font="arial, 20", fg="black", bg="red",command=Exit).place(x=1200, y=480)
addition = Button(root, text="Addition", font="arial, 20", fg="black", bg="red", command = addnum).place(x=20, y=480)
subtraction = Button(root, text="Subtraction", font="arial, 20", fg="black", bg="red", command= subnum).place(x=220, y=480)
multiplication = Button(root, text="Multiplication", font="arial, 20", fg="black", bg="red", command= multnum).place(x=440, y=480)
division = Button(root, text="Division", font="arial, 20", fg="black", bg="red", command= divnum).place(x=660, y=480)

root.mainloop()