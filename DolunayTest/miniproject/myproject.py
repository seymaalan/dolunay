import requests
import json
import csv

response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?countryCode=TR&city=Ankara&page=1&apikey=9xI7VEHC5OQbyGCt9GTtheNE9NKKVSD4")
jsonized_response = response.json()
last_response = jsonized_response["_embedded"]["events"]

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

csv_file_path = 'ankara_events.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['name', 'genre_name', 'segment_name', 'address', 'city', 'venue_name', 'local_date', 'local-time', 'url'])

    for json_data in last_response:
        name = json_data["name"]
        if "_embedded" in json_data and "attractions" in json_data["_embedded"]:
            attraction = json_data["_embedded"]["attractions"][0]
            if "name" in attraction:
                name = attraction["name"]
            if "classifications" in attraction:
                classification = attraction["classifications"][0]
                genre_name = classification["genre"]["name"] if "genre" in classification else ""
                segment_name = classification["segment"]["name"] if "segment" in classification else ""
        else:
            genre_name = segment_name = ""

        if "_embedded" in json_data and "venues" in json_data["_embedded"]:
            venue = json_data["_embedded"]["venues"][0]
            address = venue["address"].get("line1", "") if "address" in venue else ""
            city = venue["city"]["name"] if "city" in venue else ""
            venue_name = venue["name"] if "name" in venue else ""
        else:
            address = city = venue_name = ""

        if "dates" in json_data and "start" in json_data["dates"]:
            local_date = json_data["dates"]["start"].get("localDate", "")
            local_time = json_data["dates"]["start"].get("localTime", "")
        else:
            local_date = local_time = ""

        url = json_data.get("url", "")

        csv_writer.writerow([name, genre_name, segment_name, address, city, venue_name, local_date, local_time, url])

print(f"CSV dosyası '{csv_file_path}' başarıyla oluşturuldu.")
