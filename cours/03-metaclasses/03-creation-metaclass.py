def meta_method(self):
    return "meta_method"

class MyMeta(type):

    def __new__(cls, name, bases, dct):
        # print(dir(dct))
        print(f"Création de la classe {name} avec la métaclasse MyMeta.")
        dct["meta_attribute"] = "Attribut attribué automatiquement par la métaclasse MyMeta."
        dct["meta_attribute"] = "Attribut attribué automatiquement par la métaclasse MyMeta."
        return super().__new__(cls, name, bases, dct)


    def __init__(cls, name, bases, dct):
        print(f"Initialisation de la classe {name} avec la métaclasse MyMeta.")
        cls.meta_method = meta_method
        super().__init__(name, bases, dct)


class MyClass(metaclass=MyMeta):
    def my_method(self):
        return "Méthode de la classe MyClass"


my_instance = MyClass()
print(my_instance.meta_attribute)
print(my_instance.meta_method())
