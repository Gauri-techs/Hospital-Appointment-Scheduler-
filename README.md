# Clinic Appointment System

A lightweight, command-line Python application for managing clinic appointments. It supports booking, viewing, rescheduling, and canceling appointments with built-in date/time validation and doctor double-booking prevention.

## Features

* **Book Appointments:** Schedule appointments with automatic ID generation (`A101`, `A102`, etc.).
* **View All Appointments:** Display a formatted list of all scheduled appointments along with the total count.
* **Reschedule Appointments:** Update the date and time of an existing appointment while checking for scheduling conflicts.
* **Cancel Appointments:** Remove appointments from the system using their unique Appointment ID.
* **Smart Validation:**
  * **Date Format:** Enforces valid calendar dates in `DD-MM-YYYY` format.
  * **Time Slots:** Restricts bookings to 30-minute intervals (`:00` or `:30`) within clinic hours (`09:00` to `16:30` inclusive).
  * **Conflict Detection:** Case-insensitive check ensuring a doctor cannot be double-booked at the same date and time.

---

## Prerequisites

* **Python 3.6+** (uses only the Python Standard Library `datetime` module; no external packages required).

---

## Getting Started

1. **Save the script** as `appointment_system.py`.
2. **Run the application** from your terminal or command prompt:

```bash
python appointment_system.py
```

---

## Usage & Rules

When you run the script, an interactive console menu appears:

```text
--- Clinic Appointment System ---
1. Book
2. View all
3. Reschedule
4. Cancel
5. Exit
Enter choice (1-5):
```

### Input Formatting Rules

| Field | Format | Valid Examples | Invalid Examples |
| :--- | :--- | :--- | :--- |
| **Appointment ID** | `A` + Number | `A101`, `A102` | `101`, `a101` |
| **Date** | `DD-MM-YYYY` | `15-11-2026`, `03-04-2026` | `2026-11-15`, `31-02-2026` |
| **Time** | `HH:MM` (24-hr) | `09:00`, `13:30`, `16:30` | `08:30`, `10:15`, `17:00` |

### Sample Walkthrough

```text
Enter choice (1-5): 1
Patient: Rahul Sharma
Doctor: Dr. Patel
Date: 15-11-2026
Time: 10:30
Appointment booked. ID: A101 | Rahul Sharma | Dr. Patel | 15-11-2026 10:30

Enter choice (1-5): 2
A101 | Rahul Sharma | Dr. Patel | 15-11-2026 10:30
Total appointments: 1

Enter choice (1-5): 3
Appointment ID: A101
New Date (DD-MM-YYYY): 16-11-2026
New Time (HH:MM): 11:00
Appointment A101 rescheduled to 16-11-2026 11:00.

Enter choice (1-5): 4
Appointment ID: A101
Appointment A101 cancelled.
```

---

## Code Structure

* `parse_date(date_str)`: Validates that the input string matches the `DD-MM-YYYY` format.
* `is_valid_slot(time_str)`: Verifies that the time is in `HH:MM` format, ends in `:00` or `:30`, and falls between `09:00` and `16:30`.
* `book_appointment(patient, doctor, date_str, time_str)`: Validates inputs, checks doctor availability, assigns a unique ID, and stores the record in the global `appointments` dictionary.
* `view_all()`: Prints all active appointments and the total count.
* `reschedule_appointment(appt_id, new_date_str, new_time_str)`: Updates an existing record's date and time if the doctor is available.
* `cancel_appointment(appt_id)`: Deletes the specified appointment from memory.
* `main()`: Runs the interactive CLI loop.

---

## Limitations & Future Enhancements

* **In-Memory Storage:** Appointments are stored in a runtime dictionary (`appointments`) and reset when the program exits. Adding JSON, CSV, or SQLite persistence will allow data to be saved between sessions.
* **Past Date Check:** Currently, any valid calendar date is accepted. Comparing `parse_date(date_str)` against `datetime.now()` would prevent booking appointments in the past.
