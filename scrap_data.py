import requests
import bs4
import re


class ScrapData:

    def __init__(self):
        self.people_list = set()
        self.disambiguation_list = []
        self.extracted_data = []

    def get_list(self):
        res = requests.get('https://en.wikipedia.org/wiki/Dickerson_(surname)')
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        first_item = soup.select('.mw-parser-output')[0]
        whole_text = first_item.text

        list_of_lines = whole_text.split('\n')
        self.people_list.update(list_of_lines[2:-7])

    def handle_disambiguation(self):
        """
        1. Find disambiguation
        2. Get name part for url
        3. Add missing people
        """
        dis_list = self.disambiguation_list
        p_list = self.people_list
        for i, line in reversed(list(enumerate(p_list))):
            if 'disambiguation' in line:
                dis_list.append(line)
                p_list.remove(line)

        for i, line in enumerate(dis_list):
            name_end_marker = re.search(r'\W\W\W', line)
            name = line[0:name_end_marker.start() + 1]
            dis_list[i] = name

        for many_people in dis_list:
            many_people = many_people.replace(' ', '_')

            res = requests.get('https://en.wikipedia.org/wiki/{}'.format(many_people))
            soup = bs4.BeautifulSoup(res.text, 'lxml')

            names = soup.select('.mw-parser-output')[0]
            names = names.text.split('\n')[2:-9]

            self.people_list.update([x for x in names if x])

    def extract_info(self):
        """
        using regex gather info and save it as a tuple
        """
        for person in self.people_list:
            dates = []
            prof = 'not_included'

            if not re.search(r'[(]', person):
                person = person.split(',')
                name = person[0]
                description = person[1][1:]
                continue
            for date_match in re.finditer(r'\d\d\d\d', person):
                dates.append(date_match.group())

            name_match = re.search(r'\s[(]', person)
            name = person[0:name_match.start()]

            desc_match = re.search(r'[),]', person)
            description = person[desc_match.end()+1:]

            prof_match = re.search(r'[(][a-zA-Z]+[)]', person)
            if prof_match:
                prof = prof_match.group()

            self.extracted_data.append((name, prof, dates, description))
