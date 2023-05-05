import xml.sax
import requests


class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slide_count = 0
        self.item_count = 0
        self.is_in_title = False

    def startElement(self, name, attrs):
        if name == "slideshow":
            print("Slideshow title : " + attrs['title'])
            print("Slideshow date : " + attrs['date'])
            print("Slideshow author : " + attrs['author'])
        elif name == "item":
            self.item_count += 1
        elif name == "slide":
            self.slide_count += 1
        elif name == "title":
            self.is_in_title = True

    def endElement(self, name):
        if name == "title":
            self.is_in_title = False

    def characters(self, content):
        if self.is_in_title:
            print("Title : " + content)

    def startDocument(self):
        print("On est en début de document (Avant la lecture)")

    def endDocument(self):
        print("On est en fin de document (Lecture terminé).")


if __name__ == '__main__':
    url = "http://httpbin.org/xml"

    handler = MyContentHandler()
    result = requests.get(url)

    # on appelle parseString de sax, et on lui passe le handler pour traduire.
    xml.sax.parseString(result.text, handler)
    # print(result.text)
    print(handler.slide_count)
    print(handler.item_count)
