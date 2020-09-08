# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
import requests

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
response = requests.get(url).content
data = pickle.loads(response)

for pair in data:
    print(''.join([i * j for i, j in pair]))
