import requests

r = requests.get("http://api.open-notify.org/astros.json")

print(r.status_code)
print(r.json())