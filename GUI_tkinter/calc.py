import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(enum1.get())
        num2 = float(enum2.get())

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        resultlabel.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed!")

def resetnum():
    enum1.delete(0, tk.END)
    enum2.delete(0, tk.END)
    resultlabel.config(text="Result: ")
    enum1.focus()

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")

# -------- Layout using Grid ----------
tk.Label(root, text="Enter first number:", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=5)
enum1 = tk.Entry(root, font=("Arial", 12))
enum1.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Enter second number:", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=5)
enum2 = tk.Entry(root, font=("Arial", 12))
enum2.grid(row=1, column=1, pady=5, padx=5)

# Buttons
badd = tk.Button(root, text="+", width=10, command=lambda: calculate("+"))
bsub = tk.Button(root, text="-", width=10, command=lambda: calculate("-"))
bmul = tk.Button(root, text="*", width=10, command=lambda: calculate("*"))
bdiv = tk.Button(root, text="/", width=10, command=lambda: calculate("/"))
breset = tk.Button(root, text="Reset", width=10, command=resetnum)

badd.grid(row=2, column=0, pady=10)
bsub.grid(row=2, column=1)
bmul.grid(row=3, column=0, pady=5)
bdiv.grid(row=3, column=1)
breset.grid(row=4,column=0, pady=5)


# Result label
resultlabel = tk.Label(root, text="Result: ", font=("Arial", 14))
resultlabel.grid(row=5, column=0, columnspan=2, pady=15)

root.mainloop()
