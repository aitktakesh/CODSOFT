# Code created by J. TAKESHWAR(TANVAS)

import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import json
import os
from datetime import datetime
from tkcalendar import Calendar


# Custom class for creating a round button
class RoundButton(tk.Canvas):
    def __init__(self, parent, text, command, bg_color, text_color, radius=20, **kwargs):
        super().__init__(parent, width=radius * 2, height=radius * 2, bg=parent.cget("bg"), highlightthickness=0, **kwargs)
        self.command = command  # Function to be executed when the button is clicked
        self.radius = radius  # Radius of the button
        self.bg_color = bg_color  # Background color of the button
        self.text_color = text_color  # Text color on the button

        # Draw the button as a circle
        self.create_oval(2, 2, radius * 2, radius * 2, fill=bg_color, outline="")
        self.create_text(radius, radius, text=text, fill=text_color, font=("Arial", 12, "bold"))

        # Bind click event to the button
        self.bind("<Button-1>", self.on_click)

    # Function executed when the button is clicked
    def on_click(self, event):
        if self.command:
            self.command()


# Main To-Do application class
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TANVAS ToDoList App")  # Title of the application window
        self.root.geometry("350x600")  # Dimensions of the application window
        self.root.configure(bg="#f0f0f0")  # Background color of the application window

        self.tasks = self.load_tasks()  # Load tasks from the saved file

        # Application title
        self.title_label = tk.Label(root, text="TANVAS ToDoList App", font=("Arial", 16, "bold"), fg="#333", bg="#f0f0f0")
        self.title_label.pack(pady=5)

        # Task input section
        self.task_frame = tk.Frame(root, bg="#f0f0f0")
        self.task_frame.pack(pady=5)

        # Entry field for task title
        self.task_entry = tk.Entry(self.task_frame, width=20, font=("Arial", 12))
        self.task_entry.grid(row=0, column=0, padx=2)

        # Dropdown for selecting task priority
        self.priority_var = tk.StringVar(value="Normal")
        self.priority_dropdown = ttk.Combobox(
            self.task_frame,
            textvariable=self.priority_var,
            values=["Low", "Normal", "High"],
            state="readonly",
            width=10,
            font=("Arial", 10),
        )
        self.priority_dropdown.grid(row=0, column=1, padx=2)

        # Button to add a new task
        self.add_button = tk.Button(
            self.task_frame, text="+", command=self.add_task, font=("Arial", 12), bg="#4CAF50", fg="white", width=3
        )
        self.add_button.grid(row=0, column=2, padx=2)

        # Task list section
        self.task_listbox = tk.Listbox(root, width=35, height=15, font=("Arial", 10), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=5)
        self.task_listbox.bind("<<ListboxSelect>>", self.display_task_description)

        # Action buttons section
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=5)

        # Button to mark a task as completed
        self.complete_button = RoundButton(
            self.button_frame, text="\u2714", command=self.mark_completed, bg_color="#2196F3", text_color="white"
        )
        self.complete_button.grid(row=0, column=0, padx=2)

        # Button to delete a task
        self.delete_button = RoundButton(
            self.button_frame, text="\U0001F5D1", command=self.delete_task, bg_color="#F44336", text_color="white"
        )
        self.delete_button.grid(row=0, column=1, padx=2)

        # Dropdown for filtering tasks by status
        self.filter_var = tk.StringVar(value="All")
        self.filter_dropdown = ttk.Combobox(
            self.button_frame,
            textvariable=self.filter_var,
            values=["All", "Completed", "Pending"],
            state="readonly",
            width=10,
            font=("Arial", 10),
        )
        self.filter_dropdown.grid(row=0, column=2, padx=2)
        self.filter_dropdown.bind("<<ComboboxSelected>>", self.filter_tasks)

        # Dropdown for sorting tasks
        self.sort_var = tk.StringVar(value="None")
        self.sort_dropdown = ttk.Combobox(
            root,
            textvariable=self.sort_var,
            values=["None", "By Due Date", "Alphabetically"],
            state="readonly",
            width=15,
            font=("Arial", 10),
        )
        self.sort_dropdown.pack(pady=5)
        self.sort_dropdown.bind("<<ComboboxSelected>>", self.sort_tasks)

        # Calendar widget for selecting task due dates
        self.calendar = Calendar(root, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        self.calendar.pack(pady=5)
        self.calendar.bind("<<CalendarSelected>>", self.filter_tasks_by_date)

        # Search section
        self.search_frame = tk.Frame(root, bg="#f0f0f0")
        self.search_frame.pack(pady=5)

        # Button to search for tasks
        self.search_button = RoundButton(
            self.search_frame, text="\U0001F50D", command=self.search_task, bg_color="#FFC107", text_color="black"
        )
        self.search_button.grid(row=0, column=0, padx=2)

        # Load all tasks into the listbox
        self.load_tasks_to_listbox()

    # Function to load tasks from a file
    def load_tasks(self):
        try:
            os.makedirs("tasks", exist_ok=True)
            with open("tasks/tasks.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # Function to save tasks to a file
    def save_tasks(self):
        os.makedirs("tasks", exist_ok=True)
        with open("tasks/tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

    # Function to display tasks in the listbox
    def load_tasks_to_listbox(self, tasks=None):
        self.task_listbox.delete(0, tk.END)
        tasks = tasks if tasks is not None else self.tasks
        for task in tasks:
            status = "[\u2714]" if task.get("completed", False) else "[ ]"
            due_date = task.get("due_date", "No Due Date")
            priority = task.get("priority", "Normal")
            display_text = f"{status} {task.get('title', 'Untitled')} - {due_date} [Priority: {priority}]"
            self.task_listbox.insert(tk.END, display_text)

    # Function to show a task's description
    def display_task_description(self, event=None):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            return
        task_index = selected_index[0]
        task = self.tasks[task_index]
        description = task.get("description", "No description available.")
        messagebox.showinfo("Task Description", description)

    # Function to add a new task
    def add_task(self):
        task_title = self.task_entry.get().strip()
        if not task_title:
            messagebox.showwarning("Input Error", "Task title cannot be empty.")
            return

        task_description = simpledialog.askstring("Task Description", "Enter a description for the task:")
        due_date = self.calendar.get_date()
        priority = self.priority_var.get()

        self.tasks.append(
            {
                "title": task_title,
                "description": task_description or "",
                "due_date": due_date,
                "completed": False,
                "priority": priority,
            }
        )
        self.save_tasks()
        self.load_tasks_to_listbox()
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Task Added", f"Task '{task_title}' has been added successfully!")

    # Function to mark a task as completed
    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No task selected.")
            return
        task_index = selected_index[0]
        self.tasks[task_index]["completed"] = True
        self.save_tasks()
        self.load_tasks_to_listbox()
        messagebox.showinfo("Task Completed", "The selected task has been marked as completed.")

    # Function to delete a task
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Selection Error", "No task selected.")
            return
        task_index = selected_index[0]
        task_title = self.tasks[task_index].get("title", "Untitled")
        self.tasks.pop(task_index)
        self.save_tasks()
        self.load_tasks_to_listbox()
        messagebox.showinfo("Task Deleted", f"Task '{task_title}' has been deleted.")

    # Function to filter tasks based on their status
    def filter_tasks(self, event=None):
        filter_option = self.filter_var.get()
        filtered_tasks = []
        for task in self.tasks:
            if filter_option == "Completed" and task.get("completed", False):
                filtered_tasks.append(task)
            elif filter_option == "Pending" and not task.get("completed", False):
                filtered_tasks.append(task)
            elif filter_option == "All":
                filtered_tasks.append(task)
        self.load_tasks_to_listbox(filtered_tasks)

    # Function to sort tasks based on selected criteria
    def sort_tasks(self, event=None):
        sort_option = self.sort_var.get()
        if sort_option == "By Due Date":
            self.tasks.sort(key=lambda x: x.get("due_date", ""))
        elif sort_option == "Alphabetically":
            self.tasks.sort(key=lambda x: x.get("title", "").lower())
        self.save_tasks()
        self.load_tasks_to_listbox()

    # Function to search for tasks by title



    def search_task(self):
        search_term = simpledialog.askstring("Search Task", "Enter the task title to search:")
        if not search_term:
            return
        filtered_tasks = [task for task in self.tasks if search_term.lower() in task.get("title", "").lower()]
        self.load_tasks_to_listbox(filtered_tasks)

    # Function to filter tasks by the selected due date from the calendar
    def filter_tasks_by_date(self, event=None):
        selected_date = self.calendar.get_date()
        filtered_tasks = [task for task in self.tasks if task.get("due_date") == selected_date]
        self.load_tasks_to_listbox(filtered_tasks)



#main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
