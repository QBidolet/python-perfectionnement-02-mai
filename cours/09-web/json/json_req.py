import requests

url = "https://swapi.dev/api/people/1"
result = requests.get(url)

obj_json = result.json()

print(obj_json)
print(obj_json['name'])

