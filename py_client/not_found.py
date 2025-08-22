import requests

endpoint = "http://localhost:8000/api/product/74746/"

get_response = requests.get(endpoint)
print(get_response.json())