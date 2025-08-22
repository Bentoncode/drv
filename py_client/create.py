import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    "title":"They most redirect them to my email .",
    "price":"20.09"
    }

get_response = requests.post(endpoint, json=data)
print(get_response.json())
