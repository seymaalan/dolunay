import requests

r = requests.get("http://api.open-notify.org/astros.json")

print(r.status_code)
print(r.json())
import json
def jprint(obj):
    #create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(r.json())