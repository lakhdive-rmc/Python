import tkinter as tk
from tkinter import messagebox

def ctof():
    try:
        c = float(celsius.get())
        f = (c * 9/5) + 32
        resultlabel.config(text=f"{f:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

root = tk.Tk()
root.title("Celsius to Fahrenheit")
root.geometry("300x200+100+50") 

celsius = tk.Entry(root)
celsius.pack()

b1 = tk.Button(root, text="Convert", command=ctof)
b1.pack()

resultlabel = tk.Label(root, text="Result:")
resultlabel.pack()

root.mainloop()
