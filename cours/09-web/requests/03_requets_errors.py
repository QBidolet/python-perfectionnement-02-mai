import requests
from requests import HTTPError, Timeout, ConnectionError

url = "http://cette_url_nexiste_pas.org"
# url = 'http://httpbin.org/delay/5'

try:
    result = requests.get(url, timeout=10)
except HTTPError as e:
    print(e)
except Timeout as e:
    print(e)
except ConnectionError as e:
    print(e)
