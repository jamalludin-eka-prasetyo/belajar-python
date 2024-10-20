import requests

url = 'https://reqres.in/api/users1'

response = requests.get(url)

print(response.status_code)