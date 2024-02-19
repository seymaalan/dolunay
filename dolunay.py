import requests

def fetch_events(city_name):

    api_key = "2byLKaUjeRNGlW40FmD9nI5IGZx4qUrG"
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}&city={city_name}&size=20"
    
 
    response = requests.get(url)
    
 
    if response.status_code == 200:
      
        json_response = response.json()
        

        events = []
        for event in json_response["_embedded"]["events"]:
            try:
                genre = event["classifications"][0]["genre"]["name"]
            except KeyError:
                genre = "Unknown"  
            try: 
            	segment=event["classifications"][0]["segment"]["name"]
            except KeyError:
                genre = "Unknown"  
            filtered_event = {
                "event_name": event["name"],
                "genre": genre,
                "segment": event["classifications"][0]["segment"]["name"],
                "address": event["_embedded"]["venues"][0]["address"],
                "city": event["_embedded"]["venues"][0]["city"]["name"],
                "local_date": event["dates"]["start"]["localDate"],
                "local_time": event["dates"]["start"]["localTime"],
                "url": event["url"]
            }
            events.append(filtered_event)
        
        return events
    else:
        print("İstek başarısız! HTTP kodu:", response.status_code)
        return None
city_name = "Ankara"  
veriler = fetch_events(city_name)



import csv

def convert_to_csv(data_list, csv_path):

    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:

        csv_writer = csv.writer(csv_file)
        

        csv_writer.writerow(['event_name', 'genre', 'segment', 'address', 'city', 'local_date', 'local_time', 'url'])
        

        for event in data_list:
            csv_writer.writerow([event['event_name'], event['genre'], event['segment'], event['address'], event['city'], event['local_date'], event['local_time'], event['url']])


csv_path = '/home/ecem/Desktop/csvfile/events.csv'


convert_to_csv(veriler, csv_path)

































