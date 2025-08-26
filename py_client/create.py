import requests

endpoint = "http://localhost:8000/api/product/"

data = {
    "title":"August can still be your month believe in the Lord.",
    "price":"890.99", "content": " Sibongile like's to listento pastor Enigma"
    }

get_response = requests.post(endpoint, json=data)
print(get_response.json())
