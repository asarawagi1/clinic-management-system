-m pip install
import tkinter as tk
from tkinter import messagebox
import json
import os

# Define the Patient class
class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

# Define the Doctor class
class Doctor:
    def __init__(self, doctor_id, name, specialty, contact):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.contact = contact

# Define the Appointment class
class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

# Define the ClinicManagementSystem class
class ClinicManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.load_data()

    # Add a new patient
    def add_patient(self, patient):
        self.patients.append(patient)
        self.save_data()

    # View all patients
    def view_patients(self):
        return self.patients

    # Add a new doctor
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        self.save_data()

    # View all doctors
    def view_doctors(self):
        return self.doctors

    # Schedule an appointment
    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
        self.save_data()

    # View all appointments
    def view_appointments(self):
        return self.appointments

    # Save data to a file
    def save_data(self):
        data = {
            'patients': [vars(p) for p in self.patients],
            'doctors': [vars(d) for d in self.doctors],
            'appointments': [{
                'appointment_id': a.appointment_id,
                'patient_id': a.patient.patient_id,
                'doctor_id': a.doctor.doctor_id,
                'date': a.date,
                'time': a.time
            } for a in self.appointments]
        }
        with open('clinic_data.json', 'w') as f:
            json.dump(data, f)

    # Load data from a file
    def load_data(self):
        if os.path.exists('clinic_data.json'):
            with open('clinic_data.json', 'r') as f:
                data = json.load(f)
                for p in data['patients']:
                    self.patients.append(Patient(**p))
                for d in data['doctors']:
                    self.doctors.append(Doctor(**d))
                for a in data['appointments']:
                    patient = next((p for p in self.patients if p.patient_id == a['patient_id']), None)
                    doctor = next((d for d in self.doctors if d.doctor_id == a['doctor_id']), None)
                    if patient and doctor:
                        self.appointments.append(Appointment(
                            appointment_id=a['appointment_id'],
                            patient=patient,
                            doctor=doctor,
                            date=a['date'],
                            time=a['time']
                        ))

