# Générateur de mot de passe - Version 1.
# Ce programme génère un mot de passe sécurisé en fonction 
# des critères choisis par l'utilisateur.

# ------------------------------
# Partie logique du programme.
# ------------------------------

# Importation de modules.
import random
import string
def gerate_password(min_length,numbers = True, special_characters = True) :
    # Lettres majuscules et minuscules.
    letters = string.ascii_letters
    # chiffres de 0 à 9
    digits = string.digits
    # Caractères spéciaux (comme !, @, #, etc.).
    special = string.punctuation

    # on commence avec les lettres comme base.
    characters = letters
    #  Si l'utilisateur veut des chiffres, on les ajoute.
    if numbers :
        characters += digits
    # Si l'utilisateur veut des caractères speciaux, on les ajoute aussi.
    if special_characters :
        characters += special

    pwd = ""  # Mot de passe vide au départ.
    neets_criteria = False # Indique si le mot de passe respecte les critères.
    has_numbers = False # Vérifie s'il y a au moins un chiffre.
    has_special = False   # Vérifie s'il y a au moins un caractère spécial.

    # Boucle jusqu'à ce que le mot de passe soit assez long et respecte les critères.
    while not neets_criteria or len(pwd) < min_length :
        new_char = random.choice(characters) # # Choisit un caractère au hasard.
        pwd += new_char # Ajoute ce caractère au mot de passe.

        # Vérifie si le caractère est un chiffre.
        if new_char in digits :
            has_numbers = True
        # Vérifie si le caractère est special.
        elif new_char in special :
            has_special = True

        # On met à jour le critère général.
        neets_criteria = True
        if numbers :
            neets_cruteria = has_numbers
        if special_characters :
            neets_criteria = neets_criteria and has_special
    return pwd # Retourne le mot de passe final.

# ------------------------------
# Partie principale du programme.
# ------------------------------

# Titre du programme.
print("[ GENERATOR OF PASSWORD. ]")
print() #  ligne vide servant d'intervalle.
# Demande la longueur minimale du mot de passe.
min_length = int(input("Enter the minimum length :"))
# L'utilisateur choisit s'il veut des chiffres.
has_numbers = input("Do you want to have numbers(y/n) ?").lower() == "y"
# L'utilisateur choisit s'il veut des caractères spéciaux.
has_special = input("Do you want to have specials(y/n) ?").lower() == "y"
#Appelle la fonction de génération de mot de passe.
pwd = gerate_password(min_length,has_numbers,has_special)
# Affichage du mot de passe.
print("Password gerated :",pwd)

"""_______________Note importante:__________

> Dans cette première version, le mot de passe généré peut dépasser la longueur minimale demandée.
> Cela est dû à la logique de la boucle while, qui continue à ajouter des caractères tant que les critères (chiffres, spéciaux) ne sont pas remplis, même si la longueur est déjà atteinte.

-----------------------------------------------

--- Améliorations prévues---

- Corriger la logique pour garantir une *longueur exacte*
- Ajouter des *tests unitaires*
- Proposer une *interface graphique* simple (Tkinter ou web)
- Ajouter une option pour *exclure certains caractères*

-------–----------------------------------------

--- Ce que j’ai appris ---

- Utilisation des modules `string` et `random`
- Gestion des entrées utilisateur
- Importance de la logique de boucle
- Débogage et amélioration continue"""


