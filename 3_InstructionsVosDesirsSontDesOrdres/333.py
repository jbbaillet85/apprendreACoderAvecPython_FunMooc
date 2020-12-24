"""Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur, imprime cette valeur (le programme n’imprime rien dans le cas contraire).
Exemple 1
Avec les données lues suivantes :
2
1
2
le résultat à imprimer vaudra :
2
Exemple 2
Avec les données lues suivantes :
1
2
3
le programme n’affichera rien.
Exemple 3
Avec les données lues suivantes :
42
42
42
le résultat à imprimer vaudra :
42
"""
a = int(input())
b = int(input())
c = int(input())
if a == b or b == c:
    print(b)
elif a == c:
    print(a)
