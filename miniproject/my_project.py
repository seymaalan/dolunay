import requests
import json
#learning API
"""r = requests.get("http://api.open-notify.org/astros.json")

print(r.status_code)
print(r.json())
def jprint(obj):
    #create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(r.json())"""
"""parameters = {"lat":40.71, "lon": -74}
response = requests.get("http://api.open-notify.org/iss-now.json", params = parameters)
jprint(response.json())"""
"""iss_pass ={"message": "success","request": {"altitude": 100,"datetime": 1568062811,"latitude": 40.71,"longitude": -74.0,"passes": 5},"response": [{"duration": 395,"risetime": 1568082479},{"duration": 640,"risetime": 1568088118},{"duration": 614,"risetime": 1568093944},{"duration": 555,"risetime": 1568099831},{"duration": 595,"risetime": 1568105674}]}
pass_times = iss_pass["response"]
#print(pass_times)
risetimes = []
for d in pass_times:
    time = d["risetime"]
    risetimes.append(time)
#print(risetimes)
from datetime import datetime
times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)"""
# Begining to TicketMaster
#APIKey: Gkcd7sqQAXwAZPuGDyVCIFB4yD0hIwn9
def order(lis):
    s = set({})
    result = []
    for c in lis:
        s.add(c)
    a = s
    for i in a:
        result.append(i)
    return result

def are_dicts_equal(dict1, dict2):
    return sorted(dict1.items()) == sorted(dict2.items())

def fetch_events(City):
    r = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?countryCode=TR&apikey=Gkcd7sqQAXwAZPuGDyVCIFB4yD0hIwn9")
    data = r.json()
    events = data.get('_embedded', {}).get('events', [])
    result = []
    for event in events:
        a = (event.get('_embedded', {}).get('venues', []))[0]
        city = a.get('city').get('name')
        if city == City:
            valid = dict({})
            #name
            event_name = event.get('name')
            valid["event_name"] = event_name
            #genre
            e = (event.get('classifications'))[0]
            event_genre = e.get("genre", {}).get("name")
            valid["genre"] = event_genre
            #segment
            event_segment = e.get("segment").get("name")
            valid["segment"] = event_segment
            #address
            k = event.get("_embedded").get("venues")
            event_address = (k[0]).get("address", {}).get("line1", "No address")
            valid["address"] = event_address
            #city
            valid["city"] = City
            #localdate
            event_localdate = event.get("dates").get("start").get("localDate")
            valid["localdate"] = event_localdate
            #localtime
            event_localtime = event.get("dates").get("start").get("localTime")
            valid["localtime"] = event_localtime
            #URL
            event_url = event.get("url")
            valid["url"] = event_url
            result.append(valid)
    return result
import csv

def convert_to_csv(jsons, path):
    with open(path, "w", encoding="utf-8-sig") as csvfile:
        headers = ["event_name", "genre", "segment", "address", "city", "localdate", "localtime", "url"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for event in jsons:
            writer.writerow(event)

# Assuming fetch_events returns a list of dictionaries representing events
json_data = fetch_events("Mardin")

if json_data is not None:
    convert_to_csv(json_data, "C:\\Users\\glsm\\Dolunay\\dolunay\\miniproject\\events.csv")
else:
    print("Error: fetch_events returned None")