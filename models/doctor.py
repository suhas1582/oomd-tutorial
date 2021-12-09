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

class Doctor(HealthcareManager):

    def __init__(self, user, specialization, location):
        self.user = user
        self.specialization = specialization
        self.location = location

    def add_prescription(self, user_id, medicines, directions):
        prescription = Prescription(medicines, directions, self)
        super(Doctor, Doctor).update_user_profile(user_id, {'prescriptions': [prescription]})

    def diagnose_patient(self, user_id):
        pass

    def order_tests(self, user_id, tests):
        ordered_tests = []
        for test in tests:
            ordered_test = Test(test, self)
            ordered_tests.append(ordered_test)
        super(Doctor, Doctor).update_user_profile(user_id, {'tests': ordered_tests})

    def save(self):
        doctors = []
        with open(data_file_path) as data_file:
            if not is_file_empty(data_file_path):
                doctors = pickle.load(data_file)
        
        doctors.append(self)
        with open(data_file_path, 'wb') as data_file:
            pickle.dump(doctors, data_file)
            
        return self
