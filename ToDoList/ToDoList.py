import tkinter as tk
from tkinter import messagebox
import json
import os


TASKS_FILE = "tasks.json"


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Bir görev girin.")


def delete_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks_listbox.delete(index)
        tasks.pop(index)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Uyarı", "Silmek için bir görev seçin.")


def mark_task_complete():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        tasks_listbox.delete(index)
        task_text = tasks[index]["task"]
        if tasks[index]["completed"]:
            task_text += " (Tamamlandı)"
        tasks_listbox.insert(index, task_text)
        save_tasks(tasks)
    else:
        messagebox.showwarning("Uyarı", "Bir görev seçin.")


root = tk.Tk()
root.title("Görev Yöneticisi")

tasks = load_tasks()


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Görev Ekle", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Görev Sil", command=delete_task)
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Görevi Tamamlandı Olarak İşaretle", command=mark_task_complete)
complete_button.pack(pady=5)


tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

for task in tasks:
    task_text = task["task"] + (" (Tamamlandı)" if task["completed"] else "")
    tasks_listbox.insert(tk.END, task_text)

root.mainloop()
