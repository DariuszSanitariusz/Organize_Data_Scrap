import csv


class CreateCsv:
    def __init__(self, file_name):
        self.file_name = file_name
        self.wiki_data_csv = None

    def open_file(self):
        self.wiki_data_csv = open(self.file_name, mode='w', encoding='UTF-8',newline='')

    def index_line(self):
        wiki_data_writer = csv.writer(self.wiki_data_csv, delimiter=',')
        wiki_data_writer.writerow(['id', 'name', 'birth_year', 'death_year', 'mail', 'description', 'url'])

    def add_line(self, row):
        wiki_data_writer = csv.writer(self.wiki_data_csv, delimiter=',')
        wiki_data_writer.writerow(row)

    def close_file(self):
        self.wiki_data_csv.close()
