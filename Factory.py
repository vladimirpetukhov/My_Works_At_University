import tkinter as tk
from tkinter import messagebox
from IFactory import IFactory
from services import Service
from db import DbContext as db


class Factory(IFactory):
    def __init__(self, master, db):
        super().__init__(master, db)
        self.master = master

    def create_widgets(self):
         # Part
        self.part_text = tk.StringVar()
        self.part_label = self.part_label = tk.Label(
            self.master, text='Part Name', font=('bold', 14), pady=20)
        self.part_label.grid(row=0, column=0, sticky=tk.W)
        self.part_entry = tk.Entry(self.master, textvariable=self.part_text)
        self.part_entry.grid(row=0, column=1)

        # Customer
        self.customer_text = tk.StringVar()
        self.customer_label = tk.Label(
            self.master, text='User', font=('bold', 14))
        self.customer_label.grid(row=0, column=2, sticky=tk.W)
        self.customer_entry = tk.Entry(
            self.master, textvariable=self.customer_text)
        self.customer_entry.grid(row=0, column=3)

        # Retailer
        self.retailer_text = tk.StringVar()
        self.retailer_label = tk.Label(
            self.master, text='Retailer', font=('bold', 14))
        self.retailer_label.grid(row=1, column=0, sticky=tk.W)
        self.retailer_entry = tk.Entry(
            self.master, textvariable=self.retailer_text)
        self.retailer_entry.grid(row=1, column=1)
        # Price
        self.price_text = tk.StringVar()
        self.price_label = tk.Label(
            self.master, text='Price', font=('bold', 14))
        self.price_label.grid(row=1, column=2, sticky=tk.W)
        self.price_entry = tk.Entry(self.master, textvariable=self.price_text)
        self.price_entry.grid(row=1, column=3)

        # Parts list (listbox)
        self.parts_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.parts_list.grid(row=3, column=0, columnspan=3,
                             rowspan=6, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        # Set scrollbar to parts
        self.parts_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.parts_list.yview)

        # Bind select
        self.parts_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_btn = tk.Button(
            self.master, text="Add", width=12)
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(
            self.master, text="Remove", width=12)
        self.remove_btn.grid(row=2, column=1)

        self.update_btn = tk.Button(
            self.master, text="Update", width=12)
        self.update_btn.grid(row=2, column=2)
        # Clear Input Fields
        self.exit_btn = tk.Button(
            self.master, text="Cansel", width=12, command=self.clear_text)
        self.exit_btn.grid(row=2, column=3)

        def add_item(self):
            if self.part_text.get() == '' or self.customer_text.get() == '' or self.retailer_text.get() == '' or self.price_text.get() == '':
                messagebox.showerror(
                    "Required Fields", "Please include all fields")
            return
        print(self.part_text.get())
        # Insert into DB
        # db.insert(self.part_text.get(), self.customer_text.get(),
        #           self.retailer_text.get(), '0')
        # Clear list
        self.parts_list.delete(0, tk.END)
        # Insert into list
        self.parts_list.insert(tk.END, (self.part_text.get(), self.customer_text.get(
        ), self.retailer_text.get(), self.price_text.get()))
        print(self.price_text.get())
        self.clear_text()
        # self.populate_list()

    def select_item(self, event):
            # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.parts_list.curselection()[0]
            # Get selected item
            self.selected_item = self.parts_list.get(index)
            print(selected_item) # Print tuple

            # Add text to entries
            self.part_entry.delete(0, tk.END)
            self.part_entry.insert(tk.END, self.selected_item[1])
            self.customer_entry.delete(0, tk.END)
            self.customer_entry.insert(tk.END, self.selected_item[2])
            self.retailer_entry.delete(0, tk.END)
            self.retailer_entry.insert(tk.END, self.selected_item[3])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(tk.END, self.selected_item[4])
        except IndexError:
            pass

    # Clear all text fields
    def clear_text(self):
        self.part_entry.delete(0, tk.END)
        self.customer_entry.delete(0, tk.END)
        self.retailer_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
