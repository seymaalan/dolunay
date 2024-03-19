import json
import requests
import csv

def fetch_events(city_name):
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?countryCode=TR&apikey=Gkcd7sqQAXwAZPuGDyVCIFB4yD0hIwn9&city={city_name}"
    response = requests.get(url)
    if response.status_code == 200:
        events_data = response.json().get("_embedded", {}).get("events", [])
        filtered_events = []
        for event in events_data:
            filtered_event = {
                "event_name": event.get("name", ""),
                "genre": event.get("classifications", [{}])[0].get("genre", {}).get("name", ""),
                "segment": event.get("classifications", [{}])[0].get("segment", {}).get("name", ""),
                "address": event.get("_embedded", {}).get("venues", [{}])[0].get("address", {}).get("line1", ""),
                "city": event.get("_embedded", {}).get("venues", [{}])[0].get("city", {}).get("name", ""),
                "localdate": event.get("dates", {}).get("start", {}).get("localDate", ""),
                "localtime": event.get("dates", {}).get("start", {}).get("localTime", ""),
                "url": event.get("url", "")
            }
            filtered_events.append(filtered_event)
        return filtered_events
    else:
        print("Error:", response.status_code)
        return []

def convert_to_csv(events, csv_path):
    if not events:
        print("No events to convert.")
        return
    
    # Header names for the CSV file
    fieldnames = ["event_name", "genre", "segment", "address", "city", "localdate", "localtime", "url"]
    
    # Writing the data to CSV file
    with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Writing the header
        writer.writeheader()
        
        # Writing each event's data
        for event in events:
            writer.writerow({
                "event_name": event.get("event_name", ""),
                "genre": event.get("genre", ""),
                "segment": event.get("segment", ""),
                "address": event.get("address", ""),
                "city": event.get("city", ""),
                "localdate": event.get("localdate", ""),
                "localtime": event.get("localtime", ""),
                "url": event.get("url", "")
            })
    
    print("Conversion to CSV completed. File saved at:", csv_path)

# Kullanımı:
city_name = input("Enter the name of the city in Turkey: ")
events = fetch_events(city_name)
if events:
    convert_to_csv(events, "events.csv")
else:
    print("No events found.")


