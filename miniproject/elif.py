import requests
import json
response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?size=1&apikey=g6pKevuLGDIhUR5eudnnOiWtvpW6SeDf")
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())  
def fetch_events():
      