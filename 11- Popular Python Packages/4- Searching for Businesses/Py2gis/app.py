import requests
import config

url = "https://catalog.api.2gis.com/3.0/items"

params = {
    "q": "бар",
    "key": config.api_key
}

response = requests.get(
    url=url, params=params)

result = response.json()
print(result)
