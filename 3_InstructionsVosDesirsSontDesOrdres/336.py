"""Écrire un programme qui teste la parité d’un nombre entier lu sur input
et imprime True si le nombre est pair, False dans le cas contraire.
Exemple 1
Avec la donnée lue suivante :
13
le résultat à imprimer vaudra :
False
Exemple 2
Avec la donnée lue suivante :
42
le résultat à imprimer vaudra :
True
"""

nombre = int(input())
if nombre%2==0:
    print("True")
else:
    print("False")