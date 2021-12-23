from datetime import datetime

class Report:

    def __init__(self, id, test_id, test_results, report_file, test_performed_by):
        self.id = id
        self.test_id = test_id
        self.test_results = test_results
        self.report_file = report_file if report_file else None
        self.test_performed_by = test_performed_by
        self.test_done_on = datetime.now()