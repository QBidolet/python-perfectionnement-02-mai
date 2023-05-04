import requests

# 1/ Utiliser requests pour une requête HTTP simple.
url = "https://swapi.dev/api/people/1/"
result = requests.get(url)
print(result)

# 2/ Envoyer des paramètres avec GET
datas = {"key1": "value1", "key2": "value2"}
url = "http://httpbin.org/get"
result = requests.get(url, params=datas)
print(result.text)

# 3/ Envoyer des paramètres avec POST
url = "http://httpbin.org/post"
result = requests.post(url, data=datas)
print(result.text)
