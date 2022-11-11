Tirage au sort the noel
========================


un script pour faire un tirage au sort de cadeau de noel. Une personne offira un cadeau à une seul autre personne. Chaque personne fait partie d'un foyer.

Règles:

#. Il n'y a qu'une seule boucle fermée (en suivant qui offre à qui, on finit par la première personne).
#. Pas de cadeau intra-foyer, si possible.

La 2e règle n'est pas forcément optimisée: il faudra recommencer le tirage si on veut tenter de l'atteindre.

utilisation
===========

Exécuter le script tirage.py avec python pour lancer l'interface en console. Si on ne veut pas utiliser le mode interactif, changer la variable INTERACTIVE_MODE en False et changer le dictionnaire DEFAULT_PEOPLE selon le besoin.
