import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone and email and address:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo('Success', f'Contact {name} added successfully!')
        clear_entries()
    else:
        messagebox.showwarning('Warning', 'Please fill in all fields.')

def view_contact():
    name = name_entry.get()
    if name in contacts:
        contact_info = contacts[name]
        messagebox.showinfo('Contact Details', f'Name: {name}\nPhone: {contact_info["Phone"]}\nEmail: {contact_info["Email"]}\nAddress: {contact_info["Address"]}')
    else:
        messagebox.showwarning('Warning', 'Contact not found.')

def view_all_contacts():
    if contacts:
        contact_list = '\n'.join(contact for contact in contacts)
        messagebox.showinfo('All Contacts', f'Contacts:\n{contact_list}')
    else:
        messagebox.showinfo('No Contacts', 'No contacts available.')

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo('Success', f'Contact {name} deleted successfully!')
        clear_entries()
        
    else:
        messagebox.showwarning('Warning', 'Contact not found.')

def update_contact():
    name = name_entry.get()
    
    if name in contacts:
        # Prompt user for updated information
        updated_phone = phone_entry.get()
        updated_email = email_entry.get()
        updated_address = address_entry.get()

        # Update contact information
        contacts[name]["Phone"] = updated_phone
        contacts[name]["Email"] = updated_email
        contacts[name]["Address"] = updated_address

        if name and updated_phone and updated_email and updated_address:
            messagebox.showinfo('Success', 'Contact updated successfully!')

        else:
            messagebox.showwarning('Warning', 'Contact not found.')
            
    else:
        messagebox.showwarning('Warning', 'Contact not found.')


def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title('Contact Book')
root.configure(bg='#FFBBFF')

# Styles
entry_style = {'width': 20, 'font': ('Arial', 12)}
button_style = {'font': ('Arial', 12), 'padx': 10, 'pady': 5, 'bg': '#EEAEEE', 'fg': '#8B2252'}

# Labels and Entries
labels = ['Name:', 'Phone:', 'Email:', 'Address:']
for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text, **entry_style)
    label.grid(row=i, column=0, padx=5, pady=5)
    
name_entry = tk.Entry(root, **entry_style)
name_entry.grid(row=0, column=1, padx=5, pady=5)
phone_entry = tk.Entry(root, **entry_style)
phone_entry.grid(row=1, column=1, padx=5, pady=5)
email_entry = tk.Entry(root, **entry_style)
email_entry.grid(row=2, column=1, padx=5, pady=5)
address_entry= tk.Entry(root, **entry_style)
address_entry.grid(row=3, column=1, padx=5)

# Buttons
buttons = ['Add Contact', 'View Contact', 'View All Contacts', 'Delete Contact', 'Update Contact']
commands = [add_contact, view_contact, view_all_contacts, delete_contact, update_contact]
for i, (button_text, command) in enumerate(zip(buttons, commands)):
    button = tk.Button(root, text=button_text, command=command, **button_style)
    button.grid(row=i + 4, column=0, columnspan=2, sticky='WE', padx=5, pady=5)

root.mainloop()




