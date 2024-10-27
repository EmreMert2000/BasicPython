import tkinter as tk
from tkinter import messagebox
import csv
import os


EXPENSE_FILE = "expenses.csv"


def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    if category and amount:
        with open(EXPENSE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([category, amount])
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        load_expenses()
    else:
        messagebox.showwarning("Uyarı", "Kategori ve miktar girin.")


def load_expenses():
    expenses_listbox.delete(0, tk.END)
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                expenses_listbox.insert(tk.END, f"{row[0]}: {row[1]} TL")


root = tk.Tk()
root.title("Gider Takip Uygulaması")

category_label = tk.Label(root, text="Kategori")
category_label.pack()
category_entry = tk.Entry(root, width=30)
category_entry.pack(pady=5)

amount_label = tk.Label(root, text="Miktar (TL)")
amount_label.pack()
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)


add_button = tk.Button(root, text="Gider Ekle", command=add_expense)
add_button.pack(pady=10)


expenses_listbox = tk.Listbox(root, width=50, height=10)
expenses_listbox.pack(pady=10)


load_expenses()

root.mainloop()
