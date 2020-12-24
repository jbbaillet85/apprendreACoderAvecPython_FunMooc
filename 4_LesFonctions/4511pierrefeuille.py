"""

Pierre-feuille-ciseaux (voir Pierre-papier-ciseaux sur Wikipedia) est un jeu effectué avec les mains et opposant un ou plusieurs joueurs.

Déroulement du jeu

Les deux joueurs choisissent simultanément un des trois coups possibles en le symbolisant de la main :

    poing fermé : Pierre ;

    main ouverte, doigts collés les uns aux autres : Feuille ;

    main avec pouce, annulaire et auriculaire fermé, index et majeur ouvert en forme de V : Ciseaux.

La pierre bat les ciseaux (en les émoussant), les ciseaux battent la feuille (en la coupant), la feuille bat la pierre (en l’enveloppant). Ainsi chaque coup bat un autre coup, fait match nul contre le deuxième (son homologue) et est battu par le troisième.

Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur. Chaque manche va consister en :

    la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random, qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;

    la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ;

    l’affichage du résultat sous une des formes :

        coup_o bat coup_j : points

        coup_o est battu par coup_j : points

        coup_o annule coup_j : points

    où

        coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : "Pierre" s’il a joué 0, "Feuille" s’il a joué 1 et "Ciseaux" s’il a joué 2.

        points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, et est incrémenté de un chaque fois que le joueur gagne une manche, et décrémenté de un chaque fois que l’ordinateur gagne une manche (les match nuls ne modifiant pas le compteur points).

À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou strictement positif.

Pour plus de clarté dans votre code, nous vous conseillons de définir les trois constantes symboliques :

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

Par ailleurs, votre code doit importer le module random et, avant de commencer les manches, pour permettre à UpyLaB de valider les résultats, il doit d’abord lire une valeur entière s et appeler la fonction random.seed(s). Vous devez donc intégrer le code suivant :

import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

...

s = int(input())
random.seed(s)

Votre code fera donc un appel à random.seed suivi de cinq appels à random.randint, un par manche. Aucun autre appel à une fonction de random ne pourra être effectué.

Vous pouvez bien sûr utiliser la fonction bat de l’exercice 4.10 mais nous vous conseillons vivement de définir aussi d’autres fonctions (par exemple , une fonction qui réalise une manche et imprime la ligne de message) pour structurer votre code.
Exemple 1

Sachant que le code suivant :

random.seed(65)
for i in range(5):
    print(random.randint(0,2))

donne le résultat :

1
1
1
2
0

l’exécution du code avec les entrées :

65
0
1
2
1
0

doit afficher :

Feuille bat Pierre : -1
Feuille annule Feuille : -1
Feuille est battu par Ciseaux : 0
Ciseaux bat Feuille : -1
Pierre annule Pierre : -1
Perdu

Exemple 2

Sachant que le code suivant :

random.seed(1515)
for i in range(5):
    print(random.randint(0,2))

donne le résultat :

2
1
0
2
2

l’exécution du code avec les entrées :

1515
0
1
2
1
0

doit afficher :

Ciseaux est battu par Pierre : 1
Feuille annule Feuille : 1
Pierre bat Ciseaux : 0
Ciseaux bat Feuille : -1
Ciseaux est battu par Pierre : 0
Nul

Exemple 3

Sachant que le code suivant :

random.seed(2001)
for i in range(5):
    print(random.randint(0,2))

donne le résultat :

2
0
1
0
0

l’exécution du code avec les entrées :

2001
0
1
2
1
0

doit afficher :

Ciseaux est battu par Pierre : 1
Pierre est battu par Feuille : 2
Feuille est battu par Ciseaux : 3
Pierre est battu par Feuille : 4
Pierre annule Pierre : 4
Gagné

"""
import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2

TEXTES = ('PIERRE', 'FEUILLE', 'CISEAUX')


def bat(coup_1, coup_2):
    return coup_1 == (coup_2 + 1) % 3

def resulat_manche():
    if bat(coup_o, coup_j):
        pt = -1
        verbe = 'bat'
    elif bat(coup_j, coup_o):
        pt = 1
        verbe = 'est battu par'
    else:
        pt = 0
        verbe = "annule"
    return pt, verbe

def score():
    if score > 0:
        print('Gagne')
    elif score == 0:
        print('Nul')
    else:
        print('Perdu')

def manche(score):
    coup_o = randint(0, 2)
    coup_j = int(input("Entrez votre choix: 0 pour Pierre,"
                       "\n 1 pour feuille,"
                       "\n, ou 2 pour Ciseaux:  "))
    pt, verbe = resulat_manche(coup_o, coup_j)
    score += pt
    print('{} {} {} : {}'.format(TEXTES[coup_o], verbe, TEXTES[coup_j], [score]))
    return score

def jeu(nb_manches):
    # realiser les nb de manches
    random.seed(int(input("Entrez un nombre:  ")))
    score = 0
    for i in range(nb_manches):
        score = manche(score)
    # afficher le resultat final
        resultat_manche(score)

print("Bienvenu dans le jeux Pierre Feuille Ciseaux")
jeu()