import re

class ValidAttributeNames(type):
    def __new__(cls, name, bases, dct):
        for attr_name in dct:
            if not re.match(r'^[a-z_][a-zA-Z0-9_]*$', attr_name):
                raise ValueError(f"Attribut invalide : '{attr_name}', les attributs doivent commencer"
                                 f"par une lettre minuscule et ne pas contenir de caractère spéciaux.")
                return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=ValidAttributeNames):
    valid_attribute = 42
    # Invalide = "Test" # Attribut invalide.
    _private = "secret"