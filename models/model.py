import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,create_engine,ForeignKey,Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


Base = declarative_base()
# Base.metadata.bind = create_engine('sqlite:///hospital.db')
engine =create_engine('sqlite:///hospital.db')



class User(Base):
  __tablename__ = "users"

  id = Column(Integer(), primary_key = True)
  name = Column(String())
  email = Column(String())
  password = Column(String())
  phone = Column(Integer())
  role = Column(String())

class Patient(Base):
  __tablename__ = "patients"

  id = Column(Integer(), primary_key=True)
  name = Column(String())
  phone = Column(Integer()) 
  date_birth = Column(String())
  gender = Column(String())
  address = Column(String())
  user_id = Column(Integer(), ForeignKey('users.id'))   

class Doctor(Base):
   __tablename__ = "doctors"

   id = Column(Integer(), primary_key = True)
   name = Column(String())
   specialization = Column(String())
   department_id = Column(Integer(), ForeignKey('departments.id'))
   license_number = Column(String())

class Department(Base):
    __tablename__ = "departments"
  
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    description = Column(String())
    doctors = relationship("Doctor", backref = "department")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer(), primary_key = True)
    date = Column(String())
    time = Column(String())
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))
    department_id = Column(Integer(), ForeignKey('departments.id')) 

class Prescription(Base):
    __tablename__ = "prescriptions" 

    id = Column(Integer(), primary_key = True)  
    date = Column(String()) 
    patient_id = Column(Integer(), ForeignKey('patients.id')) 
    medical_record_id = Column(Integer(), ForeignKey('medical_records.id')) 


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer(), primary_key = True)
    name = Column(String())
    description = Column(String())
    prescription_id = Column(Integer(), ForeignKey('prescriptions.id')) 

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer(), primary_key = True)
    date = Column(String())
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))
    department_id = Column(Integer(), ForeignKey('departments.id'))
    prescription_id = Column(Integer(), ForeignKey('prescriptions.id')) 
    diagnosis = Column(String())
    treatment = Column(String())

class Billing(Base):
    __tablename__ = "billings"

    id = Column(Integer(), primary_key = True)
    date = Column(String())
    patient_id = Column(Integer(), ForeignKey('patients.id'))
    doctor_id = Column(Integer(), ForeignKey('doctors.id'))
    department_id = Column(Integer(), ForeignKey('departments.id'))
    total_amount = Column(Integer())
    payment_status = Column(String()) 


session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
