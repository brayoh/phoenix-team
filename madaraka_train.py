import json
from pprint import pprint


with open('db.json') as data_file:
    data = json.load(data_file)


pprint(data['trains'])
# data_file.write(json.dumps(data))


with open('db.json', 'w') as data_file:
    json.dumps(data)
