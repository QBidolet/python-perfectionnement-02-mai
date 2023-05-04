"""
    Le fichier __init__.py est obligatoire pour que Python reconnaisse un dossier en tant que module.
    C'est un fichier spécial, il faut respecter le nom exacte.
    Il est exécuté quand le module est importé.
    Il peut être vide ou contenir du code d'initialisation et des importations.
"""

# exemple d'importation
from .mon_dossier import hello_world

# On peut aussi déclarer des constantes
CONSTANTE = 42

# C'est aussi le fichier où on initialise les configurations nécessaire
# pour la configuration de base de données, tous fichiers de configuration etc.