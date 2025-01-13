# Code created by J. Takeshwar (Tanvas)


import tkinter as tk
from tkinter import messagebox

def terminal_calculator():
    """
    Function to provide a terminal-based calculator.
    Allows the user to input calculations and displays the results.
    Type 'exit' to close the terminal calculator.
    """
    print("\nTerminal Calculator")
    print("Enter 'exit' to quit.")

    while True:
        user_input = input("Enter calculation: ")
        if user_input.lower() == 'exit':
            print("Exiting Terminal Calculator...")
            break
        try:
            result = eval(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

def gui_calculator():
    """
    Function to provide a GUI-based calculator using Tkinter.
    Includes basic arithmetic operations and displays calculation history.
    """
    history = []  # List to store the history of calculations

    def calculate():
        """
        Function to evaluate the expression entered in the input field.
        Updates the input field with the result and stores it in history.
        """
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            history.append(f"{expression} = {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Input: {e}")

    def clear():
        """
        Function to clear the input field.
        """
        entry.delete(0, tk.END)

    def show_history():
        """
        Function to display a new window showing the history of calculations.
        """
        if history:
            history_window = tk.Toplevel(root)
            history_window.title("Calculation History")
            history_window.geometry("400x300")
            tk.Label(history_window, text="History", font=("Arial", 16)).pack(pady=10)
            history_text = tk.Text(history_window, wrap=tk.WORD, font=("Arial", 12))
            history_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
            history_text.insert(tk.END, "\n".join(history))
            history_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo("History", "No calculations yet.")

    # Setting up the main Tkinter window
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x600")

    # Entry widget for input
    entry = tk.Entry(root, width=24, font=("Arial", 24), justify='right')
    entry.grid(row=0, column=0, columnspan=4, pady=20)

    # Button layout and configurations
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3, "#FF6666"),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3, "#FFCC66"),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3, "#66CCFF"),
        ('C', 4, 0, None, "#FF9999"), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3, "#99FF99"),
        ('=', 5, 0, 4, "#CCCCFF"), ('History', 6, 0, 4, "#CCCCFF")
    ]

    # Creating and placing buttons in the grid
    for (text, row, col, *span) in buttons:
        color = span[1] if len(span) > 1 else None
        if text == '=':
            tk.Button(root, text=text, width=15, height=2, bg=color, font=("Arial", 14), command=calculate).grid(row=row, column=col, columnspan=span[0])
        elif text == 'C':
            tk.Button(root, text=text, width=7, height=2, bg=color, font=("Arial", 14), command=clear).grid(row=row, column=col)
        elif text == 'History':
            tk.Button(root, text=text, width=15, height=2, bg=color, font=("Arial", 14), command=show_history).grid(row=row, column=col, columnspan=span[0])
        else:
            tk.Button(root, text=text, width=7, height=2, bg=color, font=("Arial", 14), 
                      command=lambda t=text: entry.insert(tk.END, t)).grid(row=row, column=col)

    root.mainloop()

if __name__ == "__main__":
    """
    Main entry point of the program.
    Prompts the user to choose between GUI or terminal calculator modes.
    """
    print("Choose Calculator Mode:")
    print("1. GUI Calculator")
    print("2. Terminal Calculator")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        gui_calculator()
    elif choice == '2':
        terminal_calculator()
    else:
        print("Invalid choice. Exiting...")
