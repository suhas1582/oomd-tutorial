from datetime import datetime
import uuid

class Test:

    def __init__(self, name, ordered_by):
        self.id = str(uuid.uuid4())
        self.name = name
        self.ordered_by = ordered_by
        self.ordered_on = datetime.now()
        