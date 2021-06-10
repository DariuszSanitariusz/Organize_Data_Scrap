from scrap_data import ScrapData
from personal_data import PersonalData
from list_of_records import ListOfRecords
from create_additional_data import CreateAdditionalData
from some_sort import SomeSort
from create_csv import CreateCsv

"""
scrap data from url
"""
scrapped_data = ScrapData()
scrapped_data.get_list()
scrapped_data.handle_disambiguation()
scrapped_data.extract_info()

"""
creating space for record objects
"""
rec_list = ListOfRecords()
rec_list.set_size(len(scrapped_data))

for i, person in enumerate(scrapped_data.extracted_data):
    """
    saving scrapped data and adding created info
    """
    rec_list.list_of_records[i] = PersonalData()
    rec_list.list_of_records[i].create_record_from_scrapped_data(person)

    add_data = CreateAdditionalData()
    add_data.create_url(person[0], person[1])
    add_data.create_id()
    add_data.create_mail(person[0])

    rec_list.list_of_records[i].write_additional_data(add_data.get_attr())

"""
sorting records by id's
"""
rec_list.get_records_ids()
sort_type = SomeSort(rec_list.records_ids)
rec_list.sort_records(sort_type.bubble_sort())

"""
writing csv file
"""

wiki_csv = CreateCsv('wiki')

wiki_csv.open_file()
wiki_csv.index_line()

for record in rec_list.list_of_records:
    wiki_csv.add_line(record.list_info())

wiki_csv.close_file()



