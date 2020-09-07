# http://www.pythonchallenge.com/pc/def/equality.html

from bs4 import BeautifulSoup, Comment
import requests
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'
url_data = requests.get(url).text

soup = BeautifulSoup(url_data, 'html.parser')
quiz_data = soup.find_all(text=lambda text: isinstance(text, Comment))[-1]
quiz = quiz_data.strip()

pattern = '[a-z][A-Z]{3}([a-z]){1}[A-Z]{3}[a-z]'
result = ''.join(re.findall(pattern, quiz))

print(result)
