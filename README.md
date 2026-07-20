# Attendance Management System

A Python-based application for managing student records and recording daily attendance. The project demonstrates essential Python skills including file handling, list and dictionary management, input validation, table formatting, and persistent data storage.

## 🚀 Key Features

**Add Student Names:** Add student names to create and maintain a class roster.

**Mark Attendance:** Record each student as **Present** or **Absent** for the day.

**Attendance Tables:** Display a structured attendance table containing student names and their current attendance status.

**Data Storage:** Save student records and attendance data to a local file so information remains available between program runs.

**Attendance Summary:** Calculate and display the total number of students, students present, and students absent.

**Input Validation:** Handles invalid selections and empty student names safely to keep records accurate.

## 📁 Project Structure

```text
Attendance-Management-System/
│
├── attendance_manager.py    # Core Python program for roster and attendance management
├── attendance_data.json     # Locally stored student and attendance records
├── attendance_report.txt    # Generated attendance summary report
└── README.md                # Project documentation
```

## 📊 Attendance Table

| Student Name | Attendance Status |
| --- | --- |
| Aarav Sharma | Present |
| Meera Patel | Absent |

## 💾 Data Storage

Student records are stored locally in `attendance_data.json`. A typical record uses the following format:

```json
[
  { "name": "Aarav Sharma", "status": "Present" },
  { "name": "Meera Patel", "status": "Absent" }
]
```

## 🛠️ Tech Stack

**Language:** Python 3.x

**Storage Format:** JSON and text files

**Concepts Used:** File I/O, lists, dictionaries, functions, loops, conditionals, exception handling, string formatting, input validation, and automated report generation.

## ▶️ How to Run

1. Ensure Python 3 is installed.
2. Open a terminal in the project directory.
3. Run the application:

```bash
python attendance_manager.py
```

4. Follow the menu prompts to add students, mark attendance, view the table, and save data.
