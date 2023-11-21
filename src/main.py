import tkinter as tk
import re
from reuse_math.Operation import Operation

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)


def evaluate(lhs, op, rhs, base):
    if op == '+':
        temp = Operation([lhs, rhs]).add()
    if op == '-':
        temp = Operation([lhs, rhs]).subtract()
    if op == '*':
        temp = Operation([lhs, rhs]).multiply()
    if op == '/':
        temp = Operation([lhs, rhs]).divide()

    if base == 10:
        ans = temp.as_int()
    elif base == 2:
        ans = temp.as_bin()
    elif base == 8:
        ans = temp.as_oct()
    elif base == 16:
        ans = temp.as_hex()

    return ans

def calculate(base):
    try:
        text = entry.get()

        separators = ['+', '-', '*', '/']
        separator_pattern = '|'.join(re.escape(sep) for sep in separators)
        parts = re.split(f'({separator_pattern})', text)
        lhs=''
        rhs=''
        op=''
        temp=0
        for part in parts:
            if re.match(separator_pattern,part):
                op=part
            elif lhs != '':
                rhs=part
            else:
                lhs=part
            if op != '' and lhs != '' and rhs != '':
                temp = evaluate(lhs,op,rhs,base)
                lhs=temp
                op=''
                rhs=''
            elif op == '' and lhs != '' and rhs == '':
                temp = evaluate(lhs,'+','0',base)
                lhs=temp
                op=''
                rhs=''

        entry.delete(0, tk.END)
        entry.insert(0, temp)
    except Exception as e:
        print(e)
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an Entry widget to display the input and results
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the numbers and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '= b2', '= b8', '= b16', 'C'
]

row_val = 1
col_val = 0

for button in buttons:
    if button.startswith('='):
        if button == '=':
            tk.Button(window, text=button, padx=20, pady=20, command=lambda base=10: calculate(base)).grid(row=row_val, column=col_val)
        if button == '= b2':
            tk.Button(window, text=button, padx=20, pady=20, command=lambda base=2: calculate(base)).grid(row=row_val, column=col_val)
        if button == '= b8':
            tk.Button(window, text=button, padx=20, pady=20, command=lambda base=8: calculate(base)).grid(row=row_val, column=col_val)
        if button == '= b16':
            tk.Button(window, text=button, padx=20, pady=20, command=lambda base=16: calculate(base)).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(window, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()