"""Le Petit Prince vient de débarquer sur la planète U357, et il apprend qu'il peut y voir de belles aurores boréales !
La planète U357 a deux soleils : les étoiles E1515 et E666.  C'est pour cela que les tempêtes magnétiques sont permanentes, ce qui est excellent pour avoir des aurores boréales.
Par contre, il y fait souvent jour, sauf bien évidemment quand les deux soleils sont couchés en même temps.
Heureusement pour nous, une journée U357 s'écoule sur 24 heures comme sur notre Terre, et pour simplifier, nous ne prendrons pas en compte les minutes (on ne donne que les heures avec des valeurs entières entre 0 et 23). 
Nous vous demandons d'aider le Petit Prince à déterminer les périodes de jour et de nuit.
UPYLAB 4.2A
Pour cela, vous allez dans un premier temps écrire une fonction soleil_leve qui, pour un soleil particulier, reçoit trois valeurs entières en argument pour la planète :
     - l'heure de lever du soleil (entre 0 et 23)
     - l'heure du coucher du soleil (entre 0 et 23)
     - l'heure actuelle (entre 0 et 23)
et qui renvoie une valeur booléenne vraie si le soleil est levé sur la planète à l'heure donnée en troisième argument et fausse, s'il est couché.
On supposera que chacun des soleils ne se lève et ne se couche au plus qu'une seule fois par jour.
Il est toutefois possible que le lever ait lieu après l'heure du coucher, ce qui signifie dans ce cas que le soleil est levé au début de la journée, puis qu'il se couche, puis qu'il se lève à nouveau plus tard dans la journée.
Enfin, si l'heure du lever est la même que l'heure du coucher :
     - soit toutes deux valent 12, cela signifie que le soleil ne se lève pas de la journée,
     - soit toutes les deux valent 0, cela signifie que le soleil ne se couche pas de la journée.
Exemple 1
L'appel suivant de la fonction :
soleil_leve(6, 18, 10)
doit retourner
True
Exemple 2
L'appel suivant de la fonction :
soleil_leve(15, 8, 12)
doit retourner
False
Exemple 3
L'appel suivant de la fonction :
soleil_leve(12, 12, 10)
doit retourner
False
Exemple 4
L'appel suivant de la fonction :
soleil_leve(0, 0, 22)
doit retourner
True
"""



def soleil_leve(lever, coucher, heure):
	cas1=lever==coucher==0
	cas2=lever<=heure<coucher
	cas3=coucher<lever and (heure<coucher or lever <=heure)
	return cas1 or cas2 or cas3

"""Il vous faut maintenant écrire un programme qui lit en entrée :
. l'heure de lever du soleil E1515
. l'heure du coucher du soleil E1515
. l'heure de lever du soleil E666
. l'heure du coucher du soleil E666
et qui utilise la fonction soleil_leve pour afficher ligne par ligne chacune des heures de la journée, depuis 0 jusqu'à 23, suivies d'une espace et d'une astérisque s'il fait nuit à cette heure.
Attention, il ne fera nuit que si E1515 et E666 sont tous deux couchés.
Exemple 1
Avec les données lues suivantes :
6
18
10
21
le résultat à imprimer vaudra donc
0 *
1 *
2 *
3 *
4 *
5 *
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21 *
22 *
23 *
Exemple 2
Avec les données lues suivantes :
15
8
6
17
le résultat à imprimer vaudra donc
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23 
"""
def soleil_leve(lever, coucher, heure):
	cas1 = lever == coucher == 0
	cas2 = lever <= heure < coucher
	cas3 = coucher < lever and (heure < coucher or lever <= heure)
	return cas1 or cas2 or cas3

leverE1515 = int(input())
coucherE1515 = int(input())
leverE666 = int(input())
coucherE666 = int(input())
jour = leverE666 or leverE1515
for heure in range(24):
    if soleil_leve(leverE1515, coucherE1515, heure) or soleil_leve(leverE666, coucherE666, heure):
        print(heure)
    else:
        print(str(heure) + ' *')
        