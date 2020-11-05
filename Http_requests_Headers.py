# Http_requests_Headers.py

import requests

response = requests.get(
    "http://www.example.com",
    headers = {
        "header1": "value1",
        "header2": "value2"
    }
)
print(response) #<Response [200]>