# GUI Application
class ClinicApp:
    def __init__(self, root, cms):
        self.cms = cms
        self.root = root
        self.root.title("Clinic Management System")

        # Patient Section
        self.patient_frame = tk.LabelFrame(root, text="Patients")
        self.patient_frame.grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.patient_frame, text="Patient ID:").grid(row=0, column=0)
        self.patient_id = tk.Entry(self.patient_frame)
        self.patient_id.grid(row=0, column=1)
        tk.Label(self.patient_frame, text="Name:").grid(row=1, column=0)
        self.patient_name = tk.Entry(self.patient_frame)
        self.patient_name.grid(row=1, column=1)
        tk.Label(self.patient_frame, text="Age:").grid(row=2, column=0)
        self.patient_age = tk.Entry(self.patient_frame)
        self.patient_age.grid(row=2, column=1)
        tk.Label(self.patient_frame, text="Gender:").grid(row=3, column=0)
        self.patient_gender = tk.Entry(self.patient_frame)
        self.patient_gender.grid(row=3, column=1)
        tk.Label(self.patient_frame, text="Contact:").grid(row=4, column=0)
        self.patient_contact = tk.Entry(self.patient_frame)
        self.patient_contact.grid(row=4, column=1)
        tk.Button(self.patient_frame, text="Add Patient", command=self.add_patient).grid(row=5, column=0, columnspan=2)

        # Doctor Section
        self.doctor_frame = tk.LabelFrame(root, text="Doctors")
        self.doctor_frame.grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.doctor_frame, text="Doctor ID:").grid(row=0, column=0)
        self.doctor_id = tk.Entry(self.doctor_frame)
        self.doctor_id.grid(row=0, column=1)
        tk.Label(self.doctor_frame, text="Name:").grid(row=1, column=0)
        self.doctor_name = tk.Entry(self.doctor_frame)
        self.doctor_name.grid(row=1, column=1)
        tk.Label(self.doctor_frame, text="Specialty:").grid(row=2, column=0)
        self.doctor_specialty = tk.Entry(self.doctor_frame)
        self.doctor_specialty.grid(row=2, column=1)
        tk.Label(self.doctor_frame, text="Contact:").grid(row=3, column=0)
        self.doctor_contact = tk.Entry(self.doctor_frame)
        self.doctor_contact.grid(row=3, column=1)
        tk.Button(self.doctor_frame, text="Add Doctor", command=self.add_doctor).grid(row=4, column=0, columnspan=2)

        # Appointment Section
        self.appointment_frame = tk.LabelFrame(root, text="Appointments")
        self.appointment_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        tk.Label(self.appointment_frame, text="Appointment ID:").grid(row=0, column=0)
        self.appointment_id = tk.Entry(self.appointment_frame)
        self.appointment_id.grid(row=0, column=1)
        tk.Label(self.appointment_frame, text="Patient ID:").grid(row=1, column=0)
        self.appointment_patient_id = tk.Entry(self.appointment_frame)
        self.appointment_patient_id.grid(row=1, column=1)
        tk.Label(self.appointment_frame, text="Doctor ID:").grid(row=2, column=0)
        self.appointment_doctor_id = tk.Entry(self.appointment_frame)
        self.appointment_doctor_id.grid(row=2, column=1)
        tk.Label(self.appointment_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0)
        self.appointment_date = tk.Entry(self.appointment_frame)
        self.appointment_date.grid(row=3, column=1)
        tk.Label(self.appointment_frame, text="Time (HH:MM):").grid(row=4, column=0)
        self.appointment_time = tk.Entry(self.appointment_frame)
        self.appointment_time.grid(row=4, column=1)
        tk.Button(self.appointment_frame, text="Schedule Appointment", command=self.schedule_appointment).grid(row=5, column=0, columnspan=2)

        # View Section
        self.view_frame = tk.LabelFrame(root, text="View Data")
        self.view_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(self.view_frame, text="View Patients", command=self.view_patients).grid(row=0, column=0)
        tk.Button(self.view_frame, text="View Doctors", command=self.view_doctors).grid(row=0, column=1)
        tk.Button(self.view_frame, text="View Appointments", command=self.view_appointments).grid(row=0, column=2)

    def add_patient(self):
        patient_id = self.patient_id.get()
        name = self.patient_name.get()
        age = self.patient_age.get()
        gender = self.patient_gender.get()
        contact = self.patient_contact.get()
        if patient_id and name and age and gender and contact:
            patient = Patient(patient_id, name, age, gender, contact)
            self.cms.add_patient(patient)
            messagebox.showinfo("Success", "Patient added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def add_doctor(self):
        doctor_id = self.doctor_id.get()
        name = self.doctor_name.get()
        specialty = self.doctor_specialty.get()
        contact = self.doctor_contact.get()
        if doctor_id and name and specialty and contact:
            doctor = Doctor(doctor_id, name, specialty, contact)
            self.cms.add_doctor(doctor)
            messagebox.showinfo("Success", "Doctor added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def schedule_appointment(self):
        appointment_id = self.appointment_id.get()
        patient_id = self.appointment_patient_id.get()
        doctor_id = self.appointment_doctor_id.get()
        date = self.appointment_date.get()
        time = self.appointment_time.get()
        patient = next((p for p in self.cms.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.cms.doctors if d.doctor_id == doctor_id), None)
        if appointment_id and patient and doctor and date and time:
            appointment = Appointment(appointment_id, patient, doctor, date, time)
            self.cms.schedule_appointment(appointment)
            messagebox.showinfo("Success", "Appointment scheduled successfully.")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields correctly.")

    def view_patients(self):
        patients = self.cms.view_patients()
        patient_data = "\n".join([f"ID: {p.patient_id}, Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Contact: {p.contact}" for p in patients])
        messagebox.showinfo("Patients", patient_data)

    def view_doctors(self):
        doctors = self.cms.view_doctors()
        doctor_data = "\n".join([f"ID: {d.doctor_id}, Name: {d.name}, Specialty: {d.specialty}, Contact: {d.contact}" for d in doctors])
        messagebox.showinfo("Doctors", doctor_data)

    def view_appointments(self):
        appointments = self.cms.view_appointments()
        appointment_data = "\n".join([f"ID: {a.appointment_id}, Patient: {a.patient.name}, Doctor: {a.doctor.name}, Date: {a.date}, Time: {a.time}" for a in appointments])
        messagebox.showinfo("Appointments", appointment_data)

if __name__ == "__main__":
    root = tk.Tk()
    cms = ClinicManagementSystem()
    app = ClinicApp(root, cms)
    root.mainloop()
