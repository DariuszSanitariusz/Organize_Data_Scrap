import requests
import random


class CreateAdditionalData:

    domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'msn.com', 'live.com', 'mac.com']

    def __init__(self):
        self.id = None
        self.mail = None
        self.url = None

    def create_url(self, name, prof):
        name = name.replace(' ', '_')
        if prof == 'not_included':
            self.url = 'https://en.wikipedia.org/wiki/{}'.format(name)
        else:
            target = name + prof
            self.url = 'https://en.wikipedia.org/wiki/{}'.format(target)

    def create_id(self, name, prof):
        res = requests.get(self.url)
        self.id = int(res.elapsed.total_seconds()*10**5)+random.randint(10**3, 10**5)

    def create_mail(self, name):
        name = name.replace(' ', '_')
        self.mail = name + str(random.randint(11, 99)) + '@' + random.choice(self.domain)

    def __str__(self):
        return self.id, self.mail, self.url
