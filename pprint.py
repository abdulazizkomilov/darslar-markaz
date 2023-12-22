from pprint import pprint
import json
import requests

# filename = "bemor.json"
# with open(filename) as f:
#     bemor = json.load(f)

# print(bemor)
# pprint(bemor)

import requests
from pprint import pprint
r = requests.get("https://api.github.com")
# print(r.json())
pprint(r.json())


page = 'https://kun.uz/news/main'
r = requests.get(page)
# print(r.text)
pprint(r.text)

