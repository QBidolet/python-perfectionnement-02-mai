import json
import urllib.request

url = "https://swapi.dev/api/people/1"

# 1/ Ouvrir une URL et obtenir les données
result = urllib.request.urlopen(url)

# 2/ Afficher le code HTTP de la requête
print(f"Code HTTP {result.status}")

# 3/ Afficher le headers de la page
print("Headers\n")
print(result.headers)

# 4/ Afficher les données
print("#"*25)
print("Datas")
print("#"*25)
datas = result.read()
datas_str = datas.decode()
datas_json = json.loads(datas_str)

print(datas_json)
print(datas_json["name"])
print(datas_json["mass"])
print(datas_json["eye_color"])
