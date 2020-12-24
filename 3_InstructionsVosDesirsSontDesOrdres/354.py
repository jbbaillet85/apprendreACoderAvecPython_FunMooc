"""Écrire un programme qui calcule la taille moyenne (en nombre de salariés) des Petites
et Moyennes Entreprises de la région.
Les tailles seront données en entrée, chacune sur sa propre ligne,
et la fin des données sera signalée par la valeur sentinelle -1.
Cette valeur n’est pas à comptabiliser pour le calcul de la moyenne,
mais indique que l’ensemble des valeurs a été donné.
Après l’entrée de cette valeur sentinelle -1, le programme affiche la valeur de la moyenne arithmétique calculée.
On suppose que la suite des tailles contient toujours au moins un élément avant la valeur sentinelle -1,
et que toutes ces valeurs sont positives ou nulles.
Exemple 1
Avec les données lues suivantes :
11
8
14
5
-1
le résultat à imprimer vaudra :
9.5
Exemple 2
Avec les données lues suivantes :
12
6
7
-1
le résultat à imprimer vaudra approximativement :
8.333333333333334
"""
listeSalaries = 0
entreprises = 0
sentinelle = "-1"
nbSalaries = input("Entrez votre nombre de salariés")
while nbSalaries != sentinelle:
    nbSalaries = int(nbSalaries)
    listeSalaries += nbSalaries
    entreprises += 1
    nbSalaries = input("Entrez votre nombre de salariés")
moyenne = listeSalaries / entreprises
print(f"la taille moyenne en nombre de salariés de la région est de {moyenne}")