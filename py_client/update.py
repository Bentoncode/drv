import requests

endpoint = "http://localhost:8000/api/product/1/update/"

data = {
    "title" : "My new with django ",
    "price": "00.00"
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())