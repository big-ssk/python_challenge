from pprint import pprint
from bs4 import BeautifulSoup, Comment
from collections import defaultdict
import requests

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
url_data = requests.get(url).text

soup = BeautifulSoup(url_data, 'html.parser')
quiz_data = soup.find_all(text=lambda text: isinstance(text, Comment))[-1]
quiz = quiz_data.strip()


result = defaultdict(int)
for i in quiz:
    result[i] += 1

pprint(sorted(result.items(), key=lambda x: x[1]))
