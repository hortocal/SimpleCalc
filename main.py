import tkinter
from tkinter import *
global first
first = None
global second
second = None
global operator
operator = None
global result
result = None


def click_num(number):
    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(current) + str(number))


def click_operator(string):
    global first
    global operator
    try:
        if entry_box.get() != "":
            first = float(entry_box.get())
            entry_box.delete(0, END)
            if string == '/':
                operator = '/'
            elif string == '*':
                operator = '*'
            elif string == '-':
                operator = '-'
            elif string == '+':
                operator = '+'
            else:
                pass
        else:
            first = float(output.get())
            entry_box.delete(0, END)
            if string == '/':
                operator = '/'
            elif string == '*':
                operator = '*'
            elif string == '-':
                operator = '-'
            elif string == '+':
                operator = '+'
            else:
                pass
    except:
        clear_box()
        output.insert(INSERT, "Oops! Please try again.")

def clear_box():
    entry_box.delete(0, END)
    output.delete(0, END)
    global first
    first = None
    global second
    second = None


def to_percent():
    try:
        if entry_box.get() != "":
            percent_val = (float(entry_box.get()) / 100.0)
            entry_box.delete(0, END)
            entry_box.insert(INSERT, percent_val)
        elif output.get() != "":
            percent_val = (float(output.get()) / 100.0)
            output.delete(0, END)
            entry_box.insert(INSERT, percent_val)
        else:
            pass
    except:
        clear_box()
        output.insert(INSERT, "Oops! Please try again.")


def to_negative():
    try:
        if entry_box.get() != "":
            neg_val = (float(entry_box.get()) * -1)
            entry_box.delete(0, END)
            entry_box.insert(INSERT, neg_val)
        elif output.get() != "":
            neg_val = (float(output.get()) * -1)
            output.delete(0, END)
            entry_box.insert(INSERT, neg_val)
    except:
        clear_box()
        output.insert(INSERT, "Oops! Please try again.")


def evaluate():
    global first
    global second
    global operator
    global result
    output.delete(0, END)
    if first is None:
        output.insert(INSERT, float(entry_box.get()))
    else:
        second = entry_box.get()
        entry_box.delete(0, END)
        try:
            if operator == '/':
                result = float(first) / float(second)
            elif operator == '*':
                result = float(first) * float(second)
            elif operator == '-':
                result = float(first) - float(second)
            elif operator == '+':
                result = float(first) + float(second)
            else:
                pass
            output.insert(INSERT, str(result))
        except:
            output.insert(INSERT, "Invalid operation. Try again.")


if __name__ == '__main__':
    window = Tk()
    user_result = StringVar()
    window.title("Simple Calculator")
    window.configure(background="grey")
    entry_box = Entry(window, width=18)
    entry_box.grid(row=0, columnspan=4, sticky=NW)
    output = Entry(window, width=18, textvariable=user_result)
    output.grid(row=1, columnspan=4, sticky=NW)
    button_clear = Button(window, text="AC", width=1, command=lambda: clear_box()).grid(row=2, column=0, sticky=NW)
    button_negative = Button(window, text="+/-", width=1, command=lambda: to_negative()).grid(row=2, column=1, sticky=NW)
    button_percent = Button(window, text="%", width=1, command=lambda: to_percent()).grid(row=2, column=2, sticky=NW)
    button_div = Button(window, text="/", width=1, command=lambda: click_operator('/')).grid(row=2, column=3, sticky=NW)
    button7 = Button(window, text="7", width=1, command=lambda: click_num(7)).grid(row=3, column=0, sticky=NW)
    button8 = Button(window, text="8", width=1, command=lambda: click_num(8)).grid(row=3, column=1, sticky=NW)
    button9 = Button(window, text="9", width=1, command=lambda: click_num(9)).grid(row=3, column=2, sticky=NW)
    button_mult = Button(window, text="*", width=1, command=lambda: click_operator('*')).grid(row=3, column=3, sticky=NW)
    button4 = Button(window, text="4", width=1, command=lambda: click_num(4)).grid(row=4, column=0, sticky=NW)
    button5 = Button(window, text="5", width=1, command=lambda: click_num(5)).grid(row=4, column=1, sticky=NW)
    button6 = Button(window, text="6", width=1, command=lambda: click_num(6)).grid(row=4, column=2, sticky=NW)
    button_subt = Button(window, text="-", width=1, command=lambda: click_operator('-')).grid(row=4, column=3, sticky=NW)
    button1 = Button(window, text="1", width=1, command=lambda: click_num(1)).grid(row=5, column=0, sticky=NW)
    button2 = Button(window, text="2", width=1, command=lambda: click_num(2)).grid(row=5, column=1, sticky=NW)
    button3 = Button(window, text="3", width=1, command=lambda: click_num(3)).grid(row=5, column=2, sticky=NW)
    button_add = Button(window, text="+", width=1, command=lambda: click_operator('+')).grid(row=5, column=3, sticky=NW)
    button0 = Button(window, text="0", width=6, command=lambda: click_num(0)).grid(row=6, columnspan=2, sticky=NW)
    button_period = Button(window, text=".", width=1, command=lambda: click_num('.')).grid(row=6, column=2, sticky=NW)
    button_result = Button(window, text="=", width=1, command=lambda: evaluate()).grid(row=6, column=3, sticky=NW)
    window.mainloop()