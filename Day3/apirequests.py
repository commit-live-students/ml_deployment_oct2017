import requests

url = "http://localhost:8080/hello/Manas"

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print response.text