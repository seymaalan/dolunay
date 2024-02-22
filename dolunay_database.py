import requests
import csv

def fetch_events(city_name):
    url = "https://app.ticketmaster.com/discovery/v2/events.json?countryCode=TR&apikey=2n2yRVtMTlYyMW0xOJXiLccxmLUIhIDA"
    api_key = "2n2yRVtMTlYyMW0xOJXiLccxmLUIhIDA"
    params = {
        "city": city_name,
        "apikey": api_key,  
    }
    response = requests.get(url, params=params)
    data = response.json()

    events_info = []
    for event in data.get("_embedded").get("events"):

        event_info = {
            "event_name": event.get("name"),
            "genre": event.get("classifications", [{}])[0].get("genre", {}).get("name"),
            "segment": event.get("classifications", [{}])[0].get("segment", {}).get("name"),
            "address": event.get("_embedded", {}).get("venues", [{}])[0].get("address", {}).get("line1"),
            "city": event.get("_embedded", {}).get("venues", [{}])[0].get("city", {}).get("name"),
            "localdate": event.get("dates", {}).get("start", {}).get("localDate"),
            "localtime": event.get("dates", {}).get("start", {}).get("localTime"),
            "url": event.get("url")
        }

        events_info.append(event_info)

    return events_info


def convert_to_csv(events, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'event_name', 'genre', 'segment', 'address', 'city', 'localdate', 'localtime', 'url'
        ])

        writer.writeheader()

        for event in events:
            writer.writerow(event)


city_name = "Istanbul"
events = fetch_events(city_name)

if events:
    file_path = 'events.csv'
    convert_to_csv(events, file_path)
    print(f'CSV dosyası "{file_path}" yoluna başarıyla kaydedildi.')
else:
    print("Etkinlik bulunamadı.")



