import types


class Base:
    def base_method(self):
        return "Méthode de la classe de base"


# Fonction qui sera ajoutée à la classe Base.
def dynamic_method(self):
    return "Méthode de la classe dynamique."


# Création d'une classe dynamique qui hérite de Base
DynamicClass = types.new_class("DynamicClass", (Base,), {})
print(type(DynamicClass))

# Ajouter la méthode dynamic_method à notre classe.
DynamicClass.dynamic_method = dynamic_method

# Instancier notre classe dynamique
dynamic_instance = DynamicClass()
print(type(dynamic_instance))

print(dynamic_instance.base_method())
print(dynamic_instance.dynamic_method())