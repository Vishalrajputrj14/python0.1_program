import tkinter as tk
from tkinter import ttk, messagebox
import re
import mysql.connector


class Database:
    def __init__(self, host="localhost", user="root", password="vishal", database="formdb"):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            self.conn.database = database
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS registrations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone VARCHAR(20),
                age INT,
                gender VARCHAR(20),
                country VARCHAR(50),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            self.conn.commit()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"MySQL Connection Failed:\n{e}")

    def insert(self, data: dict):
        query = """
        INSERT INTO registrations (name, email, phone, age, gender, country)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            data["name"],
            data["email"],
            data["phone"],
            data["age"],
            data["gender"],
            data["country"]
        )
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT id, name, email, phone, age, gender, country, created_at FROM registrations")
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()


class FormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form (MySQL + OOP)")
        self.root.geometry("500x450")

        self.db = Database(user="root", password="vishal", database="formdb")

        container = ttk.Frame(root, padding=16)
        container.pack(fill=tk.BOTH, expand=True)

        ttk.Label(container, text="Register", font=("Helvetica", 16, "bold")).pack(pady=(0,10))

        form_frame = ttk.Frame(container)
        form_frame.pack(fill=tk.BOTH, expand=True)

        # Name
        ttk.Label(form_frame, text="Full Name:").grid(row=0, column=0, sticky=tk.W, pady=6)
        self.name_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.name_var, width=35).grid(row=0, column=1, pady=6)

        # Email
        ttk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky=tk.W, pady=6)
        self.email_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.email_var, width=35).grid(row=1, column=1, pady=6)

        # Phone
        ttk.Label(form_frame, text="Phone:").grid(row=2, column=0, sticky=tk.W, pady=6)
        self.phone_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.phone_var, width=35).grid(row=2, column=1, pady=6)

        # Age
        ttk.Label(form_frame, text="Age:").grid(row=3, column=0, sticky=tk.W, pady=6)
        self.age_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.age_var, width=35).grid(row=3, column=1, pady=6)

        # Gender
        ttk.Label(form_frame, text="Gender:").grid(row=4, column=0, sticky=tk.W, pady=6)
        self.gender_var = tk.StringVar(value="Other")
        gframe = ttk.Frame(form_frame)
        gframe.grid(row=4, column=1, sticky=tk.W)
        ttk.Radiobutton(gframe, text="Male", value="Male", variable=self.gender_var).pack(side=tk.LEFT, padx=4)
        ttk.Radiobutton(gframe, text="Female", value="Female", variable=self.gender_var).pack(side=tk.LEFT, padx=4)
        ttk.Radiobutton(gframe, text="Other", value="Other", variable=self.gender_var).pack(side=tk.LEFT, padx=4)

        # Country
        ttk.Label(form_frame, text="Country:").grid(row=5, column=0, sticky=tk.W, pady=6)
        self.country_var = tk.StringVar()
        countries = ["India", "United States", "United Kingdom", "Australia", "Canada", "Other"]
        self.country_cb = ttk.Combobox(form_frame, textvariable=self.country_var, values=countries, state="readonly", width=33)
        self.country_cb.grid(row=5, column=1, pady=6)
        self.country_cb.set(countries[0])

        # Buttons
        btn_frame = ttk.Frame(container)
        btn_frame.pack(pady=(12,0))
        ttk.Button(btn_frame, text="Submit", command=self.on_submit).pack(side=tk.LEFT, padx=8)
        ttk.Button(btn_frame, text="Reset", command=self.on_reset).pack(side=tk.LEFT, padx=8)
        ttk.Button(btn_frame, text="View All Submissions", command=self.view_submissions).pack(side=tk.LEFT, padx=8)
        ttk.Button(btn_frame, text="Quit", command=self.on_quit).pack(side=tk.LEFT, padx=8)

    def validate(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        phone = self.phone_var.get().strip()
        age = self.age_var.get().strip()

        if not name:
            return False, "Name is required."
        if not email or not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            return False, "Valid Email is required."
        if phone and (not phone.isdigit() or not (7 <= len(phone) <= 15)):
            return False, "Phone must be digits (7-15 characters)."
        if age and (not age.isdigit() or not (0 < int(age) < 120)):
            return False, "Enter a valid age."

        return True, ""

    def on_submit(self):
        valid, msg = self.validate()
        if not valid:
            messagebox.showerror("Validation Error", msg)
            return

        data = {
            "name": self.name_var.get().strip(),
            "email": self.email_var.get().strip(),
            "phone": self.phone_var.get().strip() or None,
            "age": int(self.age_var.get().strip()) if self.age_var.get().strip() else None,
            "gender": self.gender_var.get(),
            "country": self.country_var.get()
        }
        try:
            self.db.insert(data)
            messagebox.showinfo("Success", "Data saved in MySQL successfully!")
            self.on_reset()
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not save data:\n{e}")

    def on_reset(self):
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")
        self.age_var.set("")
        self.gender_var.set("Other")
        self.country_cb.current(0)

    def on_quit(self):
        self.db.close()
        self.root.destroy()

    def view_submissions(self):
        records = self.db.fetch_all()
        if not records:
            messagebox.showinfo("No Data", "No submissions found!")
            return

        # Naya window
        win = tk.Toplevel(self.root)
        win.title("All Submissions")
        win.geometry("900x400")

        cols = ["ID", "Name", "Email", "Phone", "Age", "Gender", "Country", "Created At"]
        tree = ttk.Treeview(win, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill=tk.BOTH, expand=True)

        for row in records:
            tree.insert("", tk.END, values=row)

        # Scrollbar
        scrollbar = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        print("Hello, code run ho raha hai ✅")

