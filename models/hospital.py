from os import name
from models.healthcareManager import HealthcareManager

class Hospital(HealthcareManager):

    def __init__(self, name, address, phone_no, specialities, doctors_employed):
        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.spcialities = specialities
        self.doctors_employed = doctors_employed
    
    def admit_patient(self, patient):
        pass

    def discharge_patient(self, patient):
        pass