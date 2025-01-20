import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
import os
import csv

# File to store contacts
DATA_FILE = "contacts.json"

# Load contacts from the file
def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts(contacts):
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# ------------------- Contact Management Functions -------------------

def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        favorite_marker = "⭐ " if contact.get("favorite") else ""
        contact_list.insert(tk.END, f"{favorite_marker}{contact['name']} - {contact['phone']}")

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name:
        return
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    if not phone:
        return
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    birthday = simpledialog.askstring("Add Contact", "Enter Birthday (YYYY-MM-DD):")
    group = simpledialog.askstring("Add Contact", "Enter Group (e.g., Family, Friends, Work):")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
        "birthday": birthday,
        "group": group,
        "favorite": False
    })
    save_contacts(contacts)
    refresh_contact_list()
    messagebox.showinfo("Success", "Contact added successfully!")

def view_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to view.")
        return
    index = selected[0]
    contact = contacts[index]
    details = (
        f"Name: {contact['name']}\n"
        f"Phone: {contact['phone']}\n"
        f"Email: {contact['email']}\n"
        f"Address: {contact['address']}\n"
        f"Birthday: {contact['birthday'] or 'N/A'}\n"
        f"Group: {contact['group'] or 'N/A'}"
    )
    messagebox.showinfo("Contact Details", details)

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter name, phone number, or group:")
    if not query:
        return
    results = [c for c in contacts if query.lower() in c["name"].lower() or query in c["phone"] or query.lower() in (c.get("group") or "").lower()]
    if results:
        result_text = "\n\n".join(
            [f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}\nBirthday: {c['birthday'] or 'N/A'}\nGroup: {c['group'] or 'N/A'}" for c in results]
        )
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("No Results", "No contacts found.")

def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")
        return
    index = selected[0]
    confirmation = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
    if confirmation:
        del contacts[index]
        save_contacts(contacts)
        refresh_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")

def call_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to call.")
        return
    index = selected[0]
    contact = contacts[index]
    messagebox.showinfo("Calling", f"Calling {contact['name']} at {contact['phone']}...")

def export_contacts():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    try:
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Address", "Birthday", "Group", "Favorite"])
            for contact in contacts:
                writer.writerow([contact["name"], contact["phone"], contact["email"], contact["address"],
                                 contact["birthday"], contact["group"], contact.get("favorite", False)])
        messagebox.showinfo("Success", "Contacts exported successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export contacts: {e}")

def import_contacts():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path:
        return
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["favorite"] = row.get("favorite", "False") == "True"
                contacts.append(row)
        save_contacts(contacts)
        refresh_contact_list()
        messagebox.showinfo("Success", "Contacts imported successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to import contacts: {e}")

def toggle_favorite():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a contact to mark as favorite.")
        return
    index = selected[0]
    contacts[index]["favorite"] = not contacts[index].get("favorite", False)
    save_contacts(contacts)
    refresh_contact_list()

def toggle_dark_mode():
    if root["bg"] == "#f9f5f0":
        root.configure(bg="#2c3e50")
        contact_list.configure(bg="#34495e", fg="#ecf0f1")
    else:
        root.configure(bg="#f9f5f0")
        contact_list.configure(bg="#fef9e7", fg="#34495e")

# ------------------- Dialer Functions -------------------

def open_dialer():
    dialer_window = tk.Toplevel(root)
    dialer_window.title("Dialer")
    dialer_window.geometry("300x200")

    phone_number_var = tk.StringVar()

    def dial():
        phone_number = phone_number_var.get()
        if phone_number:
            messagebox.showinfo("Dialing", f"Dialing {phone_number}...")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid phone number.")

    label = tk.Label(dialer_window, text="Enter Phone Number:", font=("Helvetica", 12))
    label.pack(pady=10)

    phone_entry = tk.Entry(dialer_window, textvariable=phone_number_var, font=("Helvetica", 14), width=20)
    phone_entry.pack(pady=10)

    dial_button = tk.Button(dialer_window, text="Dial", command=dial, font=("Helvetica", 12), bg="#d5f5e3", fg="#2c3e50")
    dial_button.pack(pady=10)

    dialer_window.mainloop()

# ------------------- UI Initialization -------------------

def ui_main_menu():
    global root, contact_list
    root = tk.Tk()
    root.title("Contact Management System")
    root.geometry("600x600")

    # Homely Theme
    root.configure(bg="#f9f5f0")
    title_label = tk.Label(
        root, text="Contact Management System", font=("Helvetica", 16, "bold"), bg="#f9f5f0", fg="#2c3e50"
    )
    title_label.pack(pady=10)

    contact_list = tk.Listbox(root, height=20, width=60, font=("Helvetica", 12), bg="#fef9e7", fg="#34495e")
    contact_list.pack(pady=10)
    refresh_contact_list()

    button_frame = tk.Frame(root, bg="#f9f5f0")
    button_frame.pack(pady=10)

    # Organize buttons into groups
    row1 = ["➕", "🔍", "📞"]  # Add Contact, Search, Call
    row2 = ["👁️", "❌", "⭐"]  # View, Delete, Favorite
    row3 = ["📤", "📥", "🌙"]  # Export, Import, Dark Mode
    row4 = ["🚪", "📲"]        # Exit, Dialer

    # Place buttons in the grid layout
    buttons = {
        "➕": add_contact,
        "🔍": search_contact,
        "📞": call_contact,
        "👁️": view_contact,
        "❌": delete_contact,
        "⭐": toggle_favorite,
        "📤": export_contacts,
        "📥": import_contacts,
        "🌙": toggle_dark_mode,
        "🚪": root.destroy,
        "📲": open_dialer
    }

    button_rows = [row1, row2, row3, row4]
    for i, row in enumerate(button_rows):
        for j, symbol in enumerate(row):
            button = tk.Button(button_frame, text=symbol, command=buttons[symbol], width=5, font=("Helvetica", 14), bg="#d5f5e3", fg="#2c3e50")
            button.grid(row=i, column=j, padx=10, pady=10)

    root.mainloop()

# ------------------- Main Entry Point -------------------

if __name__ == "__main__":
    contacts = load_contacts()
    ui_main_menu()
