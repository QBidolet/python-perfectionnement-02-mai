# 1/ Syntaxe
class SimpleMeta(type):
    def __new__(meta, name, bases, dct):
        return super().__new__(meta, name, bases, dct)


class MyClass(metaclass=SimpleMeta):
    pass


# 2/ Créer une métaclasse pour modifier le typage des attributs.

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
class TypedMeta(type):
    def __new__(cls, name, bases, dct):
        typed_attributes = {
            key: value for key, value in dct.items()
            if isinstance(value, type)
        }
        print(typed_attributes)
        for key, value in typed_attributes.items():
            dct.pop(key)
        dct['_typed_attributes'] = typed_attributes
        return super().__new__(cls, name, bases, dct)

    def __setattr__(cls, name, value):
        # Bout de code pour retrouver le type initial de l'attribut
        if name in cls._typed_attributes:
            attr_type = cls._typed_attributes[name]

            # si le type de la nouvelle valeur (value) ne correspond pas
            if not isinstance(value, attr_type):
                # on lève une exception pour bloquer l'attribution de la nouvelle valeur
                raise TypeError(f"Type incorrect pour l'attribut {name} : attendu {attr_type}, obtenu {type(value)}")
        super().__setattr__(name, value)


class TypeCheckingClass(metaclass=TypedMeta):
    nombre = 42
    chaine = "Hello"


obj = TypeCheckingClass()
obj.nombre = 13  # valeur OK
obj.nombre = "Un str."  # Lève une exception TypeError
