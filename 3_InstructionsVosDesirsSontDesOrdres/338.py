"""Écrire un programme qui imprime la moyenne géométrique \sqrt{a.b}
(la racine carrée du produit de a par b) de deux nombres positifs a et b de type float lus en entrée.
Si au moins un de ces nombres est strictement négatif, le programme imprime le texte « Erreur ».
Exemple 1
Avec les données lues suivantes :
1.0
2.0
le résultat à imprimer vaudra approximativement  :
1.4142135623730951
Exemple 2
Avec les données lues suivantes :
-1.0
2.0
le résultat à imprimer vaudra :
Erreur"""
https://www.fun-mooc.fr/courses/course-v1:ulb+44013+session04/courseware/63e9dd1bcf594fc4a084abc1531260d4/815669e67e584324ab1a5b4a912b28cf/

from math import sqrt

a = float(input())
b = float(input())

if a <0 or b < 0:
    print("Erreur")
elif a>0 or b > 0:
    print(sqrt(a*b))
