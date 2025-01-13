import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import json
import os
from datetime import datetime
from tkcalendar import Calendar


class RoundButton(tk.Canvas):
    def __init__(self, parent, text, command, bg_color, text_color, radius=20, **kwargs):
        super().__init__(parent, width=radius * 2, height=radius * 2, bg=parent.cget("bg"), highlightthickness=0, **kwargs)
        self.command = command
        self.radius = radius
        self.bg_color = bg_color
        self.text_color = text_color

        # Draw the button
        self.create_oval(2, 2, radius * 2, radius * 2, fill=bg_color, outline="")
        self.create_text(radius, radius, text=text, fill=text_color, font=("Arial", 12, "bold"))

        # Bind events
        self.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if self.command:
            self.command()


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mobile-Friendly To-Do List")
        self.root.geometry("350x600")
        self.root.configure(bg="#d9f0ff")  # Light blue background for the main window

        self.tasks = self.load_tasks()

        # Title
        self.title_label = tk.Label(
            root, text="To-Do List", font=("Arial", 18, "bold"), fg="#ffffff", bg="#3b5998"  # Blue header
        )
        self.title_label.pack(fill=tk.X)

        # Add Task Section
        self.task_frame = tk.Frame(root, bg="#e8f5e9")  # Light green background for the task input section
        self.task_frame.pack(pady=10, fill=tk.X)

        self.task_entry = tk.Entry(self.task_frame, width=20, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.priority_var = tk.StringVar(value="Normal")
        self.priority_dropdown = ttk.Combobox(
            self.task_frame,
            textvariable=self.priority_var,
            values=["Low", "Normal", "High"],
            state="readonly",
            width=10,
            font=("Arial", 10),
        )
        self.priority_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.add_button = tk.Button(
            self.task_frame, text="+", command=self.add_task, font=("Arial", 12), bg="#4CAF50", fg="white", width=3
        )
        self.add_button.grid(row=0, column=2, padx=5, pady=5)

        # Task List
        self.task_listbox = tk.Listbox(
            root, width=35, height=15, font=("Arial", 10), selectmode=tk.SINGLE, bg="#fdfdfd", fg="#333333"
        )
        self.task_listbox.pack(pady=10)

        # Buttons Section
        self.button_frame = tk.Frame(root, bg="#fffde7")  # Light yellow background for the button section
        self.button_frame.pack(pady=10)

        self.complete_button = RoundButton(
            self.button_frame, text="\u2714", command=self.mark_completed, bg_color="#2196F3", text_color="white"
        )
        self.complete_button.grid(row=0, column=0, padx=10)

        self.delete_button = RoundButton(
            self.button_frame, text="\U0001F5D1", command=self.delete_task, bg_color="#F44336", text_color="white"
        )
        self.delete_button.grid(row=0, column=1, padx=10)

        self.filter_var = tk.StringVar(value="All")
        self.filter_dropdown = ttk.Combobox(
            self.button_frame,
            textvariable=self.filter_var,
            values=["All", "Completed", "Pending"],
            state="readonly",
            width=10,
            font=("Arial", 10),
        )
        self.filter_dropdown.grid(row=0, column=2, padx=10)
        self.filter_dropdown.bind("<<ComboboxSelected>>", self.filter_tasks)

        self.sort_var = tk.StringVar(value="None")
        self.sort_dropdown = ttk.Combobox(
            root,
            textvariable=self.sort_var,
            values=["None", "By Due Date", "Alphabetically"],
            state="readonly",
            width=15,
            font=("Arial", 10),
        )
        self.sort_dropdown.pack(pady=10)
        self.sort_dropdown.bind("<<ComboboxSelected>>", self.sort_tasks)

        # Calendar
        self.calendar = Calendar(root, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        self.calendar.pack(pady=10)

        # Search Section
        self.search_frame = tk.Frame(root, bg="#e3f2fd")  # Light blue background for the search section
        self.search_frame.pack(pady=10)

        self.search_button = RoundButton(
            self.search_frame, text="\U0001F50D", command=self.search_task, bg_color="#FFC107", text_color="black"
        )
        self.search_button.grid(row=0, column=0, padx=10)

        self.load_tasks_to_listbox()

    # Rest of the methods remain unchanged...


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
