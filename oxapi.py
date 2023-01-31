import  requests
import json
from pprint import pprint
# TODO: replace with your own app_id and app_key
app_id = '79fb63e1'
app_key = '200cfb65f2e575f473f71f8da22db306'
language = 'en-gb'
word_id = 'apple'
url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'  + language + '/'  + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
pprint("code {}\n".format(r.status_code))
pprint("text \n" + r.text)
pprint("json \n" + json.dumps(r.json()))
