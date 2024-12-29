import tkinter as tk
from tkinter import messagebox

# Global list to store the history of calculations
history_list = []

# Function definitions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

# Button click handler
def button_click(value):
    current_text = display.get()

    if value == "C":  # Clear display
        display.delete(0, tk.END)
    elif value == "=":  # Evaluate the expression
        try:
            # Parse the operation and numbers
            if "^" in current_text:
                base, exp = map(float, current_text.split("^"))
                result = power(base, exp)
            elif "%" in current_text:
                num1, num2 = map(float, current_text.split("%"))
                result = remainder(num1, num2)
            else:
                result = eval(current_text)
            
            operation = f"{current_text} = {result}"
            history_list.append(operation)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            display.delete(0, tk.END)
    elif value == "History":  # Show history
        if not history_list:
            messagebox.showinfo("History", "No past calculations to show.")
        else:
            history_text = "\n".join(history_list)
            messagebox.showinfo("History", history_text)
    elif value == "Reset":  # Clear history
        history_list.clear()
        messagebox.showinfo("Reset", "History cleared. Calculator reset.")
    else:  # Append to display
        display.insert(tk.END, value)

# Create the main application window
root = tk.Tk()
root.title("Real-World Calculator")
root.geometry("400x600")
root.configure(bg="#f7f9fc")

# Display Entry
display = tk.Entry(root, font=("Arial", 24), justify="right", bg="#e8f4f8", borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4, pady=20, padx=10, sticky="we")

# Button configuration
button_config = {
    "font": ("Arial", 18),
    "width": 5,
    "height": 2,
    "bg": "#f1f1f1",
    "relief": "raised",
    "borderwidth": 2,
}

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("History", 5, 1), ("Reset", 5, 2), ("^", 5, 3),
    ("%", 6, 0)
]

# Add buttons to the grid
for (text, row, col) in buttons:
    # Customize Reset button
    if text == "Reset":
        custom_config = button_config.copy()
        custom_config.update({"bg": "red", "fg": "white"})
        button = tk.Button(root, text=text, command=lambda value=text: button_click(value), **custom_config)
    else:
        button = tk.Button(root, text=text, command=lambda value=text: button_click(value), **button_config)
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
