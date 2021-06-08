class PersonalData:

    def __init__(self):

        self.name = None
        self.date_of_birth = None
        self.date_of_death = '-'
        self.description = None
        self.id = None
        self.mail = None
        self.url = None

        self.list_of_records = []

    def create_record_from_scrapped_data(self, *args):
        for name, prof, date, description in args:
            self.name = name
            self.date_of_birth = date[0]
            if len(date) == 2:
                self.date_of_death = date[1]
            self.description = description

    def write_additional_data(self, *args):
        for id, mail, url in args:
            self.id = id
            self.mail = mail
            self.url = url

    def add_record_to_list(self, record):
        self.list_of_records.append(record)

    def sort_records(self, sort_type):
        sort_type(self.list_of_records)
