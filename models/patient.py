from database import session
from models import Patient, MedicalRecord, Prescription, Appointment, Billing

def register_patient():
    name = input("Enter patient name: ")
    patient = Patient(name=name)
    session.add(patient)
    session.commit()
    print("Patient registered successfully!")

def view_medical_records():
    patient_id = input("Enter your patient ID: ")
    records = session.query(MedicalRecord).filter_by(patient_id=patient_id).all()

    if not records:
        print("No medical history found.")
        return

    for record in records:
        print(f"Date: {record.date} | Diagnosis: {record.diagnosis}")

def view_prescriptions():
    patient_id = input("Enter your patient ID: ")
    prescriptions = session.query(Prescription).filter_by(patient_id=patient_id).all()

    if not prescriptions:
        print("No prescriptions found.")
        return

    for prescription in prescriptions:
        print(f"Medication: {prescription.medication} | Dosage: {prescription.dosage}")

def generate_bill():
    patient_id = input("Enter patient ID: ")
    amount = input("Enter billing amount: ")
    bill = Billing(patient_id=patient_id, amount=amount)
    session.add(bill)
    session.commit()
    print("Bill paid successfully!")

def make_appointment():
    patient_id = input("Enter your patient ID: ")
    doctor_id = input("Enter doctor ID: ")
    date = input("Enter appointment date (YYYY-MM-DD): ")
    appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, date=date)
    session.add(appointment)
    session.commit()
    print("Appointment booked successfully!")

def view_my_appointments():
    patient_id = input("Enter your patient ID: ")
    appointments = session.query(Appointment).filter_by(patient_id=patient_id).all()

    if not appointments:
        print("No appointments found.")
        return

    for appointment in appointments:
        print(f"Doctor ID: {appointment.doctor_id} | Date: {appointment.date}")

def patient_menu():
    while True:
        print("\n👤 PATIENT MENU")
        print("1. Register as Patient")
        print("2. View Medical History")
        print("3. View Prescriptions")
        print("4. Pay Bills")
        print("5. Make an Appointment")
        print("6. View My Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()
        elif choice == "2":
            view_medical_records()
        elif choice == "3":
            view_prescriptions()
        elif choice == "4":
            generate_bill()
        elif choice == "5":
            make_appointment()
        elif choice == "6":
            view_my_appointments()
        elif choice == "7":
            print("Exiting patient menu...")
            break
        else:
            print("Invalid choice. Try again.")
