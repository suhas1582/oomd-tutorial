import uuid
from models.healthcareManager import HealthcareManager

class Lab(HealthcareManager):

    def __init__(self, name, address, phone, tests_offered):
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.phone = phone
        self.tests_offered = tests_offered


    def generate_reports(self, test_id, report_file):
        pass