#! /usr/bin/env python3

"""Programme affichant les arguments qui lui sont fournis ainsi que leur indice si la variable d'environnement `DEBUG` est définie sur le shell. 
- Ce programme doit afficher un message d'erreur et renvoyer le code d'erreur 1 si aucun argument n'est fourni.
- Une fois le programme mis au point, poussez votre travail sur votre dépôt git et appelez l'enseignant avant de passer à l'exercice suivant."""
import os
import sys

def arguments():
    """Fonction qui affiche les arguments de la ligne de commande."""
    if "DEBUG" in os.environ:
        for k in range(len(sys.argv)):
            print("k "+ sys.argv[k])
    else:
        sys.stderr.write("Pas d'arguments fournie \n")
        sys.exit(1)
    



    

if __name__ == "__main__":
    arguments()         
