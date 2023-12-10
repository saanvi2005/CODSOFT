import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        list_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = list_tasks.curselection()[0]
        list_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def update_task():
    try:
        selected_task_index = list_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task:
            list_tasks.delete(selected_task_index)
            list_tasks.insert(selected_task_index, updated_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def clear_tasks():
    list_tasks.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

entry_task = tk.Entry(frame_input, width=30)
entry_task.grid(row=0, column=0, padx=5)

add_button = tk.Button(frame_input, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=1, padx=5)

frame_tasks = tk.Frame(root)
frame_tasks.pack(padx=10, pady=5)

list_tasks = tk.Listbox(frame_tasks, width=50, height=10)
list_tasks.pack()

update_button = tk.Button(root, text="Update Task", width=48, command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=48, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=48, command=clear_tasks)
clear_button.pack()

root.mainloop()



    