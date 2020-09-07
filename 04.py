# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?'


class Solver:

    def __init__(self, cycles, link):
        self.cycles = cycles
        self.link = link
        self.nothing = 12345

    def get_stuff(self):
        for i in range(self.cycles):
            response = requests.get(self.link, params={'nothing': self.nothing})
            print('Request №', i)
            print('Nothing is:', self.nothing)
            print('Response is:', response.text)
            if response.text == 'Yes. Divide by two and keep going.':
                self.nothing = int(self.nothing) / 2
            else:
                self.nothing = response.text.split()[-1]


solve_it = Solver(400, url)
solve_it.get_stuff()
