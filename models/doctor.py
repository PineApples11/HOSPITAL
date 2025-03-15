from database import session
from models import Doctor, MedicalRecord, Prescription, Appointment, Patient

def register_doctor():
    name = input("Enter doctor name: ")
    doctor = Doctor(name=name)
    session.add(doctor)
    session.commit()
    print("Doctor registered successfully!")

def add_medical_record():
    patient_id = input("Enter patient ID: ")
    diagnosis = input("Enter diagnosis: ")
    date = input("Enter date (YYYY-MM-DD): ")
    record = MedicalRecord(patient_id=patient_id, diagnosis=diagnosis, date=date)
    session.add(record)
    session.commit()
    print("Medical record added!")

def prescribe_medication():
    patient_id = input("Enter patient ID: ")
    medication = input("Enter medication name: ")
    dosage = input("Enter dosage: ")
    prescription = Prescription(patient_id=patient_id, medication=medication, dosage=dosage)
    session.add(prescription)
    session.commit()
    print("Medication prescribed!")

def view_all_my_patients():
    doctor_id = input("Enter your doctor ID: ")
    patients = session.query(Appointment.patient_id).filter_by(doctor_id=doctor_id).distinct().all()

    if not patients:
        print("No patients found.")
        return

    for patient in patients:
        patient_info = session.query(Patient).filter_by(id=patient.patient_id).first()
        print(f"Patient ID: {patient_info.id} | Name: {patient_info.name}")

def view_prescriptions():
    patient_id = input("Enter patient ID to view prescriptions: ")
    prescriptions = session.query(Prescription).filter_by(patient_id=patient_id).all()

    if not prescriptions:
        print("No prescriptions found.")
        return

    for prescription in prescriptions:
        print(f"Medication: {prescription.medication} | Dosage: {prescription.dosage}")

def doctor_menu():
    while True:
        print("\n🩺 DOCTOR MENU")
        print("1. Register as Doctor")
        print("2. Add Medical Record")
        print("3. Prescribe Medications")
        print("4. View All My Patients")
        print("5. View My Prescriptions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_doctor()
        elif choice == "2":
            add_medical_record()
        elif choice == "3":
            prescribe_medication()
        elif choice == "4":
            view_all_my_patients()
        elif choice == "5":
            view_prescriptions()
        elif choice == "6":
            print("Exiting doctor menu...")
            break
        else:
            print("Invalid choice. Try again.")
