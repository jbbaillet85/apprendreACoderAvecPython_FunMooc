"""Cet exercice propose une variante de l’exercice précédent sur le carré de X.
Écrire un programme qui lit en entrée une valeur naturelle n 
et qui affiche à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).
Exemple 1
Avec la donnée lue suivante :
6
le résultat à imprimer vaudra :
XXXXXX
 XXXXX
  XXXX
   XXX
    XX
     X
Exemple 2
Avec la donnée lue suivante :
2
le résultat à imprimer vaudra :
XX
 X
"""
nbX = int(input())
espace = " "
increment = 0
for x in range(nbX):
     print(espace*increment + "X"*nbX)
     increment+=1
     nbX -= 1