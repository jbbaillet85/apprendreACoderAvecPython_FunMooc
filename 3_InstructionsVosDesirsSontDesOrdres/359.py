"""Dans cet exercice, nous revenons sur le petit jeu de devinette.
Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100. Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.
À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :
    « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais
    « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais
    « Gagné en n essais ! » : si le nombre secret est trouvé
    « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.
Exemple 1
Une partie gagnante (après la génération du nombre à deviner) :
NB : Les nombres sont les valeurs saisies par l’utilisateur, et les textes sont imprimés par le programme.
50
Trop grand
8
Trop petit
20
Trop petit
27
Gagné en 4 essais !
Exemple 2
Une partie gagnante (après la génération du nombre à deviner) :
50
Trop grand
24
Trop petit
37
Trop petit
43
Trop grand
40
Trop petit
41
Perdu ! Le secret était 42
Consignes
    Attention, au dernier essai, le programme ne doit afficher ni « Trop petit » ni « Trop grand », mais le verdict comme illustré plus haut.
    Pour qu’Upylab puisse tester que votre solution est correcte, il faut que vous respectiez strictement la séquence décrite dans l’énoncé. Si par exemple, vous n’affichez pas « Trop petit » ou « Trop grand », le nombre suivant ne sera pas fourni par le système et votre solution sera considérée comme incorrecte.
    En pratique, pour la génération du nombre secret, vous devez débuter votre code comme suit :
    import random
    NB_ESSAIS_MAX = 6
    secret = random.randint(0, 100)
    et ne pas faire d’autre appel à randint ou à une autre fonction du module random."""
    import random

NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
essais = int(input())
nb_essais = 1

while essais != secret and nb_essais < NB_ESSAIS_MAX:
	if essais < secret:
		print('Trop petit')
	else:
		print('Trop grand')
	essais = int(input())
	nb_essais += 1

if essais == secret:
	print('Gagné en {} essais ! '.format(nb_essais))
else:
	print('Perdu ! Le secret était {} '.format(secret))