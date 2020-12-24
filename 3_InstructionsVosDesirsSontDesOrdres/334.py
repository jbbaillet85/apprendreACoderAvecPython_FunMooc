"""Écrire un programme qui, si temperature (entier lu sur input correspondant à la température maximale
prévue pour aujourd’hui) est strictement supérieur à 0,
teste si temperature est inférieur ou égal à 10, auquel cas il imprime le texte :
    Il va faire frais.
et qui, si temperature n’est pas supérieur à 0, imprime le texte :
    Il va faire froid.
Dans les autres cas, le programme n’imprime rien.
Exemple 1
Avec la donnée lue suivante :
1
le résultat à imprimer vaudra :
Il va faire frais.
Exemple 2
Avec la donnée lue suivante :
20
le programme n’affichera rien.
Exemple 3
Avec la donnée lue suivante :
-1
le résultat à imprimer vaudra :
Il va faire froid."""

temperature = int(input())
if 0<temperature<10:
    print("Il va faire frais.")
elif temperature<=0:
    print("Il va faire froid.")