# from models import user
# from .report import Report
# from .test import Test
# from .prescription import Prescription

import pickle
import os
import sys
# /Users/suhas/Downloads/oomd/data
data_file_path = os.path.join('data', 'user_profiles.bin')

sys.path.append('..')
print(data_file_path)

from utils.fileOps import is_file_empty

class UserProfile:

    def __init__(self, user):
        self.id = user.national_id
        self.name = user.name
        self.phone_no = user.phone_no
        self.dob = user.dob
        self.prescriptions = []
        self.tests = []
        self.test_reports = []

    def save_profile(self):
        user_profiles = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                user_profiles = pickle.load(data_file)
                print(user_profiles)
        user_profiles.append(self)
        with open(data_file_path, 'wb') as data_file:
            # TODO: Prevent appending of the user profiles with same national Id
            pickle.dump(user_profiles, data_file)

        return self

    @staticmethod
    def find_user_by_id(user_id):
        user_profiles = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                user_profiles = pickle.load(data_file)
        if user_profiles:
            desired_profile = [user_profile for user_profile in user_profiles if user_profile.id == user_id]
            desired_profile = desired_profile[0] if desired_profile else None

            return desired_profile

        return None

    @staticmethod
    def get_all_users():
        user_profiles = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                user_profiles = pickle.load(data_file)
                
        return user_profiles

    def find_prescription_by_id(self, prescription_id):
        pass

    def find_test_by_id(self, test_id):
        pass

    def find_report_by_id(self, report_id):
        pass

    @staticmethod
    def update_profile_details(user_id, new_user):
        user_profiles = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                user_profiles = pickle.load(data_file)
        desired_user_profile = list(filter(lambda user_profile: user_profile.id == user_id, user_profiles))[0]
        # desired_user_profile = desired_user_profile[0]
        # print(desired_user_profile[0])
        unchanged_user_profile_list = list(filter(lambda user_profile: user_profile.id != user_id, user_profiles))

        setattr(desired_user_profile, 'id', new_user.national_id)
        setattr(desired_user_profile, 'name', new_user.name)
        setattr(desired_user_profile, 'phone_no', new_user.phone_no)
        setattr(desired_user_profile, 'dob', new_user.dob)

        unchanged_user_profile_list.append(desired_user_profile)
        with open(data_file_path, 'wb') as data_file:
            pickle.dump(unchanged_user_profile_list, data_file)

    def get_profile_info(self):
        pass


        