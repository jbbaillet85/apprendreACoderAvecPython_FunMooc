"""Écrire un programme qui lit en entrée deux nombres entiers strictement positifs,
et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.
Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.
Exemple 1
Avec les données lues suivantes :
6
42
le résultat à imprimer vaudra :
False
Exemple 2
Avec les données lues suivantes :
5
42
le résultat à imprimer vaudra :
True
"""

a = int(input())
b = int(input())

if b%a == 0 or a%b==0:
    print("False")
else:
    print("True")