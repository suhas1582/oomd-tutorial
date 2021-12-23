from models.userProfile import UserProfile
import pickle
import os
import sys
# /Users/suhas/Downloads/oomd/data
data_file_path = os.path.join('data', 'user_profiles.bin')

sys.path.append('..')
print(data_file_path)

from utils.fileOps import is_file_empty

class HealthcareManager:

    @staticmethod
    def update_user_profile(id, **kwargs):
        user_profiles = UserProfile.get_all_users()
        if user_profiles:
            required_profile = list(filter(lambda user_profile: user_profile.id == id, user_profiles))[0]
            unchanged_profile_list = list(filter(lambda user_profile: user_profile.id != id, user_profiles))
            prescriptions = kwargs.pop('prescriptions', None)
            tests = kwargs.pop('tests', None)
            test_reports = kwargs.pop('test_reports', None)
            if prescriptions:
                required_profile.prescriptions.append(prescriptions)
            if tests:
                required_profile.tests.extend(tests)
            if test_reports:
                required_profile.tests.append(test_reports)
            unchanged_profile_list.append(required_profile)
            with open(data_file_path, 'wb') as data_file:
                pickle.dump(unchanged_profile_list, data_file)

    @staticmethod
    def perform_test(id, test_id):
        pass