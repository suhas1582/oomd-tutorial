from .user import User

class Patient(User):
    def __init__(self, name, national_id, phone_no, dob, address):
        super().__init__(name, national_id, phone_no)
        self.dob = dob
        self._address = address