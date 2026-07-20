# Attendance Management System

A lightweight, browser-based application for maintaining a class roster and marking daily attendance. It works without a server or account, and keeps information saved in the browser.

## Features

- **Add student names** — Create a class roster by entering each student's name.
- **Mark attendance** — Set every student to **Present** or **Absent**. Select the same status again to return the student to an unmarked state.
- **Attendance table** — The class roster is displayed in a clean table-style list with each student's name and attendance controls.
- **Attendance totals** — See the total students, present students, and absent students at a glance.
- **Data storage** — The roster and attendance selections are stored locally in the browser using `localStorage`, so they remain available after a page refresh.
- **Remove students** — Remove one student from the roster or clear the complete roster when needed.

## How to use

1. Open `index.html` in any modern web browser.
2. Type a name in the **Student name** field.
3. Select **Add student** to add the student to the roster.
4. Use **Present** or **Absent** beside each student to record today's attendance.
5. The summary cards update automatically.

## Data table structure

| Field | Description |
| --- | --- |
| Student name | The name entered for a student. |
| Attendance status | One of `Present`, `Absent`, or unmarked. |

## Data storage details

The application stores the roster in the current browser under the key `rollcall-students-v1`.

Example stored data:

```json
[
  { "name": "Aarav Sharma", "status": "present" },
  { "name": "Meera Patel", "status": "absent" }
]
```

> Clearing browser site data or using a different browser/device removes access to this locally stored roster.

## Technology

- HTML
- CSS
- Vanilla JavaScript
- Browser `localStorage`

## Running the project

No installation is needed. Download or open the project folder, then double-click `index.html`.

