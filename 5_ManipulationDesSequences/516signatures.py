"""

Écrire une fonction signature qui reçoit un paramètre identite . Ce paramètre est un couple (tuple de deux composantes) dont la première composante représente un nom et la seconde un prénom.
Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.
Exemple
L’appel suivant de la fonction :
signature(('de Saint-Exupéry', 'Antoine'))
doit retourner :
'Antoine de Saint-Exupéry'
"""
def signature(identité):
    identité = identité[1]+" "+identité[0]
    return identité

newsignature = signature(("baillet", "jb"))
print(newsignature)