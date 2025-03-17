from database import session
from models import Patient, Doctor, MedicalRecord, Prescription, Appointment, Billing
from datetime import datetime, timedelta
from faker import Faker
import random

fake = Faker()

# Clear existing data (optional)
session.query(MedicalRecord).delete()
session.query(Prescription).delete()
session.query(Appointment).delete()
session.query(Billing).delete()
session.query(Patient).delete()
session.query(Doctor).delete()
session.commit()

# Generate 20 random patients
patients = [Patient(name=fake.name()) for _ in range(20)]
session.add_all(patients)
session.commit()

# Get patient IDs
patients = session.query(Patient).all()

# Generate 5 random doctors
doctors = [Doctor(name=f"Dr. {fake.name()}") for _ in range(5)]
session.add_all(doctors)
session.commit()

# Get doctor IDs
doctors = session.query(Doctor).all()

# Generate random medical records
medical_records = [
    MedicalRecord(
        patient_id=random.choice(patients).id,
        diagnosis=random.choice(["Flu", "Cold", "Allergy", "Diabetes", "Hypertension"]),
        date=fake.date_this_decade()
    )
    for _ in range(20)
]

# Generate random prescriptions
prescriptions = [
    Prescription(
        patient_id=random.choice(patients).id,
        medication=random.choice(["Paracetamol", "Ibuprofen", "Antibiotic", "Insulin"]),
        dosage=random.choice(["500mg", "250mg", "100mg", "10ml"])
    )
    for _ in range(20)
]

# Generate random appointments
appointments = [
    Appointment(
        patient_id=random.choice(patients).id,
        doctor_id=random.choice(doctors).id,
        date=fake.date_between(start_date="-30d", end_date="+30d")
    )
    for _ in range(20)
]

# Generate random billing data
bills = [
    Billing(
        patient_id=random.choice(patients).id,
        amount=random.randint(500, 5000)
    )
    for _ in range(20)
]

# Add and commit all data
session.add_all(medical_records + prescriptions + appointments + bills)
session.commit()

print("✅ Database seeded with 20+ randomized records!")
