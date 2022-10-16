import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "coffee",
    "location": "Palo Alto"
}
response = requests.get(url=url, headers=headers, params=params)
result = response.json()
businesses = result["businesses"]

names = [b["name"] for b in businesses if b["rating"] > 4.0]
for name in names:
    print(name)
