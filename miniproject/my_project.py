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
def fetch_events(City):
    r = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?countryCode=TR&apikey=Gkcd7sqQAXwAZPuGDyVCIFB4yD0hIwn9")
    data = r.json()
    events = data.get('_embedded', {}).get('events', [])
    result = {"events_in_city":[]}
    t = []
    for event in events:
        a = (event.get('_embedded', {}).get('venues', []))[0]
        city = a.get('city').get('name')
        if city == City:
            valid = dict({})
            #name
            event_name = event.get('name')
            valid["name"] = event_name
            #genre
            e = (event.get('classifications'))[0]
            event_genre = e.get("genre").get("name")
            valid["genre"] = event_genre
            t.append(valid)
    result["events_in_city"] = t
    print(result)


fetch_events("İzmir")