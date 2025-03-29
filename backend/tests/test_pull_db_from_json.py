import json
from config import jwt
import requests

url = "http://127.0.0.1:8080/events/pull/from/json"


headers = {
    'Authorization': f'Bearer {jwt}'
}
with open("../parser/parsed_data.json") as f:
    data = json.load(f)
    for item in data:
        response = requests.post(url, headers=headers, json=item)

print(f"Status Code: {response.status_code}")
print(response)
