"""Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
La première donnée lue ne fait pas partie des valeurs à sommer. Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :
    si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;
    si elle est égale à -1, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée par le caractère "F" signifiant que la liste est terminée.
Exemple 1
Avec les données lues suivantes :
4
1
3
5
7
qui indiquent qu’il y a 4 données à sommer : 1 + 3 + 5 + 7,
le résultat à imprimer vaudra donc
16
Exemple 2
Avec les données lues suivantes :
-1
1
3
5
7
21
F
qui indiquent qu’il faut sommer : 1 + 3 + 5 + 7 + 21,
le résultat à imprimer vaudra donc
37
Exemple 3
Avec la donnée :
0
qui indique qu’il faut sommer 0 nombre,
le résultat à imprimer vaudra donc
0
"""
nombre = input()
sentinelleN = int(nombre)
increment = 0
sentinelleF = 'F'
somme = 0

if sentinelleN >= 0:
    nombre = int(nombre)
    while increment < sentinelleN:
        nombre = int(input())
        somme += nombre
        increment += 1
    print(somme)

else:
    while nombre != sentinelleF:
        nombre = input()
        if nombre == sentinelleF:
            nombre = sentinelleF
        else:
            nombre = int(nombre)
            somme += nombre
    print(somme)