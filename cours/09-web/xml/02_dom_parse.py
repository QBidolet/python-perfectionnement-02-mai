import xml.dom.minidom
import requests

url = "http://httpbin.org/xml"

result = requests.get(url)

# Lecture du XML
dom_tree = xml.dom.minidom.parseString(result.text)
root_node = dom_tree.documentElement
print(root_node.nodeName)
print(root_node.getAttribute("title"))

items = dom_tree.getElementsByTagName("item")
print(items.length)
print(items[0].nodeName)

# Créer un objet item
new_item = dom_tree.createElement("item")
new_item.appendChild(dom_tree.createTextNode("Nouvel item ajouté depuis le code."))

# Ajouter du XML
first_slide = dom_tree.getElementsByTagName("slide")[0]
first_slide.appendChild(new_item)

items = dom_tree.getElementsByTagName("item")
print('#'*25)
for item in items:
    if item.hasChildNodes:
        print("Item :")
        for contenu in item.childNodes:
            print(contenu)