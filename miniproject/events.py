import requests

def fetch_events(city):
    
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "countryCode": "TR",
        "apikey": "RyH8X5Z5A3wa7UHDaCwNfBwfMzYhJ4rh",
        "city": city
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        events = data["_embedded"]["events"]

        formatted_events = []

        for event in events:
            try:
                name = event["name"]
            except KeyError:
                name = "None"
            
            try:
                genre = event["classifications"][0]["genre"]["name"]
            except KeyError:
                genre = "None"

            try:
                segment = event["classifications"][0]["segment"]["name"]
            except KeyError:
                segment = "None"

            try:
                address = event["_embedded"]["venues"][0]["address"]["line1"]
            except KeyError:
                address = "None"

            try:
                city = event["_embedded"]["venues"][0]["city"]["name"]
            except KeyError:
                city = "None"

            try:
                localdate = event["dates"]["start"]["localDate"]
            except KeyError:
                localdate = "None"

            try:
                localtime = event["dates"]["start"]["localTime"]
            except KeyError:
                localtime = "None"

            try:
                event_url = event["url"]
            except KeyError:
                event_url = "None"

            event_info = [name,genre,segment,address,city,localdate,localtime,event_url]

            formatted_events.append(event_info)

        return formatted_events
    
    else:
        print("Error:", response.status_code)
        return []
    

#print(fetch_events("Ankara"))


import csv

def convert_to_csv(json_data, csv_path):
    try:
        with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['event_name', 'genre', 'segment', 'address', 'city', 'localdate', 'localtime', 'url'])
            for event in json_data:
                writer.writerow(event)
                
        print(f"CSV dosyası başarıyla oluşturuldu: {csv_path}")

    except Exception as e:
        print("CSV'ye dönüştürme hatası:", e)


events = fetch_events("Ankara") 
convert_to_csv(events, "c:\\Users\\ASUS\\Desktop\\dolunay\\miniproject\\events.csv")


