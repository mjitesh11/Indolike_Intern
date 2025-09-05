import tkinter as tk

# Function to update the expression in entry box
def press(num):
    entry_var.set(entry_var.get() + str(num))

# Function to evaluate expression
def equalpress():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry
def clear():
    entry_var.set("")

# Function to open calculator window
def start_calculator():
    calc_window = tk.Toplevel(root)
    calc_window.title("Simple Calculator")
    calc_window.geometry("320x400")
    calc_window.configure(bg="lightgray")

    global entry_var
    entry_var = tk.StringVar()

    entry = tk.Entry(calc_window, textvariable=entry_var, font=('Arial', 18), bd=8, relief="ridge", justify="right")
    entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

    # Buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            btn = tk.Button(calc_window, text=text, width=5, height=2, bg="lightgreen",
                            command=equalpress)
        else:
            btn = tk.Button(calc_window, text=text, width=5, height=2, bg="lightblue",
                            command=lambda t=text: press(t))
        btn.grid(row=row, column=col, padx=5, pady=5)

    # Clear and Exit buttons
    clear_btn = tk.Button(calc_window, text="Clear", width=12, height=2, bg="orange", command=clear)
    clear_btn.grid(row=5, column=0, columnspan=2, pady=5)

    exit_btn = tk.Button(calc_window, text="Exit", width=12, height=2, bg="red", command=calc_window.destroy)
    exit_btn.grid(row=5, column=2, columnspan=2, pady=5)


# Main window
root = tk.Tk()
root.title("Calculator Launcher")
root.geometry("300x200")

start_btn = tk.Button(root, text="Start Calculator", command=start_calculator, width=20, height=2, bg="lightgreen")
start_btn.pack(pady=40)

exit_main = tk.Button(root, text="Exit", command=root.destroy, width=20, height=2, bg="red")
exit_main.pack()

root.mainloop()
