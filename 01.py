# http://www.pythonchallenge.com/pc/def/map.html

from bs4 import BeautifulSoup
import requests
from string import ascii_lowercase as letters


url = 'http://www.pythonchallenge.com/pc/def/map.html'
url_data = requests.get(url).text

soup = BeautifulSoup(url_data, 'html.parser')
quiz_data = soup.find('td')
quiz_table = quiz_data.get_text()
quiz = quiz_table.splitlines()[-1]

table = quiz.maketrans(letters, letters[2:] + letters[:2])
result = quiz.translate(table)

print(result)
print('map'.translate(table))