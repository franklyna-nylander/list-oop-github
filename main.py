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

