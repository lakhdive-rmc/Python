import tkinter as tk
from tkinter import messagebox

def addnumbers():
    try:
        num1 = int(enum1.get())
        num2 = int(enum2.get())
        result = num1 + num2
        resultlabel.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter only integers!")

def resetnum():
    enum1.delete(0, tk.END)
    enum2.delete(0, tk.END)
    resultlabel.config(text="Result: ")
    enum1.focus()
# Main window
root = tk.Tk()
root.title("Addition of Two Numbers")
root.geometry("300x300")
root.resizable(False, False)

# Widgets
label1 = tk.Label(root, text="Enter first number:", font=("Arial", 12))
label1.pack(pady=5)

enum1 = tk.Entry(root, font=("Arial", 12))
enum1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:", font=("Arial", 12))
label2.pack(pady=5)

enum2 = tk.Entry(root, font=("Arial", 12))
enum2.pack(pady=5)

badd = tk.Button(root, text="Add", font=("Arial", 12), command=addnumbers)
badd.pack(pady=5)

breset = tk.Button(root, text="Reset", font=("Arial", 12), command=resetnum)
breset.pack(pady=10)

resultlabel = tk.Label(root, text="Result: ", font=("Arial", 14))
resultlabel.pack(pady=10)

root.mainloop()
