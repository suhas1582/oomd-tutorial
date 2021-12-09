import pickle
import os
import sys
import hashlib

from flask_login import UserMixin

from .userProfile import UserProfile
# from models import userProfile

# /Users/suhas/Downloads/oomd/data
data_file_path = os.path.join('data', 'users.bin')

sys.path.append('..')

from utils.fileOps import is_file_empty


class User(UserMixin):

    def __init__(self, name, national_id, phone_no, dob, is_doctor, is_admin):
        self.name = name
        self.national_id = national_id
        self.phone_no = phone_no
        self.dob = dob
        self.is_doctor = is_doctor
        self.is_admin = is_admin

    def save(self):
        users = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                users = pickle.load(data_file)
        # TODO: Prevent appending of the users with same national Id
        users.append(self)
        with open(data_file_path, 'wb') as data_file:
            pickle.dump(users, data_file)
        
        user_profile = UserProfile(self)
        user_profile.save_profile()
        
        return user_profile

    @staticmethod
    def login(id, dob):
        desired_user = User.find_by_id(id)
        if desired_user:
            if dob == desired_user.dob:
                hashed_key = hashlib.sha256(id.encode())
                print(hashed_key.hexdigest())
                return {'auth_key': hashed_key.hexdigest()}
            else:
                return {'error': 'Entered DOB is not correct! Please check the entered value'}
        else:
            return {'error': 'Entered ID does not exist in the system! Plaese retry with another ID'}

    @staticmethod
    def find_by_id(id):
        users = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                users = pickle.load(data_file)
                # print(users)
        desired_user = None
        if users:
            desired_user = [user for user in users if user.national_id == id]
            desired_user = desired_user[0] if desired_user else None
        
        return desired_user

    @staticmethod
    def update_user_details(user_id, **kwargs):
        users = []
        with open(data_file_path, 'rb') as data_file:
            if not is_file_empty(data_file_path):
                users = pickle.load(data_file)
        desired_user = list(filter(lambda user: user.national_id == user_id, users))
        desired_user = desired_user[0]
        # print('line 79', desired_user[0])
        unchanged_user_list = list(filter(lambda user: user.national_id != user_id, users))

        print(kwargs)

        for key, value in kwargs.items():
            setattr(desired_user, key, value)
        unchanged_user_list.append(desired_user)
        with open(data_file_path, 'wb') as data_file:
            pickle.dump(unchanged_user_list, data_file)
        UserProfile.update_profile_details(user_id, desired_user)


    def get_id(self): # overridden method from UserMixin
        return self.national_id