#Name:Devanshu Kumar Tandan
#ERP=RU-26-01373
# P.S=77 "Hospital Management Scheduler"
from datetime import datetime

# Global dictionary storing appointments: {appt_id: appointment_data}
appointments = {}
id_counter = 101


def parse_date(date_str):
    """Validate and parse date in DD-MM-YYYY format using datetime."""
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        return None


def is_valid_slot(time_str):
    """Validate 30-minute slot format and ensure it falls between 09:00 and 16:30."""
    try:
        t = datetime.strptime(time_str, "%H:%M")
        # Minute must be :00 or :30
        if t.minute not in (0, 30):
            return False
        # Slot start time must be between 09:00 and 16:30 inclusive
        start_bound = datetime.strptime("09:00", "%H:%M")
        end_bound = datetime.strptime("16:30", "%H:%M")
        return start_bound <= t <= end_bound
    except ValueError:
        return False


# --- CRUD Functions ---

def book_appointment(patient, doctor, date_str, time_str):
    global id_counter

    # 1. Date Validation
    if not parse_date(date_str):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return

    # 2. Time Slot Validation
    if not is_valid_slot(time_str):
        print("Invalid time slot. Slots must be between 09:00 and 16:30 in 30-minute increments.")
        return

    # 3. Doctor Availability Check
    for appt in appointments.values():
        if (
            appt["doctor"].lower() == doctor.lower()
            and appt["date"] == date_str
            and appt["time"] == time_str
        ):
            print(f"Slot unavailable: {doctor} already has an appointment on {date_str} at {time_str}.")
            return

    # Generate ID: starts from A101
    appt_id = f"A{id_counter}"
    id_counter += 1

    # Store appointment in dictionary
    appointments[appt_id] = {
        "ID": appt_id,
        "patient": patient,
        "doctor": doctor,
        "date": date_str,
        "time": time_str,
    }

    print(f"Appointment booked. ID: {appt_id} | {patient} | {doctor} | {date_str} {time_str}")


def view_all():
    if not appointments:
        print("No appointments scheduled.")
        print("Total appointments: 0")
        return

    for appt in appointments.values():
        print(f"{appt['ID']} | {appt['patient']} | {appt['doctor']} | {appt['date']} {appt['time']}")
    print(f"Total appointments: {len(appointments)}")


def reschedule_appointment(appt_id, new_date_str, new_time_str):
    if appt_id not in appointments:
        print(f"Error: Appointment {appt_id} not found.")
        return

    if not parse_date(new_date_str):
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return

    if not is_valid_slot(new_time_str):
        print("Invalid time slot. Slots must be between 09:00 and 16:30 in 30-minute increments.")
        return

    doctor = appointments[appt_id]["doctor"]

    # Check conflict with existing appointments
    for aid, appt in appointments.items():
        if aid != appt_id and appt["doctor"].lower() == doctor.lower():
            if appt["date"] == new_date_str and appt["time"] == new_time_str:
                print(f"Slot unavailable: {doctor} already has an appointment on {new_date_str} at {new_time_str}.")
                return

    appointments[appt_id]["date"] = new_date_str
    appointments[appt_id]["time"] = new_time_str
    print(f"Appointment {appt_id} rescheduled to {new_date_str} {new_time_str}.")


def cancel_appointment(appt_id):
    if appt_id in appointments:
        del appointments[appt_id]
        print(f"Appointment {appt_id} cancelled.")
    else:
        print(f"Error: Appointment {appt_id} not found.")


# --- Main Menu Console Loop ---

def main():
    while True:
        print("\n--- Clinic Appointment System ---")
        print("1. Book")
        print("2. View all")
        print("3. Reschedule")
        print("4. Cancel")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            patient = input("Patient: ").strip()
            doctor = input("Doctor: ").strip()
            date_str = input("Date: ").strip()
            time_str = input("Time: ").strip()
            book_appointment(patient, doctor, date_str, time_str)

        elif choice == "2":
            view_all()

        elif choice == "3":
            appt_id = input("Appointment ID: ").strip()
            new_date = input("New Date (DD-MM-YYYY): ").strip()
            new_time = input("New Time (HH:MM): ").strip()
            reschedule_appointment(appt_id, new_date, new_time)

        elif choice == "4":
            appt_id = input("Appointment ID: ").strip()
            cancel_appointment(appt_id)

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid selection. Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()