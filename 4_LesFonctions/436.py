"""L’exercice 4.3 d’UpyLaB vous propose une fonction assez classique à rédiger, qui teste si un nombre n , reçu en paramètre, est premier.
Par définition, un nombre entier naturel est premier s’il est divisible (entièrement) uniquement par deux nombres différents, par 1 et par lui-même. 1 n’est pas premier. Le plus petit nombre premier est 2. Tous les nombres premiers suivants sont impairs puisque tous les nombres pairs sont divisibles par 2.
Il faut rédiger une fonction booléenne (dont le résultat est True ou False), qui reçoit un entier positif et renvoie True si et seulement si n est un nombre premier.
L’exercice n’a pas d’applications pratiques dans ce cours, mais comme le problème est assez simple, c’est l’occasion d’essayer d’être le plus succinct possible. L’extrait de code suivant peut servir de base. Il vous reste à compléter le corps de la fonction premier.
def premier(n):
    "" renvoie vrai si n est un nombre premier""

    ...
    return res

# code principal
print("liste des nombres premiers jusqu'à 100")
for i in range(100):
    if premier(i):
        print(i)

MODULO

Dans la fonction premier, il faut vérifier que n n’est divisible par aucun des nombres entiers à partir de 2 et strictement inférieurs à lui-même. Pour cela, notons que l’opérateur modulo peut être utile : le test n % i == 0 est vrai si i divise n entièrement.

NB : Il est toutefois intéressant de constater qu’il n’est en fait nécessaire de vérifier cette condition que pour les nombres entiers qui sont inférieurs ou égaux à la racine carrée du nombre n. Si vous souhaitez rendre votre code plus efficace en réduisant le nombre d’instructions exécutées, la fonction sqrt du module math s’avèrera utile ici.
ÉNONCÉ EXERCICE UPYLAB 4.3

Rédigez dans un script PyCharm une fonction premier qui réalise le traitement expliqué précédemment, et le code qui l’appelle. Ensuite, pour valider votre solution, modifiez votre code pour répondre à l’exercice 4.3 d’UpyLaB, dont voici l'énoncé :
Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif n et qui renvoie True si n est un nombre premier, et False sinon.
Ensuite, écrire un programme qui lit une valeur entière x et affiche, grâce à des appels à la fonction premier, tous les nombres premiers strictement inférieurs à x, chacun sur sa propre ligne.
Exemple 1
Avec la donnée lue suivante :
7
le résultat à imprimer vaudra donc
2
3
5
Exemple 2
Avec la donnée lue suivante :
9
le résultat à imprimer vaudra donc
2
3
5
7
"""
def premier(n):
    """renvoi vrai si n est un nombre premier"""
    for i in range(1, n-1):
        if n % i == 0:
            i = True
            return i