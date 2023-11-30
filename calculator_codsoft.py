from tkinter import *

def button_press(num):
    global expression_test
    expression_test = expression_test + str(num)
    expression_label.set(expression_test)

def equals():
    global expression_test
    try:
        total = str(eval(expression_test))
        expression_label.set(total)
        expression_test = total
    except Exception as e:
        expression_label.set("Error")
        expression_test = ""

def clear():
    global expression_test
    expression_label.set("")
    expression_test = ""

window = Tk()
window.title("calculator")
window.geometry("500x500")

expression_test = ""
expression_label = StringVar()

label = Label(window, textvariable=expression_label, font=("consolas", 20), width=24, height=2, bg="pink")
label.pack()

frame = Frame(window)
frame.pack()

button = Button(frame, text='1', width=9, height=4, font=35, command=lambda: button_press(1))
button.grid(row=0, column=0)
button = Button(frame, text='2', width=9, height=4, font=35, command=lambda: button_press(2))
button.grid(row=0, column=1)
button = Button(frame, text='3', width=9, height=4, font=35, command=lambda: button_press(3))
button.grid(row=0, column=2)
button = Button(frame, text='4', width=9, height=4, font=35, command=lambda: button_press(4))
button.grid(row=1, column=0)
button = Button(frame, text='5', width=9, height=4, font=35, command=lambda: button_press(5))
button.grid(row=1, column=1)
button = Button(frame, text='6', width=9, height=4, font=35, command=lambda: button_press(6))
button.grid(row=1, column=2)
button = Button(frame, text='7', width=9, height=4, font=35, command=lambda: button_press(7))
button.grid(row=2, column=0)
button = Button(frame, text='8', width=9, height=4, font=35, command=lambda: button_press(8))
button.grid(row=2, column=1)
button = Button(frame, text='9', width=9, height=4, font=35, command=lambda: button_press(9))
button.grid(row=2, column=2)
button = Button(frame, text='0', width=9, height=4, font=35, command=lambda: button_press(0))
button.grid(row=3, column=0)
plus = Button(frame, text='+', width=9, height=4, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)
minus = Button(frame, text='-', width=9, height=4, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)
multiply = Button(frame, text='*', width=9, height=4, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)
divide = Button(frame, text='/', width=9, height=4, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)
equal = Button(frame, text='=', width=9, height=4, font=35, command=equals)
equal.grid(row=3, column=1)
decimal = Button(frame, text='.', width=9, height=4, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=2)
clear_1 = Button(window, text='clear', width=9, height=4, font=35, command=clear)
clear_1.pack()

window.mainloop()

