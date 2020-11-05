# Http_requests_Headers3.py

import requests

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"Accept": "text/plain"})

data = response.json()

print(data["joke"])
print(f"status: {data['status']}") 

#print("\n")

#print(f"status: {data['status']}")

