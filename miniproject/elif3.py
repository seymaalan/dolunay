import requests
import json
from jprint import jprint


url = "https://app.ticketmaster.com/discovery/v2/events.json?size=20&countryCode=TR&dmaID=613&apikey=g6pKevuLGDIhUR5eudnnOiWtvpW6SeDf"

def fetch_events():
     city = str(input("Name a city from Türkiye: "))
     parameters = {
         "locale": "*",
         "city": city
    }
     
     response = requests.get(url, parameters)

     if response.status_code==200:
         # jprint(response.json())
         x = 0
         while x<20:
             
             data = response.json()
             try:
              event_name = data["_embedded"]["events"][x]["name"]
              print("Name: " +event_name)
             except KeyError:
                 print("Name: None") 

             try:
              genre_name = data["_embedded"]["events"][x]["classifications"][0]["genre"]["name"]
              print("Genre: " +genre_name)
             except KeyError:
                print("Genre: None") 

             try:
              segment_name = data["_embedded"]["events"][x]["classifications"][0]["segment"]["name"]
              print("Segment: " +segment_name)
             except KeyError:
                print("Segment: None") 

             try:
              address = data["_embedded"]["events"][x]["_embedded"]["venues"][0]["address"]["line1"]
              print("Address: " +address)
             except KeyError:
                print("Address: None")

             try:
              city_name = data["_embedded"]["events"][x]["_embedded"]["venues"][0]["city"]["name"]
              print("City: " +city_name)
             except KeyError:
                print("City: None")

             try:
              localdate = data["_embedded"]["events"][x]["dates"]["start"]["localDate"]
              print("Local Date: " +localdate)
             except KeyError:
                print("Local Date: None")

             try:
              localtime = data["_embedded"]["events"][x]["dates"]["start"]["localTime"]
              print("Local Time: " +localtime)
             except KeyError:
                print("Local Time: None")

             try:
              event_url = data["_embedded"]["events"][x]["url"]
              print("URL: " +event_url)
             except KeyError:
                print("URL: None")
             
             x += 1


     else:
          print("ERROR: " + response.status_code)     

fetch_events()