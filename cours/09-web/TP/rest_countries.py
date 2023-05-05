import requests
import json


def get_data_country_by_name(country_name):
    """
    Api restcountries.
    Get et affiche les informations d'un pays à partir du nom.
    :param country_name: Nom du pays en anglais en string.
    """
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    result = requests.get(url)
    obj_text = result.text
    country = json.loads(obj_text)
    print_country(country)


def print_country(country):
    """
    Extrait les informations de la liste de la liste de pays
    et les affiches à l'utilisateur.
    :param countries: Liste de pays de l'API restcountries
    """
    pays = country[0]

    # Affichage
    for value in pays.values():
        print(value)


if __name__ == '__main__':
    country_name = input("Entrez le nom d'un pays pour obtenir des informations.\n")
    get_data_country_by_name(country_name)
