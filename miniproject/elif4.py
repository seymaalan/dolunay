import requests
import json



url = "https://app.ticketmaster.com/discovery/v2/events.json?size=20&countryCode=TR&dmaID=613&apikey=g6pKevuLGDIhUR5eudnnOiWtvpW6SeDf"

def fetch_events():
     city = str(input("Name a city from Türkiye: "))
     parameters = {
         "locale": "*",
         "city": city
    }
     global info
     info = []
     response = requests.get(url, parameters)

     if response.status_code==200:
         # jprint(response.json())
         x = 0
         while x<20:
             
             data = response.json()
             try:
              event_name = data["_embedded"]["events"][x]["name"]
              
             except KeyError:
                 event_name = "None" 

             try:
              genre_name = data["_embedded"]["events"][x]["classifications"][0]["genre"]["name"]
            
             except KeyError:
                genre_name = "None" 

             try:
              segment_name = data["_embedded"]["events"][x]["classifications"][0]["segment"]["name"]
              
             except KeyError:
                segment_name = "None" 

             try:
              address = data["_embedded"]["events"][x]["_embedded"]["venues"][0]["address"]["line1"]
              
             except KeyError:
                address = "None"

             try:
              city_name = data["_embedded"]["events"][x]["_embedded"]["venues"][0]["city"]["name"]
              
             except KeyError:
                city_name = "None"

             try:
              localdate = data["_embedded"]["events"][x]["dates"]["start"]["localDate"]
             
             except KeyError:
                localdate = "None"

             try:
              localtime = data["_embedded"]["events"][x]["dates"]["start"]["localTime"]
              
             except KeyError:
                localtime = "None"

             try:
              event_url = data["_embedded"]["events"][x]["url"]
              
             except KeyError:
                event_url = "None"

             list_of_events = [event_name,genre_name,segment_name,address,city_name,localdate,localtime,event_url]  
         

             x += 1
             info.append(list_of_events)
         print(info)     
         
     else:
          print("ERROR: " + response.status_code)   

     return info      
          
import csv

def convert_to_csv(info):
   file = open("events.csv", "w")
   writer = csv.writer(file)
   #info = fetch_events()
   headers = ["Event Name","Genre","Segment","Address","City","Local Date","Local Time","URL"]
   info2 = [headers] + info
   for row in info2:
      print(row)
      writer.writerow(row)
   file.close   
   return     
      
info = fetch_events()
convert_to_csv(info)


   