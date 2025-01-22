import tkinter as tk
import os
import random

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_entry.delete(0, tk.END)
        update_task_list()

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def mark_done():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index] += " (Done)"
        update_task_list()

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks.pop(task_index)
        update_task_list()

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
        update_task_list()

def update_mantra():
    random_mantra = random.choice(mantras)
    mantra_label.config(text=random_mantra)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650")

username = os.getenv("USERNAME") or os.getenv("USER") or "User"

title_label = tk.Label(root, text=f"{username}'s To-Do List", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.pack(pady=5)

tasks = []

task_listbox = tk.Listbox(root, width=35, height=15, font=("Helvetica", 12))
task_listbox.pack(pady=20)

done_button = tk.Button(root, text="Mark as Done", font=("Helvetica", 12), command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_button.pack(pady=5)

mantras = [
    "Believe in yourself and all that you are.",
    "Every day is a new beginning.",
    "Success is not final, failure is not fatal.",
    "Keep pushing forward.",
    "Embrace the journey, not just the destination.",
    "The best way to predict the future is to create it.",
    "You are stronger than you think.",
    "Focus on progress, not perfection."
]

mantra_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"), wraplength=380, justify="center")
mantra_label.pack(pady=20)

update_mantra()

load_tasks()
root.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(), root.destroy()])

root.mainloop()
