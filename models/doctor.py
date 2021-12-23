from .prescription import Prescription
from .test import Test
from .user import User
from .healthcareManager import HealthcareManager

import pickle
import os
import sys

data_file_path = os.path.join('data', 'doctors.bin')

sys.path.append('..')

from utils.fileOps import is_file_empty

class Doctor(User, HealthcareManager):

    def __init__(self, user, specialization, location):
        super().__init__(user.name, user.national_id, user.phone_no, user.dob, True, False)
        self.specialization = specialization
        self.location = location

    def add_prescription(self, user_id, medicines, directions):
        prescription = Prescription(medicines, directions, self)
        super(Doctor, Doctor).update_user_profile(user_id, prescriptions = prescription)

    def diagnose_patient(self, user_id):
        pass

    def order_tests(self, user_id, tests):
        ordered_tests = []
        for test in tests:
            ordered_test = Test(test, self)
            ordered_tests.append(ordered_test)
        super(Doctor, Doctor).update_user_profile(user_id, tests = ordered_tests)

    def save(self):
        doctors = []
        with open(data_file_path) as data_file:
            if not is_file_empty(data_file_path):
                doctors = pickle.load(data_file)
        
        doctors.append(self)
        with open(data_file_path, 'wb') as data_file:
            pickle.dump(doctors, data_file)
            
        return self

    # def update_my_profile(self, **kwargs):
    #     specialization = kwargs.pop('specialization')
    #     location = kwargs.pop('location')
    #     super().update_user_profile()

    @staticmethod
    def find_by_id(id):
        doctors = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                doctors = pickle.load(data_file)
        
        desired_doctor = None
        if doctors:
            desired_doctor = [doctor for doctor in doctors if doctor.national_id == id]
            desired_doctor = desired_doctor[0] if desired_doctor else None
        
        return desired_doctor
