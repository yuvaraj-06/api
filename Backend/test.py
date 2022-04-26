import requests

url = "http://127.0.0.1:5000/data?email=y&password=a"

payload={}
headers = {}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
