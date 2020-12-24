"""
Dans mon casino, ma roulette comporte 13 numéros de 0 à 12 comme montrés ci-dessous :
https://studio.fun-mooc.fr/asset-v1:ulb+44013+session03+type@asset+block/roulette.jpg
Roulette
Le joueur a plusieurs types de paris possibles :
    il peut choisir de parier sur le numéro sortant, et dans ce cas, s’il gagne,
    il remporte douze fois sa mise ;
    il peut choisir de parier sur la parité du numéro sortant (pair ou impair),
    et dans ce cas, s’il gagne, il remporte deux fois sa mise ;
    enfin, il peut choisir de parier sur la couleur du numéro sortant (rouge ou noir),
    et dans ce cas aussi, s’il gagne, il remporte deux fois sa mise.
Si le joueur perd son pari, il ne récupère pas sa mise.
Pour simplifier, on suppose que le numéro 0 n’est ni rouge ni noir, mais est pair. Pour simplifier encore, on suppose que le joueur mise systématiquement 10 euros.
Écrire un programme qui aide le croupier à déterminer la somme que le casino doit donner au joueur.
Le programme lira, dans l’ordre, deux nombres entiers en entrée :
le pari du joueur (représenté par un nombre entre 0 et 16, voir description plus bas),
et le numéro issu du tirage (nombre entre 0 et 12).
Le programme affichera alors le montant gagné par le joueur.
Entrées pour le pari du joueur :
    nombre entre 0 et 12 : le joueur parie sur le numéro correspondant
    13 : le joueur parie sur pair
    14 : le joueur parie sur impair
    15 : le joueur parie sur la couleur rouge
    16 : le joueur parie sur la couleur noire.
Exemple 1
Avec les données lues suivantes :
7
9
qui indiquent que le joueur parie sur le numéro 7 et que le numéro sorti est le 9,
le résultat à imprimer vaudra donc
0
Exemple 2
Avec les données lues suivantes :
16
4
qui indiquent que le joueur parie sur la couleur noire et que le numéro sorti est le 4 (qui est noir),
le résultat à imprimer vaudra donc
20
soit deux fois sa mise de 10 euros.
Exemple 3
Avec les données lues suivantes :
7
7
qui indiquent que le joueur parie sur le numéro 7 et que le numéro sorti est bien le 7,
le résultat à imprimer vaudra donc
120
soit douze fois sa mise de 10 euros.
"""