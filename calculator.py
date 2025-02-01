#####3
import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(value):
    current = entry.get()
    if value == "C":
        entry.delete(0, tk.END)  # clear box
    elif value == "=":
        try:
            result = eval(current)  # Evaluating the expression
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        entry.insert(tk.END, value)

# main window
root = tk.Tk()
root.title("Calculator")
root.geometry("340x550")  # window size
root.resizable(False, False)  # Disable resizing

root.config(bg="#2f4f4f")     # main window background colour

# entry widget for calculator display
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, relief=tk.RIDGE, justify="right", bg="#ffffff", fg="#000000")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout and styling
buttons = [
    ("7", "#f0f8ff"), ("8", "#f0f8ff"), ("9", "#f0f8ff"), ("/", "#f0f8ff"),
    ("4", "#f0f8ff"), ("5", "#f0f8ff"), ("6", "#f0f8ff"), ("*", "#f0f8ff"),
    ("1", "#f0f8ff"), ("2", "#f0f8ff"), ("3", "#f0f8ff"), ("-", "#f0f8ff"),
    ("C", "#ff6347"), ("0", "#f0f8ff"), ("=", "#98fb98"), ("+", "#f0f8ff")
]


row_val = 1         # adding buttons to the grid
col_val = 0

for button, color in buttons:
    tk.Button(
        root, text=button, width=5, height=2, font=("Arial", 14), 
        command=lambda b=button: button_click(b), bg=color, fg="#000000", 
        relief=tk.RAISED, bd=3
    ).grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(5):            # configuring grid weights
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# main event loop
root.mainloop()

