from personal_data import PersonalData


class ListOfRecords:

    def __init__(self):
        self.list_of_records = []
        self.records_ids = []

    def set_size(self, size):
        self.list_of_records = [None] * size

    def add_record_to_list(self, record):
        self.list_of_records.append(record)

    def get_records_ids(self):
        for record in self.list_of_records:
            self.records_ids.append(record.id)

    def sort_records(self, sorted_ids):
        for i, r_id in enumerate(sorted_ids):
            for n, record in enumerate(self.list_of_records):
                if r_id == record.id:
                    swap = self.list_of_records.pop(n)
                    self.list_of_records.insert(i, swap)
                    break
