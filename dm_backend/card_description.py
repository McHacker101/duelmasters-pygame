import json

database = "test.json"
data = json.loads(open(database).read())

def search(name):
    info = (list(filter(lambda x: x['name'].lower() == name.lower(), data)))
    return info

