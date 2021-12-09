from datetime import datetime
import uuid

class Prescription:

    def __init__(self, medicines, directions, diagnosed_by):
        self.id = str(uuid.uuid4())
        self.medicines = medicines if medicines else []
        self.directions = directions
        self.diagnosed_by = diagnosed_by
        self.prescribed_on = datetime.now()