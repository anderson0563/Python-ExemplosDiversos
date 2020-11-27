import requests

url = 'http://jsonplaceholder.typicode.com/todos'
params = {'limit': 16, 'country': 'us', 'apikey': 'API-KEY'}

response = requests.get(url, params=params)
print(response.json())