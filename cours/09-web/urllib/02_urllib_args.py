import urllib.parse, urllib.request

url = "http://httpbin.org/get"

args = {
    "name": "Françoise Hardy",
    "is_author": True
}

# Pour envoyer des arguments, il faut commencer par les encoder.
data = urllib.parse.urlencode(args)

print(data)

result = urllib.request.urlopen(url + "?" + data)

print(result.read().decode())

# POST

url = "http://httpbin/org/post"
data = data.encode()
result = urllib.request.urlopen(url, data=data)

print(result.read().decode())