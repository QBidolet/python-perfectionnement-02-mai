import requests
from lxml import etree

url = "http://httpbin.org/xml"

result = requests.get(url)

doc = etree.fromstring(result.content)
print(doc.tag)

# Accéder à la valeur d'un attribut
print(doc.attrib["title"])

# Utiliser les requêtes
for element in doc.findall('.//item'):
    print(element.tag)

print(doc.tag)

slide_count = len(doc.findall("slide"))
print(slide_count)

new_slide = etree.SubElement(doc, "slide")
new_slide.text = "C'est un nouveau slide."

slide_count = len(doc.findall("slide"))
print(slide_count)