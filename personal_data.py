class PersonalData:

    def __init__(self):

        self.name = None
        self.date_of_birth = None
        self.date_of_death = '-'
        self.description = None
        self.id = None
        self.mail = None
        self.url = None

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

    def list_info(self):
        # date = str(self.date_of_birth)+','+str(self.date_of_death)
        # s_id = str(self.id)
        # str_info = s_id+','+self.name+','+date+','+self.mail+','+self.description+','+self.url
        l_info = [self.id, self.name, self.date_of_birth, self.date_of_death, self.mail, self.description, self.url]
        return l_info
