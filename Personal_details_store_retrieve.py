import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# Database Setup
def create_database():
    conn = sqlite3.connect('person_details.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS persons (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 surname TEXT,
                 aadhaar TEXT,
                 pan TEXT,
                 mobile TEXT)''')
    conn.commit()
    conn.close()


create_database()


# First GUI: Upload Details
class UploadDetailsApp:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='lightblue')  # Background color of the frame
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Labels
        tk.Label(self.root, text="Name:", bg='lightblue', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10,
                                                                                           pady=5, sticky=tk.W)
        tk.Label(self.root, text="Surname:", bg='lightblue', font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=10,
                                                                                              pady=5, sticky=tk.W)
        tk.Label(self.root, text="Aadhaar Card:", bg='lightblue', font=('Arial', 12, 'bold')).grid(row=2, column=0,
                                                                                                   padx=10, pady=5,
                                                                                                   sticky=tk.W)
        tk.Label(self.root, text="PAN Card:", bg='lightblue', font=('Arial', 12, 'bold')).grid(row=3, column=0, padx=10,
                                                                                               pady=5, sticky=tk.W)
        tk.Label(self.root, text="Mobile Number:", bg='lightblue', font=('Arial', 12, 'bold')).grid(row=4, column=0,
                                                                                                    padx=10, pady=5,
                                                                                                    sticky=tk.W)

        # Entry fields
        self.name_entry = tk.Entry(self.root, font=('Arial', 12))
        self.surname_entry = tk.Entry(self.root, font=('Arial', 12))
        self.aadhaar_entry = tk.Entry(self.root, font=('Arial', 12))
        self.pan_entry = tk.Entry(self.root, font=('Arial', 12))
        self.mobile_entry = tk.Entry(self.root, font=('Arial', 12))

        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)
        self.aadhaar_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)
        self.pan_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.EW)
        self.mobile_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.EW)

        # Buttons
        tk.Button(self.root, text="Submit", command=self.submit_details, width=20, height=2, bg='green', fg='white',
                  font=('Arial', 12, 'bold')).grid(row=5, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Refresh", command=self.refresh_fields, width=20, height=2, bg='blue', fg='white',
                  font=('Arial', 12, 'bold')).grid(row=6, column=0, columnspan=2, pady=10)

    def submit_details(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        aadhaar = self.aadhaar_entry.get()
        pan = self.pan_entry.get()
        mobile = self.mobile_entry.get()

        if not all([name, surname, aadhaar, pan, mobile]):
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect('person_details.db')
        c = conn.cursor()
        c.execute('''INSERT INTO persons (name, surname, aadhaar, pan, mobile)
                     VALUES (?, ?, ?, ?, ?)''', (name, surname, aadhaar, pan, mobile))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Details uploaded successfully!")
        self.refresh_fields()

    def refresh_fields(self):
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.aadhaar_entry.delete(0, tk.END)
        self.pan_entry.delete(0, tk.END)
        self.mobile_entry.delete(0, tk.END)


# Second GUI: Retrieve Details
class RetrieveDetailsApp:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.root.configure(bg='lightgrey')  # Background color of the frame
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Labels
        tk.Label(self.root, text="Name:", bg='lightgrey', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10,
                                                                                           pady=5, sticky=tk.W)
        tk.Label(self.root, text="Surname:", bg='lightgrey', font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=10,
                                                                                              pady=5, sticky=tk.W)

        # Entry fields
        self.name_entry = tk.Entry(self.root, font=('Arial', 12))
        self.surname_entry = tk.Entry(self.root, font=('Arial', 12))

        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)

        # Buttons
        tk.Button(self.root, text="Retrieve", command=self.retrieve_details, width=20, height=2, bg='orange',
                  fg='white', font=('Arial', 12, 'bold')).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Refresh", command=self.refresh_fields, width=20, height=2, bg='red', fg='white',
                  font=('Arial', 12, 'bold')).grid(row=3, column=0, columnspan=2, pady=10)

    def retrieve_details(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()

        if not all([name, surname]):
            messagebox.showerror("Error", "Name and surname are required!")
            return

        conn = sqlite3.connect('person_details.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM persons WHERE name=? AND surname=?''', (name, surname))
        data = c.fetchone()
        conn.close()

        if data:
            details = f"Name: {data[1]}\nSurname: {data[2]}\nAadhaar: {data[3]}\nPAN: {data[4]}\nMobile: {data[5]}"
            messagebox.showinfo("Details", details)
        else:
            messagebox.showerror("Error", "No data found for the provided name and surname.")

    def refresh_fields(self):
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)


# Main Application: Combining Both GUIs
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Person Details Manager")

        self.tab_control = ttk.Notebook(self.root)

        self.upload_tab = tk.Frame(self.tab_control)
        self.retrieve_tab = tk.Frame(self.tab_control)

        self.tab_control.add(self.upload_tab, text="Upload Details")
        self.tab_control.add(self.retrieve_tab, text="Retrieve Details")
        self.tab_control.pack(expand=1, fill="both")

        self.upload_app = UploadDetailsApp(self.upload_tab)
        self.retrieve_app = RetrieveDetailsApp(self.retrieve_tab)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()