# with pour la gestion des fichiers
with open("exemple.txt", "w") as f:
    f.write("Hello world!")
# fermeture automatique à la sortie du bloc

# Utilisation pour plusieurs ressources
with open("exemple.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        output_file.write(line)

# Exemple : fichiers temporaires
import tempfile

with tempfile.TemporaryDirectory() as tempdir:
    print("Répertoire temporaire", tempdir)
    print("test")
# Le répertoire sera automatiquement supprimé à la sortie du bloc.
