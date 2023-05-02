# 1/ Syntaxe
class SimpleMeta(type):
    def __new__(meta, name, bases, dct):
        return super().__new__(meta, name, bases, dct)

class MyClass(metaclass=SimpleMeta):
    pass

# 2/ Créer une métaclasse pour modifier le typage.

class TypedMeta(type):
    def __new__(meta, name, bases, dct):
        # Ajouter des annotations de type pour les attributs
        for attr_name, attr_value in dct.items():
            if not callable(attr_value) and not attr_name.startswith("__"):
                dct[attr_name] = (attr_value, type(attr_value))

        return super().__new__(meta, name, bases, dct)

class TypedClass(metaclass=TypedMeta):
    nombre = 42
    chaine = "Hello World!"

typed_class = TypedClass()
print(typed_class.nombre, type(typed_class.nombre))

# 3/ Créer une métaclasse pour vérifier les types
class TypeCheckingMeta(TypedMeta):
    def __setattr__(cls, name, value):
        if name in cls.__dict__:
            attr_type = cls.__dict__[name][1]
            if not isinstance(value, attr_type):
                raise TypeError(f"Type incorrect pour l'attribut {name} : attendu {attr_type}, obtenu {type(value)}")
        super().__setattr__(name, value)

class TypeCheckingClass(metaclass=TypeCheckingMeta):
    nombre = 42
    chaine = "Hello world!"

obj = TypeCheckingClass()
obj.nombre = 13 # valeur OK
obj.nombre = "Un str."
