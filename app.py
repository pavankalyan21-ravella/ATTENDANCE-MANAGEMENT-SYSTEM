import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    # Create students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL
        )
    """)
    # Create attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (roll_no) REFERENCES students(roll_no)
        )
    """)
    conn.commit()
    conn.close()

# --- GUI APPLICATION ---
class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("600x450")
        
        # Heading
        title = tk.Label(root, text="Attendance Management System", font=("Arial", 16, "bold"), fg="blue")
        title.pack(pady=10)

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create Tab Frames
        self.tab_register = ttk.Frame(self.notebook)
        self.tab_attendance = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_register, text="Register Student")
        self.notebook.add(self.tab_attendance, text="Mark & View Attendance")

        self.setup_register_tab()
        self.setup_attendance_tab()

    # --- TAB 1: REGISTER STUDENT ---
    def setup_register_tab(self):
        # Roll Number Input
        lbl_roll = tk.Label(self.tab_register, text="Roll Number:", font=("Arial", 11))
        lbl_roll.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.ent_roll = tk.Entry(self.tab_register, font=("Arial", 11))
        self.ent_roll.grid(row=0, column=1, padx=10, pady=10)

        # Name Input
        lbl_name = tk.Label(self.tab_register, text="Student Name:", font=("Arial", 11))
        lbl_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.ent_name = tk.Entry(self.tab_register, font=("Arial", 11))
        self.ent_name.grid(row=1, column=1, padx=10, pady=10)

        # Submit Button
        btn_reg = tk.Button(self.tab_register, text="Register", bg="green", fg="white", font=("Arial", 11, "bold"), command=self.register_student)
        btn_reg.grid(row=2, column=0, columnspan=2, pady=20, ipadx=20)

    def register_student(self):
        roll = self.ent_roll.get().strip()
        name = self.ent_name.get().strip()

        if not roll or not name:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect("attendance.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO students (roll_no, name) VALUES (?, ?)", (roll, name))
            conn.commit()
            messagebox.showinfo("Success", f"Student {name} registered successfully!")
            self.ent_roll.delete(0, tk.END)
            self.ent_name.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", f"Roll Number '{roll}' already exists!")
        finally:
            conn.close()

    # --- TAB 2: MARK & VIEW ATTENDANCE ---
    def setup_attendance_tab(self):
        # Roll Number to Mark Attendance
        lbl_att_roll = tk.Label(self.tab_attendance, text="Roll Number:", font=("Arial", 11))
        lbl_att_roll.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.ent_att_roll = tk.Entry(self.tab_attendance, font=("Arial", 11))
        self.ent_att_roll.grid(row=0, column=1, padx=10, pady=10)

        # Status Combobox
        lbl_status = tk.Label(self.tab_attendance, text="Status:", font=("Arial", 11))
        lbl_status.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.combo_status = ttk.Combobox(self.tab_attendance, values=["Present", "Absent"], state="readonly", font=("Arial", 11))
        self.combo_status.set("Present")
        self.combo_status.grid(row=1, column=1, padx=10, pady=10)

        # Mark Button
        btn_mark = tk.Button(self.tab_attendance, text="Mark Attendance", bg="blue", fg="white", font=("Arial", 10, "bold"), command=self.mark_attendance)
        btn_mark.grid(row=2, column=0, columnspan=2, pady=10, ipadx=10)

        # Treeview to display recorded attendance
        self.tree = ttk.Treeview(self.tab_attendance, columns=("Roll No", "Date", "Status"), show="headings", height=5)
        self.tree.heading("Roll No", text="Roll No")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Status", text="Status")
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=15, sticky="nsew")

        # Load Current Records
        self.load_attendance_records()

    def mark_attendance(self):
        roll = self.ent_att_roll.get().strip()
        status = self.combo_status.get()
        date_today = datetime.now().strftime("%Y-%m-%d")

        if not roll:
            messagebox.showerror("Error", "Please enter a Roll Number!")
            return

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        
        # Check if student exists
        cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
        student = cursor.fetchone()

        if not student:
            messagebox.showerror("Error", "Student not found! Please register first.")
            conn.close()
            return

        # Record attendance
        cursor.execute("INSERT INTO attendance (roll_no, date, status) VALUES (?, ?, ?)", (roll, date_today, status))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Attendance marked as '{status}' for {roll}!")
        self.ent_att_roll.delete(0, tk.END)
        self.load_attendance_records()

    def load_attendance_records(self):
        # Clear existing tree data
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT roll_no, date, status FROM attendance ORDER BY id DESC")
        rows = cursor.fetchall()
        
        for row in rows:
            self.tree.insert("", "end", values=row)
        conn.close()

# --- MAIN RUN ---
if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
