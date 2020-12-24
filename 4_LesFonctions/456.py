"""Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro.
Écrire une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2 et x1, qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet dont le prix est mentionné.
La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre au client, dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de billets et pièces de grosses valeurs.
Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq valeurs None.
Exemple 1
L’appel suivant de la fonction :
rendre_monnaie(38, 1, 1, 1, 1, 1)
doit retourner :
(0, 0, 0, 0, 0)
Exemple 2
L’appel suivant de la fonction :
rendre_monnaie(56, 5, 0, 0, 0, 0)
doit retourner :
(2, 0, 0, 2, 0)
Exemple 3
L’appel suivant de la fonction :
rendre_monnaie(80, 2, 2, 2, 3, 3)
doit retourner :
(None, None, None, None, None)
"""
def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    somme = x20*20+x10*10+x5*5+x2*2+x1
    if somme < prix:
        rendre_monnaie = None, None, None, None, None
    else:
        rendre_monnaie = somme - prix
        res20 = (rendre_monnaie//20)
        rendre_monnaie = rendre_monnaie % 20
        res10 = (rendre_monnaie // 10)
        rendre_monnaie = rendre_monnaie % 10
        res5 = (rendre_monnaie // 5)
        rendre_monnaie = rendre_monnaie % 5
        res2 = (rendre_monnaie // 2)
        rendre_monnaie = rendre_monnaie % 2
        res1 = (rendre_monnaie // 1)
        rendre_monnaie = rendre_monnaie % 1
        rendre_monnaie = (res20, res10, res5, res2, res1)
    return rendre_monnaie