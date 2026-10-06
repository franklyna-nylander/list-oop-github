# Patient class
class Patient:
    def __init__(self, patient_name, patient_id, age, gender, diagnosis):
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print("\n **********Patient Information**********")  
        print(f"ID: {self.patient_name}")  
        print(f"Name: {self.patient_id}")  
        print(f"Age: {self.gender}")  
        print(f"Gender: {self.gender}")  
        print(f"Diagnosis: {self.diagnosis}")

# Hospital Class
class Hospital:    
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.patients = []

    def add_patient(self,patient):
        self.patients.append(patient)
        print("Patient Added Successfully")

    def display_patients(self):
        print("\n ********** All Patients **********")
        print(f"\n ********** {self.hospital_name} **********")
        for patient in self.patients:
            if len(self.patients) == 0:
                print("No Patient Records Found")
            else:
                for patient in self.patients:
                    patient.display_info()   

patient1 = Patient(101, "Saidu", 23, "Male", "Poverty")
patient2 = Patient(102, "Saidu", 30, "Male", "Malaria")
patient3 = Patient(103, "Saidu", 21, "Female", "Headache")

#Hospital Object
hospital1 = Hospital("Donald Clinic")

# Add patient to the class using the add_patient method in the hospital class
hospital1.add_patient(patient1)
hospital1.add_patient(patient2)
hospital1.add_patient(patient3)

# Display all patient records in the hospital
hospital1.display_patients()


