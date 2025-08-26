import requests

headers = {
    "Authorization":"Bearer 8ad617609cdfa8d2bedb581320d604867f672474"
}
endpoint = "http://localhost:8000/api/product/"

data = {
    "title":"Testing out Token authentication",
    "price":"890.99", "content": "Using the post create method."
    }

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
