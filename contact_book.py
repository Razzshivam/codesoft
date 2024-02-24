import tkinter as tk
from tkinter import ttk, messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x400")

        self.contacts = []
        self.contact_items = {}

        # Create UI elements
        self.title_label = ttk.Label(root, text="Contact Book", font=("Helvetica", 20))
        self.title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.name_label = ttk.Label(root, text="Name:")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        self.phone_label = ttk.Label(root, text="Phone:")
        self.phone_label.grid(row=2, column=0, padx=5, pady=5)
        self.phone_entry = ttk.Entry(root)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        self.email_label = ttk.Label(root, text="Email:")
        self.email_label.grid(row=3, column=0, padx=5, pady=5)
        self.email_entry = ttk.Entry(root)
        self.email_entry.grid(row=3, column=1, padx=5, pady=5)

        self.address_label = ttk.Label(root, text="Address:")
        self.address_label.grid(row=4, column=0, padx=5, pady=5)
        self.address_entry = ttk.Entry(root)
        self.address_entry.grid(row=4, column=1, padx=5, pady=5)

        self.gender_label = ttk.Label(root, text="Gender:")
        self.gender_label.grid(row=5, column=0, padx=5, pady=5)
        self.gender_var = tk.StringVar()
        self.gender_combobox = ttk.Combobox(root, textvariable=self.gender_var, values=["Male", "Female", "Other"])
        self.gender_combobox.grid(row=5, column=1, padx=5, pady=5)

        self.add_button = ttk.Button(root, text="Add", command=self.add_contact)
        self.add_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.delete_button = ttk.Button(root, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=6, column=2, padx=5, pady=5, sticky="WE")

        self.update_button = ttk.Button(root, text="Update", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

        self.search_button = ttk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=2, padx=5, pady=5, sticky="WE")

        self.contact_tree = ttk.Treeview(root, columns=("Name", "Phone", "Email", "Address", "Gender"))
        self.contact_tree.grid(row=8, column=0, columnspan=3, padx=5, pady=5)
        self.contact_tree.heading("#0", text="ID")
        self.contact_tree.heading("Name", text="Name")
        self.contact_tree.heading("Phone", text="Phone")
        self.contact_tree.heading("Email", text="Email")
        self.contact_tree.heading("Address", text="Address")
        self.contact_tree.heading("Gender", text="Gender")
        self.contact_tree.bind("<ButtonRelease-1>", self.select_contact)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        gender = self.gender_var.get()

        if name and phone:
            # Check if contact already exists
            if not any(contact["phone"] == phone for contact in self.contacts):
                contact_id = len(self.contacts) + 1
                self.contacts.append({"id": contact_id, "name": name, "phone": phone, "email": email, "address": address, "gender": gender})
                self.display_contact(contact_id)
            else:
                messagebox.showerror("Error", "Contact with this phone number already exists.")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def delete_contact(self):
        selected_item = self.contact_tree.selection()
        if selected_item:
            contact_id = int(self.contact_tree.item(selected_item, "text"))
            self.contacts.pop(contact_id - 1)
            self.display_contacts()

    def update_contact(self):
        selected_item = self.contact_tree.selection()
        if selected_item:
            contact_id = int(self.contact_tree.item(selected_item, "text"))
            contact = self.contacts[contact_id - 1]
            contact["name"] = self.name_entry.get()
            contact["phone"] = self.phone_entry.get()
            contact["email"] = self.email_entry.get()
            contact["address"] = self.address_entry.get()
            contact["gender"] = self.gender_var.get()
            self.display_contact(contact_id)

    def search_contact(self):
        keyword = self.name_entry.get()
        if keyword:
            found_contacts = []
            for contact in self.contacts:
                if keyword.lower() in contact["name"].lower() or keyword in contact["phone"]:
                    found_contacts.append(contact)
            if found_contacts:
                self.display_contacts(found_contacts)
            else:
                messagebox.showinfo("Search Result", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search keyword.")

    def select_contact(self, event):
        selected_item = self.contact_tree.selection()
        if selected_item:
            contact_id = int(self.contact_tree.item(selected_item, "text"))
            contact = self.contacts[contact_id - 1]
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact["name"])
            self.phone_entry.insert(0, contact["phone"])
            self.email_entry.insert(0, contact["email"])
            self.address_entry.insert(0, contact["address"])
            self.gender_var.set(contact["gender"])

    def display_contact(self, contact_id):
        contact = self.contacts[contact_id - 1]
        if contact_id not in self.contact_items:
            item = self.contact_tree.insert("", "end", text=contact["id"], values=(contact["name"], contact["phone"], contact["email"], contact["address"], contact["gender"]))
            self.contact_items[contact_id] = item
        else:
            self.contact_tree.item(self.contact_items[contact_id], values=(contact["name"], contact["phone"], contact["email"], contact["address"], contact["gender"]))

    def display_contacts(self, contacts=None):
        if not contacts:
            contacts = self.contacts
        for contact_id in self.contact_items:
            self.contact_tree.delete(self.contact_items[contact_id])
        self.contact_items = {}
        for contact in contacts:
            self.display_contact(contact["id"])

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
