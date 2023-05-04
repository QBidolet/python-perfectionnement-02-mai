import requests
from requests.auth import HTTPBasicAuth

url = "http://httpbin.org/basic-auth/NanaMouskouri/MySecretWord"

# 1/ Un objet credentials
credentials = HTTPBasicAuth('NanaMouskouri', 'MySecretWord')

# 2/ On appel l'url avec le credentials
result = requests.get(url, auth=credentials)
print(result.text)