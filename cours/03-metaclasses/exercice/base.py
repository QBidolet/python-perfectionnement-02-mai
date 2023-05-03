import re

if not re.match(r'^[a-z_][a-zA-Z0-9_]*$', "Test"):
    print("La valeur n'est pas valide.")