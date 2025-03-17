import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.doctor import doctor_menu
from models.patient import patient_menu

# from models.doctor import doctor_menu
# from models.doctor import doctor_menu
# from models.patient import patient_menu
# from models.doctor import doctor_menu
 


def main_menu():
    while True:
        print("Welcome to Hospital Management System")
        print("Choose your role") 
        print("1. Doctor")
        print("2. Patient")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            doctor_menu()
        elif choice == "2":
            patient_menu()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()