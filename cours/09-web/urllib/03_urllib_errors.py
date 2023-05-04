import urllib.request
from urllib.error import URLError, HTTPError

url = "http://cette_url_nexiste_pas.org"

try:
    result = urllib.request.urlopen(url)
except HTTPError as e:
    print(e)
    print(e.code)
except URLError as e:
    print(e)
    print(e.reason)